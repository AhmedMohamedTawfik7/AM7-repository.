from admin import Admin
from customer import Customer
from user_service import UserService


def main():
    user_service = UserService()
    user_service.add_user(Customer(1, "Customer1", "customer1@example.com", points=10))
    user_service.add_user(Customer(2, "Customer2", "customer2@example.com", points=20))
    user_service.add_user(Admin(3, "Admin1", "admin1@example.com"))

    print("All users:")
    user_service.show_all_users()

    search_id = 2
    print(f"\nSearch for user with ID {search_id}:")
    user = user_service.find_by_id(search_id)
    if user is None:
        print("User not found.")
    else:
        print(user.show_details())

    print("\nUser roles:")
    user_service.show_roles()


if __name__ == "__main__":
    main()
