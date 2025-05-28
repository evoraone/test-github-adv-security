import os

# def connect_to_service():
#     # Simulated leaked secret
#     secret_key = "AKIAFAKEKEY1234567890"
#     print("Connecting with secret:", secret_key)

# def send_token():
#     github_token = "ghp_1234567890fakeTOKENtoTriggerScan9876543210"
#     print(github_token)
    
# Triggers a SonarQube Code issue
def unused_function():
    pass
# Triggers a SonarQube security hotspot
def insecure_eval(user_input):
    eval(user_input)  
# Triggers a SonarQube Duplication issue
def greet_user(name):
    print(f"Hello, {name}!")

def say_hello(name):
    print(f"Hello, {name}!")  # Duplicate code

if __name__ == "__main__":
    connect_to_service()
