def login(username, password):
    correct_username = "admin"
    correct_password = "1234"

    try:
        assert username == correct_username and password == correct_password, "Невірне ім'я користувача або пароль"
        print("Вхід виконано успішно")
    except AssertionError as e:
        print(e)

user_input = input("Введіть ім'я користувача: ")
pass_input = input("Введіть пароль: ")

login(user_input, pass_input)
