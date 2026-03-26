from getpass import getpass

print("Welcome to Hangmangame!")

#hide type in
word = getpass("Whats your word? (hidden) ")

letter_dict = []

dict_posi = 1

#for each letter create a dict that holds both the letter of the word and a underscore
for letter in word:
    letter_dict.append(dict(position = dict_posi, letter = letter, hidden = "_"))
    dict_posi += 1;

#our word length is the position value of the last indexed list element
word_length = letter_dict[-1]["position"]

print(f"The word is {word_length} letters long.")

#we create a empty string called hidden_list and loop through each "hidden"-letter in our letter_dict to show hidden characters
def hangman_status():
    hidden_list = ""

    for letter in letter_dict:
        hidden_list += letter["hidden"] + " "
    
    

    return hidden_list;

#we print our hangman status to see how many letters we have to uncover
print(hangman_status())

tries_left = 8
tries = 0
tries_letters = []

#we capture the typed in letters of our tries in our tries_letters list
#while we are under 8 tries we execute this code: 

while tries < 8:

    user_try = input("What letter do you want to try? - ")
    
    #user can only enter 1 character otherwise code doesnt execute

    if len(user_try) <= 1:

        # if user already tried the typed in letter before and it is stored in tries_letters, we prompt him to try again

        if user_try in tries_letters:
            print("Letter used before, try again!")
        
        # if user enters a new char we check if the letter is in our word

        while user_try not in tries_letters:

            tries_letters += user_try
            
            #we reset the hits variable
            hits = 0

            #we loop through each character in our letter_dict, if the user_try is within the letter value of one of our dicts within our list, we rise hits to 1
            for count in letter_dict:
                if user_try == count["letter"]:
                    count["hidden"] = count["letter"]
                    hits += 1
                
            #if there are no hits, the mistakes counter goes up, otherwise user keeps his tries
            if hits == 0:
                tries += 1
            
            #format

            print("_"*40)
            #message about how many tries are left and what letters have been tried already
            print(f"Mistakes: {tries}/{tries_left} - Letters tried: {tries_letters}")
        
        #If we dont have any underscores anymore we resolve the word and end the game

        if "_" not in hangman_status():
            print("")
            print("_"*40)
            print("")
            print("The word is: " + hangman_status() + "!")
            print("_"*40)
            print("")
            print("GAME OVER!")
            print("")
            break
        else:
            print(hangman_status())
        



    else:
        print("Please only put in 1 Letter!")


#if user has 8 mistakes we end the game
if tries == 8:
    print("GAME OVER!")

    