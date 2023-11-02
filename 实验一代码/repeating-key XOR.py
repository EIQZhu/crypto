def repeating_key_xor(stream: bytes, key: bytes) -> bytes:
    return bytes([letter ^ key[idx % len(key)] for idx, letter in enumerate(stream)])


if __name__ == '__main__':
    stream = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b'ICE'

    res = repeating_key_xor(stream, key)

    print(res.hex())