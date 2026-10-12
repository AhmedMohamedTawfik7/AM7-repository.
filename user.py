class User:
    """Base account shared by customers and administrators."""

    def __init__(self, user_id, name, email):
        if not isinstance(user_id, int) or user_id < 0:
            raise ValueError("User ID must be a non-negative integer.")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name is required.")

        if not isinstance(email, str) or "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Email must be a valid address.")

        self.id = user_id
        self.name = name.strip()
        self.email = email.strip()

    def show_details(self):
        return f"ID: {self.id}, Name: {self.name}, Email: {self.email}"

    def show_role(self):
        return "User"

    def __str__(self):
        return self.show_details()
