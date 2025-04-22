with open("target.txt", "w") as f:
    for i in range(1, 16385):
        n = i
        s = ""
        while n > 0:
            n -= 1
            s = chr(n % 26 + ord("A")) + s
            n //= 26
        f.write(s + "\n")

import hashlib

with open("target.txt", "rb") as f:
    data = f.read()
    sha256_hash = hashlib.sha256(data).hexdigest()
    print(sha256_hash)
