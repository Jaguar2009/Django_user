from Django_user_git.django_project import Role, User


def create_user(name, email, role_id):
    try:
        role = Role.objects.get(id=role_id)
        user = User(name=name, email=email, role=role)
        user.save()
        print(f"Користувача {name} успішно створено.")
    except Role.DoesNotExist:
        print(f"Роль з id {role_id} не існує.")
    except Exception as e:
        print(f"Помилка при створенні користувача: {e}")


def show_users_by_role(role_id):
    try:
        role = Role.objects.get(id=role_id)
        users = User.objects.filter(role=role)
        for user in users:
            print(f"Ім'я: {user.name}, Email: {user.email}, Роль: {user.role.name}")
    except Role.DoesNotExist:
        print(f"Роль з id {role_id} не існує.")
    except Exception as e:
        print(f"Помилка при отриманні користувачів: {e}")


def main():

    Role.objects.get_or_create(name="user")
    Role.objects.get_or_create(name="admin")

    while True:
        print("\nМеню:")
        print("1. Створити користувача")
        print("2. Показати користувачів за роллю")
        print("0. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            name = input("Введіть ім'я користувача: ")
            email = input("Введіть email користувача: ")
            role_id = int(input("Введіть id ролі (1 для користувача, 2 для адміністратора): "))
            create_user(name, email, role_id)
        elif choice == '2':
            role_id = int(input("Введіть id ролі для перегляду користувачів: "))
            show_users_by_role(role_id)
        elif choice == '0':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()