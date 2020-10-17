import os
class PhoneBook:

	"""A simple class for maintaing a Phone Book"""

	file_name = "contacts.pbk"
	phone_book = {}
	
	def greet(self):
		print("Welcome to Phone Book!")

	def load_file(self, f_name):
		print("Loading from", f_name)
		if not os.path.isfile(f_name):
			with open(f_name, 'w') as pbk_file:
				print(self.phone_book, file = pbk_file)
		with open(f_name, 'r') as pbk_file:
			self.phone_book = eval(pbk_file.read())

	def save_file(self, f_name):
		with open(f_name, 'w') as pbk_file:
			print(self.phone_book, file = pbk_file)
			print("Writing to", f_name)

	def add_entry(self, name, phone_no):
		if name in self.phone_book.keys():
			print(name, "already exists! Updating...")
			self.phone_book[name] = phone_no	
		else:
			self.phone_book[name] = phone_no
			print("Saved new entry", name, ":", phone_no)
			print("Phone book contains", len(self.phone_book), "entries")

	def print_entry(self, name):
		if name in self.phone_book.keys():
			print(name, ":", self.phone_book[name])
		else:
			print("No entry for given name", name)
			
	def del_entry(self, name):
		if name in self.phone_book.keys():
			self.phone_book.pop(name)
			print(name, "has been removed from the phone book")
			print("Phone book contains", len(self.phone_book), "entries")
		else:
			print("No entry for given name", name)

	def list_entries(self):
		if len(self.phone_book) == 0:
			print("Phone book is empty!")
		else:
			for name in self.phone_book:
				self.print_entry(name)
				
	def reverse_lookup(self, phone_no):
		for name, phn_no in self.phone_book.items():
			if phone_no == phn_no:
				self.print_entry(name)
				return
		print("No entry for given number", phone_no)
			
	def print_menu(self):
		print("1. Add a new entry\t\t2. Lookup for an entry")
		print("3. Delete an entry\t\t4. List all entries")
		print("5. Reverse look up\t\t6. Load from file")
		print("7. Save to file")
		print("**Press any other key to exit**")
		menu_opt = input("Enter your choice:")
		self.handle_menu(menu_opt)
		
	def handle_menu(self, menu_opt):
		if (menu_opt == "1"):
			name = input("Enter name to add:")
			phone_no = input("Enter phone number to add:")
			self.add_entry(name, phone_no)
		elif (menu_opt == "2"):
			name = input("Enter name to look up:")
			self.print_entry(name)
		elif (menu_opt == "3"):
			name = input("Enter name to be removed:")
			self.del_entry(name)
		elif (menu_opt == "4"):
			self.list_entries()
		elif (menu_opt == "5"):
			phone_no = input("Enter phone number to look up:")
			self.reverse_lookup(phone_no)
		elif (menu_opt == "6"):
			self.file_name = input("Enter file to load:")
			self.load_file(self.file_name)
		elif (menu_opt == "7"):
			self.file_name = input("Enter file to save:")
			self.save_file(self.file_name)
		else:
			self.save_file(self.file_name)
			print("Exiting!")
			return
		self.print_menu()

phoneBook = PhoneBook()
phoneBook.greet()
phoneBook.load_file(phoneBook.file_name)
phoneBook.print_menu()
