import os


async def get_private_key():
    """
    This function reads the private key from a file and returns it.
    """
    with open(os.path.join(os.path.dirname(__file__), ".", "keys/jwt-private.pem"), "rb") as key_file:
        private_key = key_file.read()
    return private_key

async def get_public_key():
    """
    This function reads the public key from a file and returns it.
    """
    with open(os.path.join(os.path.dirname(__file__), ".", "keys/jwt-public.pem"), "rb") as key_file:
        public_key = key_file.read()
    return public_key