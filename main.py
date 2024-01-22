from flask import Flask, request, jsonify
from equations import eq, normalize, unnormalize
import sys
from flask_cors import CORS
from simplifyraw import simplifyraw
import re
from openai import OpenAI
import normalization

app = Flask(__name__)
CORS(app)
client = OpenAI()
#Get ChatGPT to get the equation set up
def askchatgpt(content):
    sentence = client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[{'role':'system', 'content':'You are going to be given a problem and you need to extrapolate the equation or expression needed to solve it. Only return the set-up equation, do not return any words.'},
                    {"role": "user",
                           "content": content}],
                n=1,
                max_tokens=100
            )
    jt = sentence.choices[0].message.content
    return jt
#Normalize data to be fed into solving algorithms
def normalvar(arr):
    arr = arr.replace(' ', '')
    normalized = re.sub(r'(?<![\+\-\*/\^(])-(?![\+\-\*/\^\d])', '+-', arr)
    # Add a '+' after an opening parenthesis if the expression starts with a negative number
    normalized = re.sub(r'\(\-(\d+\.?\d*)\)', r'(+\1)', normalized)


    # Normalize standalone subtraction (e.g., '4-6' becomes '4+-6')
    arr = re.sub(r'(\d+\.?\d*)-(?=\d)', r'\1+-', normalized)
    arr = arr.replace('ln', '%')
    arr = arr.replace('arccsc', '1/arcsin')
    arr = arr.replace('arcsec', '1/arccos')
    arr = arr.replace('arccot', '1/arctan')
    arr = arr.replace('arcsin', '¸')
    arr = arr.replace('arccos', '®')
    arr = arr.replace('arctan', '¯')
    arr = arr.replace('csc', '/sin')
    arr = arr.replace('sec', '/cos')
    arr = arr.replace('cot', '/tan')
    arr = arr.replace('sin', '@')
    arr = arr.replace('cos', '?')
    arr = arr.replace('tan', ';')
    arr = arr.replace('sqrt', '¿')
    arr = arr.replace('cbrt', '»')
    return arr
#Unnormalize some data
def unnormalvar(arr):
    arr = arr.replace('%', 'ln')
    arr = arr.replace('@', 'sin')
    arr = arr.replace('?', 'cos')
    arr = arr.replace(';', 'tan')
    return arr
#Process Input
def process_input(user_inputs):
    user_input = askchatgpt(user_inputs)
    with open('output.txt', 'w') as f:
        sys.stdout = f
        try:
            usernormal = user_input
            usernormalsplit = usernormal.split(',')
            usernormal = normalvar(usernormal)
            list_vars = []
            for char in usernormal:
                if char.isalpha():
                    list_vars.append(char)
            if len(list_vars) == 0:
                usernormal = simplifyraw(usernormal)
                print(usernormal)
            elif not '=' in usernormal:
                return (normalization.mathjax(normalization.simplified(usernormal)))
            elif all(i == list_vars[0] for i in list_vars):
                eq(user_input, list_vars[0])
            else:
                return process_input(user_inputs)
        finally:
            sys.stdout = sys.__stdout__

    strings = []
    with open('output.txt', 'r') as f:
        strings.append(f.read())
    return '\n'.join(strings)

@app.route('/process_user_input', methods=['POST'])
def process_user_input():
    try:
        # Retrieve data from the incoming JSON request
        data = request.get_json()
        user_input = data.get('userInput')

        # Process the user input (you can replace this with your own logic)
        processed_result = process_input(user_input)
        print(processed_result)
        # Return the processed result as JSON
        return jsonify({'result': processed_result})
    except Exception as e:
        # Handle exceptions and return an error response
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)




