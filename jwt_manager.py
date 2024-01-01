from jwt import encode

def create_token(data):
    token = encode(payload=dict(data), key="my_secret_key", algorithm="HS256")