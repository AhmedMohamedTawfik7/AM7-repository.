from user import User


class Customer(User):
    """A customer account with a points balance."""

    def __init__(self, user_id, name, email, points=0):
        super().__init__(user_id, name, email)
        if not isinstance(points, int) or points < 0:
            raise ValueError("Points must be a non-negative integer.")
        self.points = points

    def show_role(self):
        return f"Customer (points: {self.points})"

    def show_details(self):
        return super().show_details() + f", Points: {self.points}"
