import os
from flask import Flask, request

app = Flask(__name__)

    #Triggers a CodeQL alert
@app.route('/eval')
def unsafe():
    user_input = request.args.get('input')
    eval(user_input)   
    return "done"

def connect_to_service():

# # Triggers a SonarQube Code issue
# def unused_function():
#     pass
# # Triggers a SonarQube security hotspot
# def insecure_eval(user_input):
#     eval(user_input)  
# # Triggers a SonarQube Duplication issue
# def greet_user(name):
#     print(f"Hello, {name}!")

# def say_hello(name):
#     print(f"Hello, {name}!")  # Duplicate code

if __name__ == "__main__":
    connect_to_service()
