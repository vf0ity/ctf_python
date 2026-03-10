import base64

def encode_base64(data):
    return base64.b64encode(data.encode()).decode()

def decode_base64(data):
    return base64.b64decode(data).decode()

def encode_hex(data):
    return data.encode().hex()

def decode_hex(data):
    return bytes.fromhex(data).decode()

# ASCII encoding/decoding

def encode_ascii(data):
    return ''.join(format(ord(c), '02x') for c in data)

def decode_ascii(data):
    return bytes.fromhex(data).decode('ascii')

# Common CTF encoding schemes

def encode_ctf(data):
    return encode_base64(encode_hex(data))

def decode_ctf(data):
    return decode_hex(decode_base64(data))