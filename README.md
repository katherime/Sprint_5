Проект автоматизации тестирования сервиса Stellar Burgers

**test_registration**
Тестирование регистрации на сервисе.

Успешная авторизация с валидными данными
- test_registration_success

Ошибка регистрации при некорректном пароле
- test_registration_with_wrong_password

**test_login**
Тестирование авторизации на сервисе.

Функция для авторизации в личном кабинете с валидными данными
- login_with_right_data 

Вход по кнопке «Войти в аккаунт» на главной странице
- test_login_to_account_by_button_enter_on_main - 

Вход через кнопку «Личный кабинет»
- test_login_to_account_by_button_personal_cabinet 

Вход через кнопку в форме регистрации
- test_login_to_account_by_form_of_registration 

Вход через кнопку в форме восстановления пароля
- test_login_to_account_by_form_of_recovery_password 


**test_personal_cabinet**
Тестирование перехода в личный кабинет на сервисе.

Авторизация и переход по клику на «Личный кабинет»
- test_entering_to_personal_cabinet

Выход из авторизированного аккаунта в личном кабинете
- test_exit_from_account

**test_transation_cabinet_constructor**
Тестирование перехода из личного кабинета в конструктор

Переход по клику в «Конструктор»
- test_transation_from_personal_cabinet_to_constructor

Переход по клику на логотип Stellar Burgers
- test_transation_from_personal_cabinet_to_logotype

**test_constructor**
Тестирование переходов по вкладкам на основной странице конструктора.

Доп. функция для проверки добавления слова "current" к активной вкладке
- check_transition

Переход к секции «Булки»
- test_transition_to_tab_about_bread

Переход к секции «Соусы»
- test_transition_to_tab_about_sauses

Переход к секции «Начинки»
- test_transition_to_tab_about_filling

**generator_data_login**
Функция для генерации валидных данных для регистрации.

Генерация валидного пароля с минимальной длиной 6 символов
- def_generate_password 

Генерация валидного адреса почты
- def_generate_login 