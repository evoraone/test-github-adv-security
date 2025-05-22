import os

def connect_to_service():
    # Simulated leaked secret
    secret_key = "AKIAFAKEKEY1234567890"
    print("Connecting with secret:", secret_key)

def send_token():
    github_token = "ghp_1234567890fakeTOKENtoTriggerScan9876543210"
    print(github_token)

if __name__ == "__main__":
    connect_to_service()
