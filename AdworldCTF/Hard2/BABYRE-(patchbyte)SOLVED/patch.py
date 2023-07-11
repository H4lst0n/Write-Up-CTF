st = 0x600b00
for i in range(182):
    patch_byte(st + i, ord(get_bytes(st + i, 1))^0xC)
    
