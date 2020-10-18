from phone_book import PhoneBook
class PbkConsoleFrontend:
	"""Console frontend for Phone Book Application"""
	
	pbk = PhoneBook()
	menu_handlers = {}
	
	def __init__(self):
		self.menu_handlers = {
			"1": self.handle_add,
			"2": self.handle_lookup,
			"3": self.handle_remove,
			"4": self.handle_list,
			"5": self.handle_reverse_lookup,
			"6": self.handle_load_file,
			"7": self.handle_save_file,
			"8": self.handle_save_as_file
		}	
		
	def print_menu(self):
		print("1. Add a new entry\t\t2. Lookup for an entry")
		print("3. Delete an entry\t\t4. List all entries")
		print("5. Reverse look up\t\t6. Load from file")
		print("7. Save file\t\t\t8. Save file as")
		print("**Press any other key to exit**")
		menu_opt = input("Enter your choice:")
		self.handle_menu(menu_opt)
		
	def handle_menu(self, menu_opt):
		if menu_opt in self.menu_handlers.keys():
			self.menu_handlers[menu_opt]() 
		else:
			self.menu_handlers["7"]()
			print("Exiting!")
			return
		self.print_menu()
		
	def handle_add(self):
		name = input("Enter name to add:")
		phone_no = input("Enter phone number to add:")
		if name in self.pbk.phone_book.keys():
			print(name, "already exists! Updating...")
			self.pbk.add_entry(name, phone_no)
		else:
			print("Saved new entry", name, ":", phone_no)
			self.pbk.add_entry(name, phone_no)
			print("Phone book contains", len(self.pbk.phone_book), "entries")
		
	def handle_lookup(self):
		name = input("Enter name to look up:")
		print(self.pbk.get_entry(name))
		
	def handle_remove(self):
		name = input("Enter name to be removed:")
		if name in self.pbk.phone_book.keys():
			self.pbk.del_entry(name)
			print(name, "has been removed from the phone book")
			print("Phone book contains", len(self.pbk.phone_book), "entries")
		else:
			print("No entry for given name", name)
		
	def handle_list(self):
		if len(self.pbk.phone_book) == 0:
			print("Phone book is empty!")
		else:
			print(self.pbk.list_entries())
	
	def handle_reverse_lookup(self):
		phone_no = input("Enter phone number to look up:")
		print(self.pbk.reverse_lookup(phone_no))
		
	def handle_load_file(self):
		self.pbk.file_name = input("Enter file to load:")
		print("Loading from", self.pbk.file_name)
		self.pbk.load_file()
		
	def handle_save_file(self):
		print("Writing to", self.pbk.file_name)
		self.pbk.save_file()
		
	def handle_save_as_file(self):
		self.pbk.file_name = input("Enter file to save:")
		print("Writing to", self.pbk.file_name)
		self.pbk.save_file()
		
	def greet(self):
		print("Welcome to Phone Book!")
		
c_frontend = PbkConsoleFrontend()
c_frontend.greet()
c_frontend.pbk.load_file()
c_frontend.print_menu()
