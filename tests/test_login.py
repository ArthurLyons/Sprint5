import pytest
from selenium.webdriver.support import expected_conditions as EC
from config import MAIN_PAGE_URL
from locators import (
    LOGIN_BUTTON_MAIN,
    PERSONAL_CABINET_LINK,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    LOGIN_FORM_BUTTON,
    LOGOUT_BUTTON,
    ERROR_MESSAGE_INVALID_CREDENTIALS,
    ERROR_MESSAGE_EMPTY_FIELDS
)

class TestLogin:

    def test_login_via_main_button(self, driver, wait, registered_user):
        """Проверка входа по кнопке «Войти в аккаунт» на главной."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)).click()

        # Ввод данных
        driver.find_element(*EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LOGIN_FORM_BUTTON).click()

        # Проверка отображения кнопки выхода (поиск + проверка в одном assert)
        assert wait.until(
            EC.visibility_of_element_located(LOGOUT_BUTTON)
        ), "Кнопка выхода не отображается после успешного входа"

    def test_login_via_personal_cabinet(self, driver, wait, registered_user):
        """Проверка входа через кнопку «Личный кабинет»."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(PERSONAL_CABINET_LINK)).click()

        # Ввод данных
        driver.find_element(*EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LOGIN_FORM_BUTTON).click()

        # Проверка отображения кнопки выхода
        assert wait.until(
            EC.visibility_of_element_located(LOGOUT_BUTTON)
        ), "Кнопка выхода не отображается после входа через личный кабинет"

    def test_invalid_credentials_error(self, driver, wait):
        """Проверка сообщения об ошибке при некорректных данных для входа."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)).click()

        # Ввод некорректных данных
        driver.find_element(*EMAIL_INPUT).send_keys("invalid@example.com")
        driver.find_element(*PASSWORD_INPUT).send_keys("wrongpassword")
        driver.find_element(*LOGIN_FORM_BUTTON).click()

        # Проверка отображения сообщения об ошибке
        assert wait.until(
            EC.visibility_of_element_located(ERROR_MESSAGE_INVALID_CREDENTIALS)
        ), "Сообщение об ошибке не отображается при некорректных данных"

    def test_empty_fields_login_error(self, driver, wait):
        """Проверка сообщения об ошибке при пустых полях входа."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)).click()

        driver.find_element(*LOGIN_FORM_BUTTON).click()

        # Проверка отображения сообщения об ошибке для пустых полей
        assert wait.until(
            EC.visibility_of_element_located(ERROR_MESSAGE_EMPTY_FIELDS)
        ), "Сообщение о пустых полях не отображается"

    def test_login_with_empty_email(self, driver, wait):
        """Проверка ошибки при пустом email."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)).click()

        # Ввод пароля без email
        driver.find_element(*PASSWORD_INPUT).send_keys("validpassword")
        driver.find_element(*LOGIN_FORM_BUTTON).click()

        # Проверка отображения сообщения об ошибке
        assert wait.until(
            EC.visibility_of_element_located(ERROR_MESSAGE_EMPTY_FIELDS)
        ), "Сообщение о пустом email не отображается"

    def test_login_with_empty_password(self, driver, wait, registered_user):
        """Проверка ошибки при пустом пароле."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)).click()

        # Ввод email без пароля
        driver.find_element(*EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*LOGIN_FORM_BUTTON).click()


        # Проверка отображения сообщения об ошибке
        assert wait.until(
            EC.visibility_of_element_located(ERROR_MESSAGE_EMPTY_FIELDS)
        ), "Сообщение о пустом пароле не отображается"

    def test_redirect_after_login(self, driver, wait, registered_user):
        """Проверка редиректа на главную страницу после входа."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)).click()

        # Ввод данных и вход
        driver.find_element(*EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LOGIN_FORM_BUTTON).click()

        # Ожидание редиректа
        wait.until(lambda d: d.current_url != MAIN_PAGE_URL)
        assert MAIN_PAGE_URL in driver.current_url, "Редирект на главную страницу не произошёл"
