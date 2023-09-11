from pwn import *

for i in range(100):
    p = process("./ok")
    p.recvuntil(b"++++++++++++++++++++")
    p.recvuntil(b"Secret Please:")
    p.recvuntil(b"++++++++++++++++++++")
    p.send(str(i))
    p.interactive()    
