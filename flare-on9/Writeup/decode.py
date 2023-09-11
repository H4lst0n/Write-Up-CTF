v1 = "T{xdr_vys{r"
v2 = "TxyyrtcYvzrsG~gr"
v3 = "TervcrYvzrsG~grV"
v4 = "TervcrC\x7Fervs"
v5 = "S~dtxyyrtcYvzrsG~gr"
v6 = "Q{bd\x7FQ~{rUbqqred"
v7 = "Prc[vdcReexe"
v8 = "PrcGextrdd_rvg"
v9 = "{dcetzgV"
v10 = "ErvsQ~{r"
v11 = "@e~crQ~{r"
aKk9kgGrkqVerxy = "KK9Kg~grKQ{verXy"
aVbcXeMvcXy7qvR = "Vbc\x7Fxe~mvc~xy7Qv~{rs"
def x(v):
    f = ""
    for i in range(len(v)):
        f += chr(ord(v[i]) ^ 0x17)
    
    return f

print(x(v1))
print(x(v2))
print(x(v3))
print(x(v4))
print(x(v5))
print(x(v6))
print(x(v7))
print(x(v8))
print(x(v9))
print(x(v10))
print(x(v11))
print(x(aKk9kgGrkqVerxy))
print(x(aVbcXeMvcXy7qvR))

c = [0x3E, 0x39, 0x51, 0xFB, 0xA2, 0x11, 0xF7, 0xB9, 0x2C]
for i in range(len(c)):
    c[i] = c[i] ^ 0x17

print("".join([chr(x) for x in c]))

# CloseHandle
# ConnectNamedPipe
# CreateNamedPipeA
# CreateThread
# DisconnectNamedPipe
# FlushFileBuffers
# GetLastError
# GetProcessHeap
# lstrcmpA
# ReadFile
# WriteFile
# \\.\pipe\FlareOn
# Authorization Failed