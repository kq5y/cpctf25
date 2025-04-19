import hashlib
import random
import string


def random_string(length=8):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


target_prefix = "41633f"  # ログからキャッシュされたSHA256の先頭6文字がわかる
attempts = 0

while True:
    candidate = random_string(length=8)
    hash_value = hashlib.sha256(candidate.encode()).hexdigest()
    attempts += 1
    if hash_value.startswith(target_prefix):
        print(
            f"Found candidate: {candidate}, SHA256: {hash_value}, Attempts: {attempts}"
        )
        break
    if attempts % 100000 == 0:
        print(f"Trying... {attempts} attempts")
