from selenium.webdriver.common.by import By

# === ЛОКАТОРЫ ДЛЯ ГЛАВНОЙ СТРАНИЦЫ ===
MAIN_PAGE_URL = "https://stellar-burgers.test.praktikum-services.ru"  


LOGIN_BUTTON_MAIN = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
PERSONAL_CABINET_LINK = (By.XPATH, "//a[contains(text(), 'Личный кабинет')]")
REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
LOGIN_LINK_IN_FORM = (By.XPATH, "//a[contains(text(), 'Войти')]")  # ссылка «Войти» в форме регистрации

# === ЛОКАТОРЫ ФОРМЫ ВХОДА ===
EMAIL_INPUT = (By.NAME, "email")  # поле ввода email
PASSWORD_INPUT = (By.NAME, "password")  # поле ввода пароля
LOGIN_FORM_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")  # кнопка «Войти» в форме


# === ЛОКАТОРЫ ПОСЛЕ УСПЕШНОГО ВХОДА ===
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")  # кнопка выхода из аккаунта

# === ЛОКАТОРЫ ФОРМЫ РЕГИСТРАЦИИ ===
NAME_INPUT = (By.NAME, "name")  # поле ввода имени
REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")  # кнопка регистрации


# === ЛОКАТОРЫ СООБЩЕНИЙ ОБ ОШИБКАХ ===
ERROR_MESSAGE_INVALID_CREDENTIALS = (By.XPATH,
    "//div[contains(text(), 'Неверные данные') or contains(text(), 'Некорректные данные') or contains(text(), 'Пользователь не найден')]")
ERROR_MESSAGE_EMPTY_FIELDS = (By.XPATH,
    "//div[contains(text(), 'Поля обязательны для заполнения') or contains(text(), 'Заполните все поля')]")
ERROR_MESSAGE_INVALID_EMAIL = (By.XPATH,
    "//div[contains(text(), 'Некорректный формат email') or contains(text(), 'Введите корректный email') or contains(text(), 'Email некорректен')]")
ERROR_MESSAGE_INVALID_PASSWORD = (By.XPATH,
    "//div[contains(text(), 'Некорректный пароль') or contains(text(), 'Пароль некорректен') or contains(text(), 'Слишком короткий пароль')]")
ERROR_MESSAGE_EXISTING_USER = (By.XPATH,
    "//div[contains(text(), 'Пользователь с таким email уже существует') or contains(text(), 'Такой пользователь уже зарегистрирован')]")

# === ЛОКАТОРЫ НАВИГАЦИИ И КОНСТРУКТОРА ===
CONSTRUCTOR_LINK = (By.XPATH, "//a[contains(text(), 'Конструктор')]")  # ссылка «Конструктор»
LOGO_LINK = (By.CLASS_NAME, "AppHeader_header__logo__2D9j1")  # логотип Stellar Burgers
CONSTRUCTOR_TITLE = (By.XPATH, "//h1[contains(text(), 'Собери бургер')]")  # заголовок конструктора

# Разделы конструктора
BUNS_SECTION = (By.XPATH, "//div[contains(text(), 'Булки')]")  # раздел «Булки»
SAUCES_SECTION = (By.XPATH, "//div[contains(text(), 'Соусы')]")  # раздел «Соусы»
FILLINGS_SECTION = (By.XPATH, "//div[contains(text(), 'Начинки')]")  # раздел «Начинки»
ACTIVE_SECTION_INDICATOR = (By.CSS_SELECTOR, ".tab_tab_active__2tTWO")  # индикатор активного раздела

# === ДОПОЛНИТЕЛЬНЫЕ ЛОКАТОРЫ ===
ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")  # кнопка оформления заказа
INGREDIENT_CARD = (By.CLASS_NAME, "constructor-element")  # карточка ингредиента в конструкторе
INGREDIENTS_LIST = (By.CLASS_NAME, "ingredients")  # список ингредиентов

# === ЛОКАТОРЫ ЛИЧНОГО КАБИНЕТА ===
PROFILE_LINK = (By.XPATH, "//a[contains(text(), 'Профиль')]")  # ссылка на профиль
HISTORY_ORDERS_LINK = (By.XPATH, "//a[contains(text(), 'История заказов')]")  # история заказов


# === УНИВЕРСАЛЬНЫЕ ЛОКАТОРЫ ===
ERROR_MESSAGE = (By.CLASS_NAME, "input__error")  # универсальный локатор для любых сообщений об ошибках
SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")  # сообщение об успехе
LOADER = (By.CLASS_NAME, "loader")  # индикатор загрузки
