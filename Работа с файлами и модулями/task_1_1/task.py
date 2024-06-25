if __name__ == '__main__':
    # Заранее определённый пароль
    correct_password = "SecurePass123"

    # Запросить у пользователя ввод пароля
    user_input = input("Введите пароль: ")

    # Проверка введённого пароля
    if user_input == correct_password:
        print("Доступ разрешён")
    else:
        print("Доступ запрещён")
