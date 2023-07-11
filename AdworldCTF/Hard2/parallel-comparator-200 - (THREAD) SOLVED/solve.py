d = [0, 9, -9, -1, 13, -13, -4, -11, -9, -1, -7, 6, -13, 13, 3, 9, -13, -11, 6, -7]
for j in range(26):
    flag = ""
    for i in range(20):
        fl = (j % 26) + 97
        flag += chr(fl + d[i])
    print(flag)