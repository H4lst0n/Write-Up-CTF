from pwn import *

# a-> z
# for i in range(96,123):
#     p = remote("chal.pctf.competitivecyber.club", 4757)
#     p.send("pctf{Tim3ingI8N3a" + chr(i) + "}")
#     print(chr(i))
#     p.interactive()

# # 0 -> 9    
# for i in range(96,123):
#     p = remote("chal.pctf.competitivecyber.club", 4757)
#     p.send("pctf{Tim3ingI8N3at" + chr(i) + "}")
#     print(chr(i))
#     p.interactive()

  
# # A -> Z      
# for i in range(96,123):
#     p = remote("chal.pctf.competitivecyber.club", 4757)
#     p.send("pctf{Tim3ingI8N3a" + chr(i) + "}")
#     print(chr(i))
#     p.interactive()

p = remote("chal.pctf.competitivecyber.club", 4757)
p.send("pctf{Tim3ingI8N3at"+ "}")
p.interactive()