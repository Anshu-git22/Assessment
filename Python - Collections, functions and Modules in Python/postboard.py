from datetime import datetime

# -----------------------------
# PostBoard - Python Assessment
# -----------------------------
# Temporary in-memory data only
users = [
    {"username": "admin", "password": "admin123"},
    {"username": "anshu", "password": "12345"}
]

posts = []


def get_non_empty_input(message):
    """Take input from user and do not allow blank value."""
    while True:
        value = input(message).strip()
        if value == "":
            print("This field cannot be empty. Please enter a valid value.")
        else:
            return value


def register_user():
    """Register a new user with username and password."""
    print("\n--- User Registration ---")
    username = get_non_empty_input("Enter username: ").lower()

    for user in users:
        if user["username"] == username:
            print("Username already exists. Please try another username.")
            return

    password = get_non_empty_input("Enter password: ")
    users.append({"username": username, "password": password})
    print("Registration successful! You can login now.")


def login_user():
    """Login user with maximum 3 attempts."""
    print("\n--- User Login ---")
    attempts = 3

    while attempts > 0:
        username = get_non_empty_input("Enter username: ").lower()
        password = get_non_empty_input("Enter password: ")

        for user in users:
            if user["username"] == username and user["password"] == password:
                print(f"Login successful. Welcome, {username}!")
                return username

        attempts -= 1
        print(f"Invalid username or password. Attempts left: {attempts}")

    print("Too many failed login attempts.")
    return None


def create_post(current_user):
    """Create post and link it with logged-in user."""
    print("\n--- Create New Post ---")
    title = get_non_empty_input("Enter post title: ")
    description = get_non_empty_input("Enter post description: ")

    choice = input("Do you want to enter date manually? (y/n): ").strip().lower()
    if choice == "y":
        date = get_non_empty_input("Enter date (DD-MM-YYYY): ")
    else:
        date = datetime.now().strftime("%d-%m-%Y")

    post = {
        "author": current_user,
        "title": title,
        "description": description,
        "date": date
    }
    posts.append(post)
    print("Post created successfully!")


def view_all_posts():
    """Display all posts in clean format."""
    print("\n--- All Posts ---")

    if len(posts) == 0:
        print("No posts available yet.")
        return

    for index, post in enumerate(posts, start=1):
        print("\n" + "-" * 40)
        print(f"Post No.    : {index}")
        print(f"Author      : {post['author']}")
        print(f"Title       : {post['title']}")
        print(f"Date        : {post['date']}")
        print(f"Description : {post['description']}")
        print("-" * 40)


def search_posts_by_username():
    """Search and display posts by username."""
    print("\n--- Search Posts by Username ---")
    username = get_non_empty_input("Enter username to search: ").lower()

    found = False
    for post in posts:
        if post["author"] == username:
            if not found:
                print(f"\nPosts created by {username}:")
            found = True
            print("\n" + "-" * 40)
            print(f"Author      : {post['author']}")
            print(f"Title       : {post['title']}")
            print(f"Date        : {post['date']}")
            print(f"Description : {post['description']}")
            print("-" * 40)

    if not found:
        print("No posts found for this username.")


def user_menu(current_user):
    """Menu after successful login."""
    while True:
        print("\n========== PostBoard User Menu ==========")
        print("1. Create Post")
        print("2. View All Posts")
        print("3. Search Posts by Username")
        print("4. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_post(current_user)
        elif choice == "2":
            view_all_posts()
        elif choice == "3":
            search_posts_by_username()
        elif choice == "4":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please select 1 to 4.")


def main_menu():
    """Main menu of PostBoard application."""
    while True:
        print("\n========== Welcome to PostBoard ==========")
        print("1. Register")
        print("2. Login")
        print("3. View All Posts")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            logged_user = login_user()
            if logged_user is not None:
                user_menu(logged_user)
        elif choice == "3":
            view_all_posts()
        elif choice == "4":
            print("Thank you for using PostBoard. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 4.")


main_menu()
