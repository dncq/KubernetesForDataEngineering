import base64

with open("token_base64.txt", "r") as file:
    token_base64 = file.read().strip()
    token = base64.b64decode(token_base64).decode('utf-8')
    print(token)
