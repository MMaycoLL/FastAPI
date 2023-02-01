from jwt import encode

def create_token(data: dict):
    token: str = encode(payLoad=data, key="my_secrete_key", algorithm="HS256")
    return token

