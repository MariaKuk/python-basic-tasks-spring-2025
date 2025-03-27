def get_password_from_file():
    filename = "top_secret.txt"
    with open(filename, encoding="utf-8") as f:
        password = f.read().rstrip()

    return password


if __name__ == "__main__":
    # Заранее определённый пароль
    correct_password = get_password_from_file()

    # Запросить у пользователя ввод пароля
    user_input = input("Введите пароль: ")

    # Проверка введённого пароля
    if user_input == correct_password:
        print("Доступ разрешён")
    else:
        print("Доступ запрещён")
