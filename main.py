import requests
from utils import check_username
import colorama
from colorama import Fore, Style
import os
import tkinter as tk
from tkinter import simpledialog, messagebox
import time
import random
import string

colorama.init(autoreset=True)

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_alert(title, description):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, description)
    root.destroy()

def print_cover():
    print(Fore.BLUE + """
██████╗░██████╗░░█████╗░██╗░░██╗███████╗███████╗████████╗██╗░░██╗░█████╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝╚════██║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗
██║░░██║██████╔╝███████║█████═╝░░░███╔═╝█████╗░░░░░██║░░░███████║███████║██████╔╝
██║░░██║██╔══██╗██╔══██║██╔═██╗░██╔══╝░░██╔══╝░░░░░██║░░░██╔══██║██╔══██║██╔══██╗
██████╔╝██║░░██║██║░░██║██║░╚██╗███████╗███████╗░░░██║░░░██║░░██║██║░░██║██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
""")

# You can customize this function to search for the type of usernames you want
def generate_username():
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for _ in range(4))

def find_4l_username():
    with open("valid_usernames.txt", "a") as file:
        while True:
            username = generate_username()
            print(f"{Fore.YELLOW}[?] Checking username {username}")  
            resp_to_check_user = check_username(username)
            if resp_to_check_user == False:
                print(f"{Fore.GREEN}[+] 4L username found: {username}")
                file.write(username + '\n')  # Escribir el nombre de usuario en el archivo
            elif resp_to_check_user == True:
                print(f"{Fore.RED}[-] Username already taken: {username}")
            else:
                print(f"{Fore.RED}[-] Skipping: {username} (due to rate limit)")

clear()
print_cover()
print(f"{Fore.BLUE}Drakzethar {Fore.GREEN}is ready!")
print("")
r = input(f"{Fore.GREEN}Do you want to search 4l's? yes/no [default/empty: yes] >> {Fore.RESET}")
if r != "no":
    find_4l_username()
    print(f"{Fore.RED}[-] Work finished, closing in 15 seconds...")
    time.sleep(15)
else:
    print(f"{Fore.RED}[-] Okay, closing in 5 seconds...")
    time.sleep(5)
