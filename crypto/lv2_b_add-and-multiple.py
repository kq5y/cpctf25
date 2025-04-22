f = open("cipher.txt", "r")
cipher = int(f.read())
f.close()
start = 1000
while cipher % start != 0:
    start += 1
a = []
while cipher != 0:
    cipher //= start
    start -= 1
    c = 0
    for i in range(start):
        if (cipher - i) % start == 0:
            c = i
            break
    a.append(c)
plaintext = ""
print(a)
for i in a:
    plaintext = chr(i) + plaintext
print(plaintext)
