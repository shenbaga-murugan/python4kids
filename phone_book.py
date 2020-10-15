import os

def greet():
	print("Welcome to Phone Book!")

def load_file(file_name, phn_bk):
	if file_name == '':
		file_name = 'contacts.pbk'
	print("Loading from", file_name)
	if not os.path.isfile(file_name):
		with open(file_name, 'w') as pbk_file:
			print(phn_bk, file = pbk_file)
	with open(file_name, 'r') as pbk_file:
		phn_bk = eval(pbk_file.read())
	return phn_bk

def save_file(file_name):
	if file_name == '':
		file_name = 'contacts.pbk'
	with open(file_name, 'w') as pbk_file:
		print(phone_book, file = pbk_file)
		print("Writing to", file_name)

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
			
def reverse_lookup(phone_no):
	for name, phn_no in phone_book.items():
		if phone_no == phn_no:
			print_entry(name)
			return
	print("No entry for given number", phone_no)
		
def print_menu():
	print("1. Add a new entry\t\t4. List all entries")
	print("2. Lookup for an entry\t\t5. Reverse look up")
	print("3. Delete an entry\t\t6. Load from file")
	print("7. Save to file")
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
	elif (menu_opt == "5"):
		phone_no = input("Enter phone number to look up:")
		reverse_lookup(phone_no)
	elif (menu_opt == "6"):
		file_name = input("Enter file to load:")
		load_file(file_name)
	elif (menu_opt == "7"):
		file_name = input("Enter file to save:")
		save_file(file_name)
	else:
		save_file('')
		print("Exiting!")
		return
	print_menu()

phone_book = load_file('', {})
greet()
print_menu()
