import requests
import tkinter as tk
import ClientKit.Session

login_window = tk.Tk()
register_window = tk.Tk()
action_window = tk.Tk()

def login():
    login_window.title("Login")
    login_window.geometry("600x400")

    login_username_var = tk.StringVar()
    login_password_var = tk.StringVar()

    login_username_label = tk.Label(login_window, text="Username", font=("calibre", 10, "bold"))
    login_username_entry = tk.Entry(login_window, textvariable=login_username_var, font=("calibre", 10, "normal"))
    login_password_label = tk.Label(login_window, text="Password", font=("calibre", 10, "bold"))
    login_password_entry = tk.Entry(login_window, textvariable=login_password_var, font=("calibre", 10, "normal"), show="*")
    login_button = tk.Button(login_window, text="Login", command= lambda: login_exec(login_username_entry.get(), login_password_entry.get()))

    login_username_label.grid(row=0, column=0)
    login_username_entry.grid(row=0, column=1)
    login_password_label.grid(row=1, column=0)
    login_password_entry.grid(row=1, column=1)
    login_button.grid(row=2, column=1)

    login_window.mainloop()




def login_exec(username, password):

    login_window.destroy()
    login_url = "https://onlineservices.adriandevprojects.com/v1/auth/login/"

    login_credentials = {
        "username": username,
        "password": password
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(login_url, data=login_credentials, headers=headers)

    if response.status_code == 200:
        user_file = open("user.txt", "w")
        user_file.write(response.text)
        user_file.close()
        ClientKit.Session.initialize()
    else:
        print(f"Login failed: {response.text}")


def register():
    register_window.title("Login")
    register_window.geometry("600x400")

    register_username_var = tk.StringVar()
    register_password_var = tk.StringVar()
    register_confirm_password_var = tk.StringVar()

    register_username_label = tk.Label(login_window, text="Username", font=("calibre", 10, "bold"))
    register_username_entry = tk.Entry(login_window, textvariable=register_username_var, font=("calibre", 10, "normal"))
    register_password_label = tk.Label(login_window, text="Password", font=("calibre", 10, "bold"))
    register_password_entry = tk.Entry(login_window, textvariable=register_password_var, font=("calibre", 10, "normal"), show="*")
    register_confirm_password_label = tk.Label(login_window, text="Confirm Password", font=("calibre", 10, "bold"))
    register_confirm_password_entry = tk.Entry(login_window, textvariable=register_confirm_password_var, font=("calibre", 10, "normal"), show="*")
    register_button = tk.Button(login_window, text="Register", command= lambda: register_exec(register_username_entry.get(), register_password_entry.get(), register_confirm_password_entry.get()))

    register_username_label.grid(row=0, column=0)
    register_username_entry.grid(row=0, column=1)
    register_password_label.grid(row=1, column=0)
    register_password_entry.grid(row=1, column=1)
    register_confirm_password_label.grid(row=2, column=0)
    register_confirm_password_entry.grid(row=2, column=1)
    register_button.grid(row=3, column=1)

    login_window.mainloop()




def register_exec(username, password, confirm_password):

    register_window.destroy()
    register_url = "https://onlineservices.adriandevprojects.com/v1/auth/register/"

    register_credentials = {
        "username": username,
        "password": password,
        "confirm_password": confirm_password
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(register_url, data=register_credentials, headers=headers)

    if response.status_code == 201:
        login_exec(register_credentials.get(username), register_credentials.get(password))
    else:
        print(f"Registration failed: {response.text}")

