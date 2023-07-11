def XOR(str_one, str_two):
    i1 = int(str_one, 16)
    i2 = int(str_two, 16)
    res = i1 ^ i2
    result = format(res, 'x')
    return result

def main():
    str_one = "4b64ca12ace755516c178f72d05d7061"
    str_two = "ecd44646cfe5994ebeb35bf922e25dba"
    answer = XOR(str_one, str_two)
    print("your flag is:", answer)

if __name__ == "__main__":
    main()
