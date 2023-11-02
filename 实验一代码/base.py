import base64

if __name__ == '__main__':
    string_src = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    raw_src = bytes.fromhex(string_src)

    # encode to base64
    b64_string = base64.encodebytes(raw_src)

    print(b64_string)
