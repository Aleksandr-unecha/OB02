class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._users_list = []

    def add_user(self, user):
        if isinstance(user, User):
            self._users_list.append(user)
            print(f"User {user.get_name()} added.")
        else:
            print("Error: Only instances of User can be added.")

    def remove_user(self, user_id):
        for user in self._users_list:
            if user.get_user_id() == user_id:
                self._users_list.remove(user)
                print(f"User {user.get_name()} removed.")
                return
        print("User not found.")

    def get_users_list(self):
        return [(user.get_user_id(), user.get_name(), user.get_access_level()) for user in self._users_list]


# Пример использования:
admin = Admin(1, "Pavel")

user1 = User(2, "Gosha")
user2 = User(3, "Stepa")

admin.add_user(user1)
admin.add_user(user2)

print(admin.get_users_list())

admin.remove_user(2)
print(admin.get_users_list())