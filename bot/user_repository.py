class UserRepository:
    """Репозиторий для работы с пользователями"""

    def __init__(self):
        self.users = {}

    def get_user(self, user_id):
        return self.users.get(user_id)

    def save_user(self, user_id, data):
        self.users[user_id] = data

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
