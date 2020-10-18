import os
class PhoneBook:

	"""A simple class for maintaing a Phone Book"""

	file_name = "contacts.pbk"
	phone_book = {}
	
	def load_file(self):
		if not os.path.isfile(self.file_name):
			with open(self.file_name, 'w') as pbk_file:
				print(self.phone_book, file = pbk_file)
		with open(self.file_name, 'r') as pbk_file:
			self.phone_book = eval(pbk_file.read())

	def save_file(self):
		with open(self.file_name, 'w') as pbk_file:
			print(self.phone_book, file = pbk_file)

	def add_entry(self, name, phone_no):
		self.phone_book[name] = phone_no	

	def get_entry(self, name):
		if name in self.phone_book.keys():
			return self.phone_book[name]
		else:
			return "No entry for given name " + name
			
	def del_entry(self, name):
		self.phone_book.pop(name)

	def list_entries(self):
		contact_list = "There are " + str(len(self.phone_book)) + " contacts"
		for name in self.phone_book:
			contact_list += "\n" + name + ": " + self.get_entry(name)
		return contact_list
				
	def reverse_lookup(self, phone_no):
		for name, phn_no in self.phone_book.items():
			if phone_no == phn_no:
				return name + ": " + self.get_entry(name)
		return "No entry for given number " + phone_no
