from flask import Flask, request, jsonify
from equations import eq
import sys
from flask_cors import CORS
from simplifyraw import simplifyraw
import re
from openai import OpenAI
import normalization

"""
Please Note that throughout this entire project, I have prioritized development speed over perfection. I am aware
there are many redundancies, as well as points where code may have faster time complexity or more efficient memory
allocation. My aim is not to fix that yet. My aim is to prove that this theory of solving math problems discretely
is better than solving math problems by generating tokens.
"""

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
                max_tokens=200
            )
    jt = sentence.choices[0].message.content
    return jt

#Process Input
def process_input(user_inputs):
    user_input = askchatgpt(user_inputs)
    user_input = user_input.replace(' ', '')
    with open('output.txt', 'w') as f:
        sys.stdout = f
        try:
            usernormalsplit = user_input.split(',')
            usernormal = normalization.normalizeraw(user_input)
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
                #Sometimes chatgpt returns a sentence. I have not
                # cared about prompt optimization because ideally it would have a local fine-turned LLM in the future anyways.
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



