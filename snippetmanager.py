import json
import clipboard

SNIPPETS_FILE = "snippets.json"

def load_snippets():
    try:
        with open(SNIPPETS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_snippets(snippets):
    with open(SNIPPETS_FILE, "w") as file:
        json.dump(snippets, file)

def add_snippet():
    snippets = load_snippets()

    name = input("Enter snippet name: ")
    category = input("Enter snippet category: ")
    code = input("Enter snippet code: ")

    if category not in snippets:
        snippets[category] = []

    snippets[category].append({"name": name, "code": code})
    save_snippets(snippets)

    print("Snippet added successfully!")

def search_snippets():
    snippets = load_snippets()

    keyword = input("Enter search keyword: ")

    found_snippets = []
    for category in snippets:
        for snippet in snippets[category]:
            if keyword.lower() in snippet["name"].lower() or keyword.lower() in snippet["code"].lower():
                found_snippets.append(snippet)

    if found_snippets:
        print("Matching snippets found:")
        for snippet in found_snippets:
            print(f"Name: {snippet['name']}")
            print(f"Category: {category}")
            print(f"Code: {snippet['code']}")
            print("-" * 20)
    else:
        print("No matching snippets found.")

def copy_snippet_code():
    snippets = load_snippets()

    category = input("Enter category of snippet: ")
    name = input("Enter name of snippet: ")

    if category in snippets:
        for snippet in snippets[category]:
            if snippet["name"].lower() == name.lower():
                clipboard.copy(snippet["code"])
                print("Snippet code copied to clipboard!")
                return

    print("Snippet not found.")


print("Welcome to Code Snippet Manager!")
while True:
    print("\nSelect an option:")
    print("1. Add Snippet")
    print("2. Search Snippets")
    print("3. Copy Snippet Code to Clipboard")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_snippet()
    elif choice == "2":
        search_snippets()
    elif choice == "3":
        copy_snippet_code()
    elif choice == "4":
        break
    else:
        print("Please Choose from the menu.")
