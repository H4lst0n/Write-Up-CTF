import string
from random import *
seed(10)

def decode_finalstage(encoded_flag):
    reversed_w = encoded_flag[::-1]
    flag = ""
    h = 0
    while h < len(reversed_w):
        try:
            flag += reversed_w[h+1] + reversed_w[h]
        except:
            flag += reversed_w[h]
        h += 2
    return flag

def decrypt_stage2(t):
    encrypted_string = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++.++++++.-----------.++++++."[-15:(7*9)].strip('-')
    original_length = len(encrypted_string)
    t = encrypted_string + t[:original_length - len(t)]
    b = ""
    for q in range(len(t)):
        b += chr(ord(t[q]) + randint(0, 5))
    return b

def decrypt_stage1(z):
    b = list(string.ascii_lowercase)
    a = [""] * len(z)
    for y in range(len(z)):
        decrypted_char = ord(z[y]) ^ ord(b[y % len(b)])
        while decrypted_char < 0x00:
            decrypted_char += 0x100
        while decrypted_char > 0xFF:
            decrypted_char -= 0x100
        a[y] = chr(decrypted_char)
    return "".join(a)


def decrypt_entry(f):
    f = list(f)
    f.reverse()
    f = "".join(i for i in f)
    return f

flag = open('output.txt', 'r').readlines()[0]
fl1 = decode_finalstage(flag)
print(fl1)
fl2 = decrypt_stage2(fl1)
print(fl2)
fl3 = decrypt_stage1(fl2)
print(fl3)
fl4 = decrypt_entry(fl3)
print(fl4)


