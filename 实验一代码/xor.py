a = input()
b = input()
p0 = [int(byte) for byte in bytes.fromhex(a)]
p1 = [int(byte) for byte in bytes.fromhex(b)]

index = 0
result = []

for index in range(min(len(p0), len(p1))):
    result.append(p0[index] ^ p1[index])

hex_string = ''.join([format(value, '02x') for value in result])

print(result)
print(hex_string)




