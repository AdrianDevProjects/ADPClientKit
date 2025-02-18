import pathlib
import ClientKit.Auth

user_uid = ""

def initialize():
    if pathlib.Path("user.txt").is_file():
        with open("user.txt", "r") as user_file:
            user_id = user_file.read()
            if not user_id:
                ClientKit.Auth.login()
            else:
                user_uid = user_id
    else:
        ClientKit.Auth.login()
