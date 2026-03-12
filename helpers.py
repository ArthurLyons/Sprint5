import random
import string
from config import MIN_PASSWORD_LENGTH

def generate_unique_email(name="test", surname="testov", cohort=1999):
    """Генерирует уникальный email по шаблону."""
    random_digits = ''.join(random.choices(string.digits, k=3))
    return f"{name}_{surname}_{cohort}_{random_digits}@yandex.ru"

def generate_password(length=None):
    """
    Генерирует случайный пароль заданной длины.
    Если длина не указана, использует MIN_PASSWORD_LENGTH из config.
    """
    if length is None:
        length = MIN_PASSWORD_LENGTH
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def get_test_user_credentials():
    """Возвращает словарь с учётными данными тестового пользователя."""
    return {
        "email": generate_unique_email(),
        "password": generate_password()
    }

def get_weak_password():
    """Возвращает пароль короче минимальной длины (для тестов ошибок)."""
    return generate_password(MIN_PASSWORD_LENGTH - 1)

def create_existing_user_credentials(email, password):
    """
    Создаёт учётные данные существующего пользователя.

    Args:
        email (str): email пользователя
        password (str): пароль пользователя

    Returns:
        dict: словарь с ключами "email" и "password"
    """
    return {
        "email": email,
        "password": password
    }

def get_empty_credentials():
    """Возвращает учётные данные с пустыми полями для тестов валидации."""
    return {
        "email": "",
        "password": ""
    }

def get_invalid_email_credentials():
    """Возвращает учётные данные с некорректным email."""
    return {
        "email": "invalid-email",
        "password": generate_password()
    }
