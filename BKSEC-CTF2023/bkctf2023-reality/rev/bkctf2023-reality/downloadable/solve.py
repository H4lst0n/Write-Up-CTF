key = "BKSEECCCC!!!"
v7 = [0, 0, 0, 0, 6]
v8 = [0, 38, 119, 48, 88, 126, 66, 42, 127, 63, 41, 26, 33, 54, 55, 28, 85, 73, 18, 48, 120, 12, 40, 48, 48, 55, 28, 33, 18, 126, 82, 45, 38, 96, 26, 36, 45, 55, 114, 28]
v9 = [69, 68, 67, 55, 44, 108, 122, 56]

x = v7 + v8 + v9

v5 = len(key)
for i in range(len(x)):
    result_byte = ord(key[i % v5])
    x[i] ^= result_byte

result_string = ''.join(chr(byte) for byte in x)

print(result_string)
