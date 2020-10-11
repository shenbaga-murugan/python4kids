phone_book = {}

def add_entry(name, phone_no):
	if name in phone_book.keys():
		print(name, "already exists! Updating...")
		phone_book[name] = phone_no	
	else:
		phone_book[name] = phone_no
		print("Saved new entry", name, ":", phone_no)
		print("Phone book contains", len(phone_book), "entries")

def print_entry(name):
	if name in phone_book.keys():
		print(name, ":", phone_book[name])
	else:
		print("No entry for given name", name)
		
def del_entry(name):
	if name in phone_book.keys():
		phone_book.pop(name)
		print(name, "has been removed from the phone book")
		print("Phone book contains", len(phone_book), "entries")
	else:
		print("No entry for given name", name)

def list_entries():
	if len(phone_book) == 0:
		print("Phone book is empty!")
	else:
		for name in phone_book:
			print_entry(name)
		
def print_menu():
	print("1. Add a new entry")
	print("2. Lookup for an entry")
	print("3. Delete an entry")
	print("4. List all entries")
	print("**Press any other key to exit**")
	menu_opt = input("Enter your choice:")
	handle_menu(menu_opt)
	
def handle_menu(menu_opt):
	if (menu_opt == "1"):
		name = input("Enter name to add:")
		phone_no = input("Enter phone number to add:")
		add_entry(name, phone_no)
	elif (menu_opt == "2"):
		name = input("Enter name to look up:")
		print_entry(name)
	elif (menu_opt == "3"):
		name = input("Enter name to be removed:")
		del_entry(name)
	elif (menu_opt == "4"):
		list_entries()
	else:
		print("Exiting!")
		return
	print_menu()
	
print_menu()
