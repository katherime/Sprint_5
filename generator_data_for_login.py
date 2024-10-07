import string
import random


def generate_password(length=6):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_login():
    first_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    last_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    numbers = random.randint(10, 99)
    three_numbers = random.randint(100, 999)
    email = f"{first_name}_{last_name}_{numbers}_{three_numbers}@yandex.ru"
    return email
