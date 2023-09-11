enc = "bHEC_T]PLKJ{MW{AdW]Y"
print(ord(enc[0]) ^ ord('F'))
flag = ""
for i in range(len(enc)):
    flag += chr(ord(enc[i]) ^ 36)
    
print(flag)