This project is about developing computationally faster and more accurate ways to solve math problems. The fundamental part of this project is revolved around the idea that math
is absolutely discrete. There is a set of steps you can get to in order to solve a problem, and there is a well-established right and wrong way. Therefore, similarly to how we 
learned to solve math, I am attempting to teach a computer to solve math algebraically. There are 2 advantages to solving a math problem algebraically over computationally
(computationally meaning brute force or large language models). The first advantage is the way less computation power because of either much less generated tokens or far less
computation to get a precise value. The second advantage is you then get the work shown to get the correct answer.

It is important to note that I am aware as to how inefficient my current code is. It's fairly ugly; I could replace a lot of '().replace' with more efficient libraries
such as re. I have parts of my code that are redundant and do the same thing. Computationally, it has a lot of optimization that can be done with time complexity and memory
allocation. There isn't even a dedicated large language model to tokenize proper outputs; I'm just using an API connected to chatgpt because right now I don't have extremely
large data sets or computing power. The project is simply not done. Right now, I am prioritizing development speed over efficiency to get this proof of concept working, and 
there is still a lot more work ahead of me. Once that's done, I will clean it up significantly.
