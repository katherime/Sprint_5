from selenium.webdriver.common.by import By


class TestLocators:

    ### Страница регистрации/входа в аккаунт
    # Поле ввода имени
    NAME_INPUT_FIELD = By.XPATH, '//label[ text()="Имя" ]/parent::div/input'
    # Поле ввода email
    EMAIL_INPUT_FIELD = By.XPATH, '//label[ text()="Email" ]/parent::div/input'
    # Поле ввода пароля
    PASSWORD_INPUT_FIELD = By.XPATH, '//label[ text()="Пароль" ]/parent::div/input'
    # Кнопка регистрации
    BUTTON_REGISTRATION = By.XPATH, '//button[ text()="Зарегистрироваться"]'
    # Кнопка "Войти" в аккаунт
    BUTTON_ENTER = By.XPATH, '//button[ text()="Войти"]'
    # Заголовок "Вход" на странице ввода в аккаунт
    ENTER_AFTER_REGISTRATION = By.XPATH, '//h2[text()="Вход"]'
    # Заголовок с предупреждением о некорректном пароле
    WARNING_WRONG_PASSWORD = By.XPATH, '//p[text()="Некорректный пароль"]'


    ### Главная страница
    # Заголовок "Соберите бургер" на главной странице
    MAIN_H1_CONSTRUCTOR = By.XPATH, '//h1[text()="Соберите бургер"]'
    # Кнопка перехода в личный кабинет
    BUTTON_PERSONAL_CABINET = By.XPATH, '//p[text()="Личный Кабинет"]'
    # Кнопка перехода в аккаунт
    BUTTON_ENTER_TO_ACCOUNT = By.XPATH, '//button[text()=\'Войти в аккаунт\']'
    # Кнопка перехода к блоку "Булки"
    BUTTON_BREAD = By.XPATH, "//span[text()='Булки']"
    # Кнопка перехода к блоку "Соусы"
    BUTTON_SAUSES = By.XPATH, "//span[text()='Соусы']"
    # Кнопка перехода к блоку "Начинки"
    BUTTON_FILLING = By.XPATH, "//span[text()='Начинки']"
    # Кнопка оформления заказа бургера после входа в аккаунт
    BUTTON_MAKE_ORDER =  By.XPATH, "//button[contains(text(),'Оформить заказ')]"

    ### Страница личного кабинет
    # Кнопка "Выход" из аккаунта
    BUTTON_EXIT_FROM_ACCOUNT = By.XPATH, "//button[text()='Выход']"
    # Кнопка "Конструктор" из аккаунта
    BUTTON_CONSTRUCTOR = By.XPATH, "//p[contains(text(),'Конструктор')]"
    # Кликабельный логотип "Stellar Burgers"
    BUTTON_LOGOTYPE = By.CLASS_NAME, "AppHeader_header__logo__2D0X2"

    ### Форма регистрации
    BUTTON_LOGIN_TO_ACCOUNT = By.XPATH, "//a[text()='Войти']"
