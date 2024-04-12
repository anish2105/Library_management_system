from book import create_book, update_book, delete_book_by_isbn, list_books, search_books
from user import create_user, update_user, delete_user_by_id, list_users
from check import check_availability, borrow_book, return_book
from store import save_data, load_data

def manage_books_menu(books):
    print("\nBook Management")
    print("1. Add Book")
    print("2. Update Book (by ISBN)")
    print("3. Delete Book (by ISBN)")
    print("4. List Books")
    print("5. Search Books")
    print("6. Back to Main Menu")
    choice = input("Enter choice: ")
    return choice

def manage_users_menu(users):
    print("\nUser Management")
    print("1. Add User")
    print("2. Update User (by ID)")
    print("3. Delete User (by ID)")
    print("4. List Users")
    print("5. Back to Main Menu")
    choice = input("Enter choice: ")
    return choice

def main_menu():
    print("\nLibrary Management System")
    print("1. Manage Books")
    print("2. Manage Users")
    print("3. Check book availability")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    # Load data at the beginning
    books, users = load_data()
    
    while True:
        choice = main_menu()
        if choice == '1':
            while True:
                choice = manage_books_menu(books)
                if choice == '1':
                    new_book = create_book(books)
                    books.append(new_book)
                    print("Book added successfully.")
                    save_data(books, users)
                elif choice == '2':
                    list_books(books)
                    isbn = input("Enter ISBN of the book to update: ")
                    update_book(books, isbn)
                    save_data(books, users)
                elif choice == '3':
                    if not books:
                        print("No books in library.")
                        continue
                    else:
                        list_books(books)
                        isbn = input("Enter ISBN of the book to delete: ")
                        delete_book_by_isbn(books, isbn)
                        save_data(books, users)
                elif choice == '4':
                    list_books(books)
                elif choice == '5':
                    if not books:
                        print("No books found to search.")
                        continue
                    search_term = input("Enter search term (title, author, or ISBN): ")
                    search_results = search_books(books, search_term)
                    if search_results:
                        print("Search results:")
                        for book in search_results:
                            print("---------------------------")
                            print(book)
                            print("---------------------------")
                    else:
                        print("No books found matching your search criteria.")
                elif choice == '6':
                    break  # Exit from Manage Books menu
                else:
                    print("Invalid choice, please try again.")
        elif choice == '2':
            while True:
                choice = manage_users_menu(users)
                if choice == '1':
                    new_user = create_user(users)
                    users.append(new_user)
                    print("User added successfully.")
                    save_data(books, users)
                elif choice == '2':
                    list_users(users)
                    user_id = input("Enter user ID to update: ")
                    update_user(users, user_id)
                    save_data(books, users)
                elif choice == '3':
                    if not users:
                        print("No users to delete.")
                        continue
                    else:  
                        list_users(users)
                        user_id = input("Enter user ID to delete: ")
                        delete_user_by_id(users, user_id)
                        save_data(books, users)
                elif choice == '4':
                    list_users(users)
                elif choice == '5':
                    break  
                else:
                    print("Invalid choice, please try again.")
        elif choice == '3':
            isbn = input("Enter the ISBN of the book to check availability: ")
            if check_availability(books, isbn):
                print("Book is available for borrowing.")
            else:
                borrowed_user = None
                for book in books:
                    if book.isbn == isbn and not book.available:
                        borrowed_user = [user.name for user in users if user.user_id == book.borrower_id]
                        if borrowed_user:
                            borrowed_user = borrowed_user[0]
                        break
                if borrowed_user:
                    print(f"Book is not available for borrowing. Currently borrowed by: {borrowed_user}")
                else:
                    print("Book is not available for borrowing.")
        elif choice == '4':
            isbn = input("Enter the ISBN of the book to borrow: ")
            user_id = input("Enter your user ID: ")
            user = [user for user in users if user.user_id == user_id]
            if user:
                if borrow_book(books, isbn, user_id, users):  # Pass users list
                    print("Book borrowed successfully.")
                else:
                    print("Failed to borrow the book.")
            else:
                print("User not found.")
        elif choice == '5':
            isbn = input("Enter the ISBN of the book to return: ")
            if return_book(books, isbn, users):
                print("Book returned successfully.")
            else:
                print("Failed to return the book.")
        elif choice == '6':
            print("Exiting.")
            # Save data before exiting
            save_data(books, users)
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
