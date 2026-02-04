import os
from dotenv import load_dotenv

# Loads the variables from the .env file when this module is imported
load_dotenv()

def get_orange_url():
    return os.getenv("ORANGE_URL")

def get_orange_username():
    return os.getenv("ORANGE_USERNAME")

def get_orange_password():
    return os.getenv("ORANGE_PASSWORD")