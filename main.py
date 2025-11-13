from library_books import library_books
from datetime import datetime, timedelta
# NOTE This is code completes the first 3 levels and ChatGPT was used to check if the code was done correctly after completetion and testing to double check.

# Level 1 
# TODO: Create a function to view all books that are currently available
# Should include book ID, title, and author
def view_available_books():
    for i in range(len(library_books)): # goes through each library book
        if library_books[i]["available"] == True: # Check if selected book is available
            print(f"{library_books[i]['id']}, {library_books[i]['title']}, {library_books[i]['author']}") # Prints the book's ID, title, and author

# Level 2 
# TODO: Create a function to search books by author OR genre
# Return a list of matching books
def search_books():
    user_search = input("Search book by author or genre: ") # Used so user can search for a specific book
    user_search = user_search.lower() # Turns any uppercase lettes into lowercase
    print("Search Results:") # Prints this right before the program searches for book
    for i in range(len(library_books)): # Checks through each library book for a match
        if (library_books[i]["author"].lower() == user_search) or (library_books[i]["genre"].lower() == user_search): 
            # If either the author or genre matches the user's search, print the book's ID, title, and author.
            print(f"{library_books[i]['id']}, {library_books[i]['title']}, {library_books[i]['author']}")

# Level 3 
# TODO: Create a function to checkout a book by its ID
# If the book is available:
# - Mark it unavailable
# - Set due date to 2 weeks from today
# - Increment the checkouts counter
# If it’s not available, show message that it’s already checked out and will be available in 2 weeks
def checkout_book():
    user_checkout = input("What book do you want to check out?") # used so the user can type in the ID of the book they want to check out
    for i in range(len(library_books)): # used to go through each Library book to find the book with the ID the user input
        if library_books[i]["id"] == user_checkout: # When this is true, input a variable named book_to_check_out is equal to the book the user checked out, including all of it's properties
            book_to_check_out = library_books[i]
            if book_to_check_out["available"] == True:
                book_to_check_out["available"] = False # Book's status becomes unavilable
                book_to_check_out["due_date"] = datetime.today() + timedelta(weeks = 2) # sets the due date of the book two weeks from the current day
                book_to_check_out["checkouts"] += 1 # The book checkouts is added
                print(f"Book '{book_to_check_out['title']}' by {book_to_check_out['author']} has been checked out!") # Used so the user knows if the checkout was successful
            else:
                print(f"Book '{book_to_check_out['title']}' by {book_to_check_out['author']} has already been checked out.") # Used to tell the user if the book was already checked out
# Call the functions to test them
view_available_books()
search_books()
checkout_book()
