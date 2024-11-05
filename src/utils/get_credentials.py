import json

# Credentials are loaded from a JSON file that is excluded from the project.
# To use this code, you must sign up for the Allegro sandbox website and provide your own credentials


def get_credentials(filepath="credentials.json") -> list:
    with open(filepath, "r") as file:
        credentials = json.load(file)
        login = credentials.get("login")
        password = credentials.get("password")
    credentials = [login, password]
    return credentials
