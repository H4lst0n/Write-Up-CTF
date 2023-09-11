def checkName(name):
    check = name[::-1]
    return check == "uyjnimda"

def checkLength(pwd):
    return len(pwd) % 6 == 0

def checkValidity(password):
    arr = [ord(e) for e in password if 97 <= ord(e) <= 122]

    sum_val = 0
    i = 0
    while i < len(arr):
        add = arr[i] & arr[i + 2]
        or_val = arr[i + 1] | arr[i + 4]
        xor = arr[i + 3] ^ arr[i + 5]
        if add == 96 and or_val == 97 and xor == 6:
            sum_val += add + or_val - xor
        i += 6

    return sum_val == 187

# Example usage:
name = "adminjyu"
password = "abcdef"
if not checkName(name):
    print('Incorrect Name! 😥😥')
else:
    print('Correct Name! 🙂🙂')

if not checkValidity(password) and not checkLength(password):
    print('Incorrect Password! 😥😥')
else:
    print('Correct Password! 🙂🙂')
