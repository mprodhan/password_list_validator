import re

password = r"^\D[A-Za-z]\S+[0-9]*$"
password_list = []

# def password_add(*args):
#     with open('password.txt', 'a') as fa:
#         for i in range(i + 1):
#             password = input("Enter the next password: ")
#             fa.write(password + '\n')
#     return password_list

# password_add()

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

