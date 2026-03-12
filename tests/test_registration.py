import pytest
from selenium.webdriver.support import expected_conditions as EC
from config import MAIN_PAGE_URL, DEFAULT_NAME
from locators import *
from helpers import (
    get_test_user_credentials,
    get_weak_password,
    create_existing_user_credentials,
    get_empty_credentials,
    get_invalid_email_credentials
)

class TestRegistration:

    def test_successful_registration(self, driver, wait):
        """Проверка успешной регистрации с уникальными данными."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(REGISTER_LINK)).click()

        user_credentials = get_test_user_credentials()

        driver.find_element(*NAME_INPUT).send_keys(DEFAULT_NAME)
        driver.find_element(*EMAIL_INPUT).send_keys(user_credentials["email"])
        driver.find_element(*PASSWORD_INPUT).send_keys(user_credentials["password"])
        driver.find_element(*REGISTER_BUTTON).click()

        logout_btn = wait.until(EC.presence_of_element_located(LOGOUT_BUTTON))
        assert logout_btn.is_displayed(), "Кнопка выхода найдена, но не отображается после успешной регистрации"

    # ... остальные тесты регистрации (invalid_password_error, existing_user_error и т. д.) ...

class TestNavigation:

    def test_personal_cabinet_transition(self, driver, wait, logged_in_user):
        """Проверь переход по клику на «Личный кабинет»."""
        driver.get(MAIN_PAGE_URL)
        personal_cabinet_link = wait.until(
            EC.element_to_be_clickable(PERSONAL_CABINET_LINK)
        )
        personal_cabinet_link.click()

        # Проверяем, что попали в личный кабинет (появилось поле email)
        email_field = wait.until(
            EC.presence_of_element_located(EMAIL_INPUT)
        )
        assert email_field.is_displayed(), "Поле email не отображается в личном кабинете"

    def test_constructor_transition_from_cabinet(self, driver, wait, logged_in_user):
        """Проверь переход из личного кабинета в конструктор по клику на «Конструктор»."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(PERSONAL_CABINET_LINK)).click()

        constructor_link = wait.until(
            EC.element_to_be_clickable(CONSTRUCTOR_LINK)
        )
        constructor_link.click()

        # Проверяем, что видим заголовок раздела «Конструктор»
        constructor_title = wait.until(
            EC.presence_of_element_located(CONSTRUCTOR_TITLE)
        )
        assert constructor_title.is_displayed(), "Заголовок «Конструктор» не отображается"

    def test_logo_transition_to_constructor(self, driver, wait, logged_in_user):
        """Проверь переход в конструктор по клику на логотип Stellar Burgers."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(PERSONAL_CABINET_LINK)).click()

        logo = wait.until(
            EC.element_to_be_clickable(LOGO_LINK)
        )
        logo.click()

        # Проверяем переход в конструктор
        constructor_title = wait.until(
            EC.presence_of_element_located(CONSTRUCTOR_TITLE)
        )
        assert constructor_title.is_displayed(), "Не произошёл переход в конструктор по клику на логотип"

    def test_logout_from_account(self, driver, wait, logged_in_user):
        """Проверь выход из аккаунта по кнопке «Выйти» в личном кабинете."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(PERSONAL_CABINET_LINK)).click()

        logout_button = wait.until(
            EC.element_to_be_clickable(LOGOUT_BUTTON)
        )
        logout_button.click()

        # После выхода должна появиться кнопка «Войти в аккаунт»
        login_button = wait.until(
            EC.presence_of_element_located(LOGIN_BUTTON_MAIN)
        )
        assert login_button.is_displayed(), "Кнопка «Войти в аккаунт» не отображается после выхода"

    def test_navigation_to_buns_section(self, driver, wait, logged_in_user):
        """Проверь переход к разделу «Булки»."""
        driver.get(MAIN_PAGE_URL)

        buns_section = wait.until(
            EC.element_to_be_clickable(BUNS_SECTION)
        )
        buns_section.click()

        active_section = driver.find_element(*ACTIVE_SECTION_INDICATOR)
        assert "Булки" in active_section.text, "Раздел «Булки» не стал активным"

    def test_navigation_to_sauces_section(self, driver, wait, logged_in_user):
        """Проверь переход к разделу «Соусы»."""
        driver.get(MAIN_PAGE_URL)

        sauces_section = wait.until(
            EC.element_to_be_clickable(SAUCES_SECTION)
        )
        sauces_section.click()

        active_section = driver.find_element(*ACTIVE_SECTION_INDICATOR)
        assert "Соусы" in active_section.text, "Раздел «Соусы» не стал активным"

    def test_navigation_to_fillings_section(self, driver, wait, logged_in_user):
        """Проверь переход к разделу «Начинки»."""
        driver.get(MAIN_PAGE_URL)

        fillings_section = wait.until(
            EC.element_to_be_clickable(FILLINGS_SECTION)
        )
        fillings_section.click()

        active_section = driver.find_element(*ACTIVE_SECTION_INDICATOR)
        assert "Начинки" in active_section.text, "Раздел «Начинки» не стал активным"
