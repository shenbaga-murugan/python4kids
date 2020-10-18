import tkinter
from phone_book import PhoneBook
root = tkinter.Tk()
pbk = PhoneBook()
pbk.load_file()
contacts = pbk.phone_book
row_ind = 0
for name in contacts:
	tkinter.Label(root, text = name, borderwidth = 1 ).grid(row = row_ind, column = 0)
	tkinter.Label(root, text = contacts[name], borderwidth = 1 ).grid(row = row_ind, column = 1)
	row_ind += 1
root.mainloop()
