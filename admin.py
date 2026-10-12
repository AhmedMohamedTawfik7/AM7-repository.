from user import User


class Admin(User):
    """An administrator account."""

    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)

    def show_role(self):
        return "Admin"
