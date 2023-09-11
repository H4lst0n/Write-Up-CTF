enc = "xk|nF{quxzwkgzgwx|quitH"
flag = ""
for i in range(len(enc)):
    flag += chr(ord(enc[i]) - 8)

print(flag)
