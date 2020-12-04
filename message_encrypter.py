def encrypt_message(message, key):
	encrypted_message = ""
	for letter in message:
		new_asci = ((ord(letter) + int(key)) % 128)
		encrypted_message += chr((new_asci, new_asci + 32) [32 > new_asci])
	return encrypted_message
	
def decrypt_message(message, key):
	decrypted_message = ""
	for letter in message:
		new_key = (((int(key) % 128), ((int(key) % 128) - 32)) [int(key) > 32])
		new_asci = (ord(letter) - new_key)
		decrypted_message += chr((new_asci, new_asci + 96) [32 > new_asci])
	return decrypted_message

print("1. Encrypt Message\n2. Decrypt Message")
menu_opt = input("Enter your choice: ")
if(menu_opt == "1"):
	message = input("Enter your Message: ")
	key = input("Enter your key: ")
	print("Encrypted Message:", encrypt_message(message, key))
elif(menu_opt == "2"):
	message = input("Enter your Message: ")
	key = input("Enter your key: ")
	print("Decrypted Message:", decrypt_message(message, key))
else:
	print("Exiting!")
