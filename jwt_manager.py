from jwt import encode, decode

def create_token(data):
    token = encode(payload=dict(data), key="my_secret_key", algorithm="HS256")
    print(f"The data entered is: {data}")
    return token

def validate_token(token: str):
    data = decode(token, key="my_secret_key", algorithms=['HS256'])
    print(f"The data returned is: {data}")
    return data