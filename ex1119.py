# Validar un email
import re
import email.utils

def is_valid_email(text):
    valid_pattern = r'^[\w-]+@[\w\.-]+\.[\w-]{1, 3}'
    return re.search(valid_pattern, text)

if __name__ == '__main__':
    n = int(input())
    in_data = [input().split() for _ in range(n)]

    for e in in_data:
        result = email.utils.parseaddr(e)
        if is_valid_email(result[1]):
            print(email.utils.formataddr(result))