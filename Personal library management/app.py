# 📁 library_manager.py

# Step 1: Empty library list
library = []

# Step 2: Welcome message
print("📖 Welcome to Personal Library Manager")
print("Your digital book collection starts here!")

# Step 3: Menu loop
while True:
    print("\n=== MENU ===")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("\n📘 Add a Book")

        book = {
            'title': input("Title: "),
            'author': input("Author: "),
            'year': int(input("Publication Year: ")),
            'genre': input("Genre: "),
            'read': input("Read? (yes/no): ").lower().startswith("y")
        }

        library.append(book)
        print("✅ Book added!")

    elif choice == "2":
        print("\n❌ Remove a Book")
        title = input("Enter the title of the book to remove: ")
        removed = False
        for book in library:
            if book['title'].lower() == title.lower():
                library.remove(book)
                removed = True
                print("✅ Book removed.")
                break
        if not removed:
            print("⚠️ Book not found.")

    elif choice == "3":
        print("\n🔍 Search Book")
        keyword = input("Enter title or author to search: ").lower()
        found = False
        for book in library:
            if keyword in book['title'].lower() or keyword in book['author'].lower():
                print(f"📖 {book['title']} by {book['author']} ({book['year']}) | Genre: {book['genre']} | Read: {'Yes' if book['read'] else 'No'}")
                found = True
        if not found:
            print("⚠️ No matching books found.")

    elif choice == "4":
        print("\n📚 All Books in Library:")
        if not library:
            print("Library is empty.")
        else:
            for idx, book in enumerate(library, start=1):
                print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) | Genre: {book['genre']} | Read: {'Yes' if book['read'] else 'No'}")

    elif choice == "5":
        print("\n📊 Library Statistics")
        total = len(library)
        if total == 0:
            print("No books in the library yet.")
        else:
            read_books = sum(1 for book in library if book['read'])
            percent = (read_books / total) * 100
            print(f"📚 Total books: {total}")
            print(f"📖 Books read: {read_books} ({percent:.2f}%)")

    elif choice == "6":
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("⚠️ Invalid choice. Please enter a number between 1 and 6.")