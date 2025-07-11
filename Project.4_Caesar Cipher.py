#----Caesar Cipher---
# suppose you send "HI" msg (PLANE TEXT) it can encrypted and converted to *CIPHER TEXT
# when the receiver receives the msg *CIPHER TEXT converts into *PLANE TEXT
# shift--(2)
#     A B C D E F-------     THIS IS HOW TEXTS ARE ENCRIPTED
#     C D E F G H-------  ex-ABCD
# formula dor encrypted== new index=(index of A + shift number) %26
# decrypted==new index=(index of A -shift number) %26  (if index - shift is negative then (index of A -shift
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s',
           't','u','v','w','x','y','z']
def encrypt(plane_text,letters,shift_num):
    cipher_text = ""
    for char in plane_text:
        if char in letters:
            index = letters.index(char)
            new_index = (index+shift_num)%26
            cipher_text += letters[new_index]
        else:
            cipher_text += char
    print(f"Your Encrypted cipher_text is-:\"{cipher_text}\"")
def decrypt(plane_text,letters,shift_num):
    cipher_text = ""
    for char in plane_text:
        if char in letters:
            index = letters.index(char)
            if index-shift_num <0:
                new_index = ((index-shift_num)+26)%26
            else:
                new_index = ((index-shift_num)+26)%26
            cipher_text += letters[new_index]
        else:
            cipher_text += char
    print(f"Your Decrypted cipher_text is-:\"{cipher_text}\"")
game=True
while game is True:
    choice = input("Type 'encrypt' for encryption or 'decrypt' for decryption: \n")
    plane_text = input("Type Your Message: \n")
    shift_num = int(input("Enter shift number: \n"))
    if choice == 'encrypt':
        encrypt(plane_text, letters, shift_num)
    elif choice == 'decrypt':
        decrypt(plane_text, letters, shift_num)
    else:
        print("Invalid choice")
    x = input("Do you want to continue? YES/NO: \n").lower()
    if x == "yes":
        game = True
    else:
        game = False
        print("Thank you for playing,GOOD BYE")

