import re

visited = set()
files = ["69b46e1b-840f-415e-9402-2126dc9961e4.txt"]

while files:
    file = files.pop()
    if file in visited:
        continue
    visited.add(file)
    try:
        with open(file, "r") as f:
            text = f.read()
            if "CPCTF{" in text:
                flag = re.search(r"CPCTF{.*}", text)
                print(f"Flag found in {file}: {flag.group()}")
                break
            new_files = re.findall(
                r"([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\.txt)",
                text,
            )
            files.extend(new_files)
    except FileNotFoundError:
        print(f"File not found: {file}")
        continue
    print(f"Checked {file}, found {len(new_files)}")
