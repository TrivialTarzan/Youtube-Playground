import json


def get_credentials(filepath="credentials.json") -> list:
    with open(filepath, "r") as file:
        credentials = json.load(file)
        login = credentials.get("login")
        password = credentials.get("password")
    credentials = [login, password]
    return credentials
