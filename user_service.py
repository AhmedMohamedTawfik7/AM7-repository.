class UserService:
    """Store and query users in a single in-memory list."""

    def __init__(self):
        self.users = []

    def add_user(self, user):
        if user is None:
            raise ValueError("User cannot be None.")
        if self.find_by_id(user.id) is not None:
            raise ValueError(f"User with ID {user.id} already exists.")
        self.users.append(user)

    def list_users(self):
        return list(self.users)

    def find_by_id(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def show_all_users(self):
        for user in self.users:
            print(user.show_details())

    def show_roles(self):
        for user in self.users:
            print(f"{user.name}: {user.show_role()}")
