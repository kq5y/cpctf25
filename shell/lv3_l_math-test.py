import socket
import re


def solve_equation(equation):
    # {num0} + {num1} = ?
    match = re.match(r"(\d+) \+ (\d+) = \?", equation)
    if match:
        num0 = int(match.group(1))
        num1 = int(match.group(2))
        return num0 + num1
    return None


def main():
    host = "mathtest.web.cpctf.space"
    port = 30010
    with socket.create_connection((host, port)) as sock:
        sock_file = sock.makefile(mode="rw")
        i = 0
        while True:
            i += 1
            line = sock_file.readline().strip()
            if not line:
                break

            print(f"({i})Received: {line}")

            result = solve_equation(line)
            if result is not None:
                sock_file.write(f"{result}\n")
                sock_file.flush()
                print(f"Sent: {result}")
            else:
                print(line)
                break


if __name__ == "__main__":
    main()
