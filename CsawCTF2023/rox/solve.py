data = ELF("./food").read(0x403740, 0x36a4)
data = [u32(data[i:i+4]) for i in range(0,len(data),4)]

for i in range(len(check)):
    vals = set()
    for j in range(0x20,0x80):
        key = data[(data[(10 * i + 12) % len(data)] + j) % len(data)]
        out = flag[i] ^ key ^ j
        if out == x[i]:
            vals.add(j)
    print(bytes(vals))
