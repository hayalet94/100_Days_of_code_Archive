
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type '1' to encrypt, type '2' to decrypt:").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def caesar(original_text, shift_amount, choice):
    
    orig_indexlist = []
    orig_word = ""

    if choice == 1:
        val1 = 1
    elif choice == 2:
        val1 = -1

    for letter in original_text:
        orig_indexlist.append(alphabet.index(letter))
        orig_word += letter
    print(orig_indexlist, orig_word)

    shifted_indices = []
    for index in orig_indexlist:
        new_index = (index + shift_amount * val1) % len(alphabet)
        shifted_indices.append(new_index)

    encrypted_text = ""
    for i in shifted_indices:
        encrypted_text += alphabet[i]
    
    print(shifted_indices, encrypted_text)


   
caesar(text, shift, direction)
#encrypt(text, shift)

# def decrypt(encrypted_text, shift_amount):

#     encrypted_list = []
#     encrypted_word = ""

#     for letter in encrypted_text:
#         encrypted_list.append(alphabet.index(letter))
#         encrypted_word += letter
#     print(encrypted_list, encrypted_word)

#     reshift_index = []
#     for index in encrypted_list:
#         new_index = (index - shift_amount) 
#         new_index % len(alphabet)
#         reshift_index.append(new_index)
    
#     decrypted_text = ""
#     for i in reshift_index:
#         decrypted_text += alphabet[i]
    
#     print(reshift_index, decrypted_text)

# encrypt()
# decrypt()

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.


# def encrypt_anyu(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")


# encrypt_anyu(original_text=text, shift_amount=shift)

# def decrypt_anyu(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")


# decrypt_anyu(original_text=text, shift_amount=shift)
