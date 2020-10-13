import re

password = r"^\D[A-Za-z]\S+[0-9]*$"
password_list = []

def valid(*args):
    try:
        with open('password.txt', 'r') as f:
            for line in f:
                valid_passwords = re.search(password, line)
                if len(line) > 7:
                    password_list.append(line.strip())
                    print(valid_passwords.group())
    except TypeError:
        print("Missing an argument in your valid_passwords variable.")
    return line

valid(password)
print(f'password_list: {password_list}')