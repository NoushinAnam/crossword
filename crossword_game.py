import hashlib 
'''Admin details(username, password): ijti, ahmed 
player details(username, password):   ijti  habil
                                      habil ijti'''

database=[['ijti', 'bfb7836516e12905f44ec6f30c7818a1e3a3ac72e96966ec38209d16787a2948' ,'9af2921d3fd57fe886c9022d1fcc055d53a79e4032fa6137e397583884e1a5de'], ['ijti', 'bfb7836516e12905f44ec6f30c7818a1e3a3ac72e96966ec38209d16787a2948', '250133b6bf89351c12454d0bd7b00afd7bcb9b682df8e65b3885e269451c2ee2', 5], ['habil', '250133b6bf89351c12454d0bd7b00afd7bcb9b682df8e65b3885e269451c2ee2', 'bfb7836516e12905f44ec6f30c7818a1e3a3ac72e96966ec38209d16787a2948', 5]]
player1 = None
player2 = None
player1_health = 0
player2_health = 0
p1_final_health=5
p2_final_health=5
p1_correct_guesses=0
p2_correct_guesses=0
p1_incorrect_guesses=0
p2_incorrect_guesses=0

grid= [['#', '#', '#', 'F', '#', '#', '#', '#', '#',],
        ['#', '#', '#', 'L', '#', '#', '#', '#', '#',],
        ['#', '#', '# ', 7 , '#', '#', '#', '#', '#',],
        ['#', '#', '#', 'T', '#', '#', 'B', 13, 'N',],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#',],
        ['#', '#', '#', '#', 9, 'I', 'M', '#', '#',],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#',],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#',],
        ['C', 2, 'D', 4, '#', '#', '#', '#', '#',]] 

player_key=[[1,'C'],[2,"_"],[3,"D"],[4,"_"],[5,"F"],[6,'L'], [7,'_'], [8,'T'], [9,"_"], [10,"I"], [11,'M'], [12,'B'],[13,"_"],[14,'N']]
answerkey=[[1,'C'],[2,'O'],[3,'D'],[4,'E'],[5,'F'], [6,'L'], [7,'A'], [8,'T'], [9,'H'], [10,'I'],[11,'M'], [12,'B'], [13,'U'],[14,'N']]
hidden_key = [[2,'O'], [4,'E'],[7,'A'],[9,'H'],[13,'U']]#list that contains all words that need to be guessed

#below I used list comprehenstion, I did this because other list methods did not work for me in the manner I wanted to. They would give me a specific copy of each list which was not the specific one I wanted. This creates its own unique lists. It is different to the actual 2d lists above
list_copy = [i[:] for i in grid]# i[:] makes a new list for every single individual row, #the for loop iterates over every sublist in the 2d list.
hidden_key_copy=[i[:] for i in hidden_key]


'''This function allows the admin to delete a word from the game and the grid'''
def delete_word():
    global player_key, answerkey, hidden_key, grid
    print('To remove a word off the game you must do it manually, letter by letter. ')
    num_letters=input('how many letters would you like to delete? ')#stores how many letters they would like to delete
    while num_letters.isdigit()==False or int(num_letters)>9:#loops if the variable is not a number
        print("enter a valid number")
        num_letters=input('how many letters would you like to delete? ')
    print('this process will repeat ' +num_letters+' time(s) unless you do not follow the instructions')
    num_letters = int(num_letters)
    while num_letters!=0:
        num_letters-=1
        index=input("Enter the index you would like to delete: ")
        letter=input('enter a letter you would like to delete: ').upper()
        while letter.isalpha()== False or str(index).isdigit()==False or len(letter)!=1 or letter=="" or index=="":#checks if letter not alphabetic, index not a number and checks if only one value has been inputted for letter
            print("ENTER VALID INPUTS")
            index=input("Enter the index you would like to delete: ")
            letter=input('enter a letter you would like to delete: ').upper()
        letter=str(letter)
        index=int(index)
        sublist=[int(index), letter]
        print(sublist)
        #for loop below delete sublist from the answer key if it is found in there
        for i in answerkey:
            if sublist == i:
                answerkey.remove(sublist)
         #for loop below delete sublist from the player key if the chosen index is found in there 
        for i in player_key:
            for j in i:
                if sublist[0]==j:
                    player_key.remove(i)
        #for loop below delete sublist from the hidden key if the chosen index is found in there
        for i in hidden_key:
            for j in i:
                if sublist[0]==j:
                    hidden_key.remove(i)
        #for loop goes through the grid to check for the deleted letters and numbers
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                value=grid[i][j]
                if sublist[0]==value or sublist[1]==value:
                    grid[i][j]="#"
        for i in grid:
            print(i)
    print(answerkey)
    print(player_key)
    print(hidden_key)
    choice = input('press any key to return to the admin menu: ')
    admin_menu()

''' READ THIS!!!!! BELOW: function to add a word  I HAVE COMMENTED OUT THE CODE, DUE TO THE FUNCTIONALITY NOT WORKING FULLY (I was not able to finish my error handling)'''

'''def add_word():
    global answerkey, hidden_key, player_key
    used_index=[]
    for i in answerkey:
        used_index.append(i[0])

    word = input("what is your word? ").upper()#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    while word.isalpha()==False or len(word)>9:
        print("ENTER A VALID WORD")
        word = input("what is your word? ").upper()#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    word_list=list(word)
    player_word_list=[]
    print('this process will repeat for ' +str(len(word))+ ' times, unless you do not follow the insructions')
    print(used_index)
    print('the list above only shows used indicies')
    for i in word_list:
        letter_index=(input("give each letter a number that has not been used: "))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        while letter_index.isdigit()==False:
            print("ENTER A VALID NUMBER")
            letter_index=(input("give each letter a number that has not been used: "))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        while letter_index in used_index or letter_index.isdigit() or int(letter_index) in used_index==False or letter_index=='':
            letter_index=(input("give each letter a number that has not been used: "))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        letter_index= int(letter_index)
        used_index.append(letter_index)
        sublist=[letter_index,i]
        answerkey.append(sublist)
        player_word_list.append(sublist)
    print(answerkey)

    hide_letters=(input('how many letters would you like to hide? '))
    while hide_letters.isdigit()==False:
        print('ENTER A VALID NUMBER')
        hide_letters=(input('how many letters would you like to hide? '))
    hide_letters=int(hide_letters)
    while hide_letters>len(word):
        print('ENTER A NUMBER SHORTER THAN THE LENGTH OF THE WORD')
        hide_letters=(input('how many letters would you like to hide? '))
    while hide_letters!=0:
        hide_letters-=1
        letter=(input('enter the letter you would like to hide: ')).upper()
        hide_index=((input('enter the index of the hidden letter: ')))
        while not letter.isalpha() or len(letter) != 1 or not str(hide_index).isdigit():
            hide_index=(input('enter the index of the hidden letter: '))
            letter=(input('enter the letter you would like to hide: ')).upper()
        sublist=[int(hide_index),str(letter)]
        print(sublist)
        for i in answerkey:
            while sublist not in answerkey:
                letter=str(input('enter the letter you would like to hide: ')).upper()
                hide_index=((input('enter the index of the hidden letter: ')))
                while not letter.isalpha() or len(letter) != 1 or not str(hide_index).isdigit():
                    letter=(input('enter the letter you would like to hide: ')).upper()
                    hide_index=(input('enter the index of the hidden letter: '))
                sublist=[int(hide_index),str(letter)]


        #sublist=[hide_index,letter]
        hidden_key.append(sublist)
        sublist=[hide_index,"_"]
        for i in player_word_list:
            for j in range(len(i)):
                if i[j] == letter:
                    i[j] = "_"
                    player_key.append(i)
        for i in answerkey:
            print(i[0])
            print(sublist)
            if i[0]==hide_index:
                i[1]=letter
        print(player_key)
        #print(hidden_key)
        print(answerkey)
    for i in range(len(word_list)):
        if word_list[i]==letter:
            word_list[i]=hide_index
    print("NOTE: To add a word vertically you will have to add it manually one by one")
    row = ((input('what row would you like to add a word? ')))
    index = ((input('where would you like your starting letter to be? ')))
    while row.isdigit()==False and index.isdigit()==False:
        row =((input('what row would you like to add a word? ')))
        index =((input('where would you like your starting letter to be? ')))
    row=int(row)
    index=int(index)
    index = int(index) - 1

    for i in word_list:
        grid[row][index]=i
        index=index+1
    for i in grid:
        print(i)

        for i in range(len(grid)):
                    for j in range(len(grid[i])):
                        if grid[i][j]==index:
                            position=(i,j)
                            original_letter=grid[i][j]
                            for x in grid:
                                grid[i][j]=letter
 '''                               



'''this prints the answers to the grid'''
def complete_grid():
    global grid
    for i in range(len(grid)):#iterates over the number/index of each sublist
        for j in range(len(grid[i])):#iterates within sublist of each value of the number/index
            for k in answerkey:#iterates through list answerkey
                grid_letter=grid[i][j]#assigns a grid postion to the variables

                #the code below checks if the variable is the same aas the first element of k, if it is it will assign the second element of k into that grid position
                if grid_letter==k[0]:
                    grid_letter=k[1]
                    grid[i][j]=k[1]

    for i in grid:
        print(i)
    grid=list_copy
    choice=input("Press any button to return to the admin menu: ")
    admin_menu()

'''Removes sublist from hidden_key, when a player guesses a letter correct'''
def remove_sublist(sublist1):
    global hidden_key
    hidden_key.remove(sublist1)


'''generates the variable grid, to appear as a grid and not a list'''
def codeword():
    for i in grid:#iterates over each sublist
        print(i)#prints the sublist line by line
    print(player_key)


'''This shows the player stats after the game'''
def player_stats():
    stats = open('PlayerStats.txt', 'w')#variable called stats, opens a textfile in write mode
    stats.write(player1 + ' These are your stats:\n Correct guesses: ' + str(p1_correct_guesses) + '.\n Incorrect guesses: ' + str(p1_incorrect_guesses) + '.\n Your final health: ' + str(p1_final_health) + '.\n\n\n')#writes this line into the textfile
    stats.write(player2 + ' These are your stats:\n Correct guesses: ' + str(p2_correct_guesses) + '.\n Incorrect guesses: ' + str(p2_incorrect_guesses) + '.\n Your final health: ' + str(p2_final_health) + '.\n\n\n')
    stats.close()#closes the file

    show_stats=input("would you like to see your stats or just return to the home screen \n yes or no: ")
    show_stats=show_stats.lower()
    if show_stats=='yes':
        #show them the stats
        print("okay")
        stats = open('PlayerStats.txt', 'r')#opens the file in read mode
        information = stats.read()#reads the textfile and places it inside the variable information
        print(information)#prints what is insdie the variables
        stats.close()#closes the file

    else:
        print("Goodbye")
        main_menu()
    main_menu()


'''this values restores player health to what it used to be, ready for another game'''
def restore_player_health():
    global player1
    global player2
    global player1_health
    global player2_health
    for i in database:
        if len(i)==4:
            for j in i:
                if j == player1:
                    player1_health=0
                    i[3]=5  
                if j == player2:
                    player2_health=0
                    i[3]=5

'''from the database it retrieves the player health  of the playera that are logged in'''
def retrieve_player_health():
    global player1
    global player2
    global player1_health
    global player2_health
    for i in database:# iterates through database 
        if len(i)==4:# checks if length of the sublist is 4
            for j in i:#iterates through each value in sublist
                if j ==player1:#checks if the value is the same as player1
                    player1_health=i[3]#assigns 4th value in sublist to the variables
                if j == player2:
                    player2_health=i[3]


'''This is the function, to increase player health'''
def increase_health(player):
    global player1_health
    global player2_health
    global p1_final_health
    global p2_final_health
    if player == player1:
        player1_health = player1_health + 2
        p1_final_health+=2
        print(player, "your health is now, "+str(player1_health)+".")
    if player == player2:
        player2_health = player2_health + 2
        p2_final_health+=2
        print("your health is now, "+str(player2_health)+".")


'''Function to decrease player health'''
def decrease_health(player):
    global player1
    global player2
    global player1_health
    global player2_health
    global p1_final_health
    global p2_final_health

    if player == player1:#checks if the parameter is same as player1
        player1_health = player1_health - 2#if the condition above is met, variable subtracted by 2
        p1_final_health-=2
        print("your health is now, "+str(player1_health)+".")
        if player1_health<=2:#check to see if the health is less than or equal to 2
            print("The game is over")
            player_stats()#runs function player stats
                        
    if player == player2:# process above is repeated but just for player2
        player2_health = player2_health - 2
        p2_final_health-=2
        print("your health is now, "+str(player2_health)+".")

        if player2_health<=2:
            print("The game is over")
            player_stats()
    

"""Function for player turns, this allows users to take turns in guessing letters within the game. Function updates player health and changes certain lists"""

def player_turn(player):
    global hidden_key,answerkey,player_key,grid,p1_correct_guesses,p1_incorrect_guesses,p2_correct_guesses,p2_incorrect_guesses,p1_final_health,p2_final_health

    if player == player1:#checks if parameter from player menu is player1
        print(player1, ',it is your turn to play')
        codeword()#runs function which prints out codewordgrid
        while player1_health>=3 and player2_health>=3:#loop that carries on, as long as health for both players are greater than 3
            while hidden_key!= []:#while loop checks if hidden_key is not empty
                index=(input("pick an index number shown on the screen: "))
                while index.isdigit()==False:#will keep looping unless a number is inputted
                    print("enter a valid number")
                    index=(input("pick an index: "))

                index = int(index)#turn index into an integer
                initial_value=0#Variable that will be used later, to store initial value from grid 
                grid_coordinate=[0][0]#syntax is incorrrect, to be used for try except block later on
                letter=(input("enter a letter: "))
                letter=letter.upper()#turns input in a capital letter
                while letter.isalpha()==False or len(letter)>1:
                    print('enter one letter')
                    letter=(input("enter a letter: "))
                    letter=letter.upper()#turns input in a capital letter
                for i in range(len(grid)):#iterates over each index of the grid
                    for j in range(len(grid[i])):#iterates over each sub-index of sublist
                        # i and j are essentially being used as coordinates on the grid, can also view them as rows and columns 
                        if grid[i][j]==index:#checks if current value at coordinate (i,j) is same as value held in index
                            grid_coordinate=(i,j)#holds coordinate of where values match
                            initial_value=grid[i][j]#whatever is held in that specific postion (i.e number 2 or letter M) is stored into orignal_letter
                            for x in grid:#iterates over each sublist in grid
                                grid[i][j]=letter#places user input, letter inside grid postion (i,j)
                                break

                for i in grid: #iterates over each list
                    print(i)
                print("this is how it would look like")   
                sublist = [index, str(letter)]#takes user input and turns it into a list
                if sublist in hidden_key:# checks if sublist is in hidden_key
                    print("well done, you got it right")#if sublist is in hidden key, player guessed the letter correctly
                    remove_sublist(sublist)#function to remove sublist from hidden_key list
                    increase_health(player1)#runs function to increase player health
                    p1_correct_guesses = p1_correct_guesses + 1#updates correct guesses variable
                    replay=input('would you like to carry on?\n type yes to carry on or any button to log out: ')
                    if replay.lower()=='yes':
                        player_turn(player2)
                        break
                    else:
                        print("WARNING: by logging out all progress will be lost and reset")
                        replay=input("do you wish to log out?\n press yes to log out or any button to carry on: ")
                        if replay.lower()=='yes':
                            print("goodbye")
                            grid=list_copy#if player quits the game, grid is reset
                            restore_player_health()
                            player_stats()
                        else:
                            player_turn(player2)#if game carries on, it is the users turn
                else:
                    #code below uses try-except, allows me to work with data that causes errors, if an error occurs. For me, the way i used the try-except, it means there is an index inputted not in use in the grid (note: this is how i used it, not saying it is good practice of how i used it)
                    try:
                        x, y = grid_coordinate#what ever values were in grid coordinate, now have been assigned to new variables to x and y
                        grid[x][y]=initial_value#using x and y, i can access the the postion of the orignal place and assign initial_value back to grid(only done when the player got the letter wrong)
                        decrease_health(player1)
                        print('Either,you got it wrong or you already entered the letter')
                        p1_incorrect_guesses= p1_incorrect_guesses+1
                        replay=input('would you like to carry on?\n type yes to carry on or any button to log out: ')
                        if replay.lower()=='yes':
                            player_turn(player2)
                            break
                        else:
                            print("WARNING: by logging out all progress will be lost and reset")
                            replay=input("do you wish to log out?\n press yes to log out or any button to carry on: ")
                            if replay.lower()=='yes':
                                print("goodbye")
                                grid=list_copy
                                restore_player_health()
                                player_stats()
                            else:
                                player_turn(player2)
                    except TypeError:#if this error occurs, it means that grid_coordinate does not have any proper values or was not typed correctly as i planned, will allow for player to have another go
                        print('CHOOSE AN INDEX FROM THE GRID, NOT ONES THAT ARE NOT SHOWN TO YOU')#tells the player to pick an index show in the grid
                        player_turn(player1)

                    
            print("Well done, you finished the puzzle")
            break#breaks from the while loop of checking for an empty list
        grid=list_copy
        hidden_key=hidden_key_copy#fills the list back with the original values
        restore_player_health()
        player_stats()

    else:
        print(player2, ',it is your turn to play')
        codeword()
        while player1_health>=3 and player2_health>=3:
            while hidden_key!= []:
                index=(input("pick an index number shown on the screen: "))
                while index.isdigit()==False:
                    print("enter a valid number")
                    index=(input("pick an index: "))
                index = int(index)
                initial_value=0
                grid_coordinate=[0][0]
                letter=(input("enter a letter: "))
                letter=letter.upper()
                for i in range(len(grid)):
                    for j in range(len(grid[i])):
                        if grid[i][j]==index:
                            grid_coordinate=(i,j)
                            initial_value=grid[i][j]
                            for x in grid:
                                grid[i][j]=letter
                
                for i in grid: #iterates over each list
                    print(i)
                print("\nthis is how it would look like")   
                sublist = [index, str(letter)]
                if sublist in hidden_key:
                    print("well done, you got it right")
                    remove_sublist(sublist)
                    increase_health(player2)
                    p2_correct_guesses=p2_correct_guesses+1
                    replay=input('would you like to carry on?\n type yes to carry on or any button to log out: ')
                    if replay.lower()=='yes':
                        player_turn(player1)
                        break
                    else:
                        print("WARNING: by logging out all progress will be lost and reset")
                        replay=input("do you wish to log out?\n press yes to log out or any button to carry on: ")
                        if replay.lower()=='yes':
                            print("goodbye")
                            grid=list_copy
                            restore_player_health()
                            player_stats()
                        else:
                            player_turn(player1)
                else:
                    try:
                        x, y = grid_coordinate
                        grid[x][y]=initial_value
                        decrease_health(player2)
                        print('Either,you got it wrong or you already entered the letter')
                        p2_incorrect_guesses = p2_incorrect_guesses+1
                        replay=input('would you like to carry on?\n type yes to carry on or any button to log out: ')
                        if replay.lower()=='yes':
                            player_turn(player1)
                            break
                        else:
                            print("WARNING: by logging out all progress will be lost and reset")
                            replay=input("do you wish to log out?\n press yes to log out or any button to carry on: ")
                            if replay.lower()=='yes':
                                print("goodbye")
                                grid=list_copy
                                restore_player_health()
                                player_stats()
                            else:
                                player_turn(player1)
                    except TypeError:
                        print('CHOOSE AN INDEX FROM THE GRID, NOT ONES THAT ARE NOT SHOWN TO YOU')
                        player_turn(player2)
            print("Well done, you finished the puzzle")
            break
        grid=list_copy
        hidden_key=hidden_key_copy
        restore_player_health()
        player_stats()


'''Function for player menu, give user option so play the game or log out'''
def player_menu():
    print("This is the menu page")
    option = input("Do you want to play the game or sign out\n press yes to play or any button to sign out ").lower()
    if option == 'yes':
        print('the game will now run')
        print("Rules: Pick an index and choose a letter\n Correct? you will get plus 2 health.\n Wrong? then you will lose 2 \n")
        print(player1,': you have ' +str(player1_health)+ ' health' )#outputs players name with how much health they have
        print(player2,': you have ' +str(player2_health)+ ' health' )

        player_turn(player1)#will run player turn function with player1 as its parameter
    else:
        print('you will be signed out now')
        main_menu()
    

'''Function shows options to what the admin can do'''
def admin_menu():

    print('this is the admin menu and here are the option down below: \n')
    print('1.Display the code word puzzle with the answers\n2.Display the code word puzzle shown to players\n3.Display the answer key\n4.Display the player key\n5.Add a different word to the puzzle. Show all grids/keys \n6.Delete a word from the puzzle\n7. show all grids\n8. To log out')#shows all admin options
    num = (input("Please pick an option: "))#asks user to enter a number
    if num=='1':#option 1 shows answer grid
        print("This is the answer grid")
        complete_grid()
    elif num=='2':#option 2 shows player grod
        print("\n this is the player grid")
        for i in grid:#iterates over sublist in grid
            print(i)#prints each sublist
        choice=input("press any button to go back to the admin menu: ")
        admin_menu()

    elif num=='3':#option 3 shows the answer key
        print("\nthis is the answer key:")
        print(answerkey)
        choice=input('press any key to return to the admin menu: ')
        admin_menu()

    elif num=='4':#option 4 shows player key
        print("\nthis is the player key")
        print(player_key)
        choice=input('press any key to return to the admin menu: ')
        admin_menu()

    elif num=='5':# option 5 allows admin to add words
        print("What word would you like to add: ")
        choice=input("press any button to return to the admin screen: ")
        admin_menu()

    elif num=='6':#allows admin to delete a word
        delete_word()
    
    elif num=='7':
        for i in grid:
            print(i)
        print(answerkey)
        print(player_key)
        print('\n')
        complete_grid()
        choice=input('press any key to log out: ')
        main_menu()
    elif num=="8":
        main_menu()

    else:# if any of the option above are not picked it will rerun admin menu until a valid number is picked
        print('\n\n\n\nPICK A VALID OPTION')
        admin_menu()


'''Function allows to make new admin users or player users, takes a parameter'''
def create_new_user(user):
    if user == 'admin':#if parameter holds 'admin', the below will run
        username = input("Enter username: ")
        password = input("Enter password: ")
        while username=="" or password=='':
            username = input("Enter username: ")
            password = input("Enter password: ")
        hashed_username = hashlib.sha256(username.encode()).hexdigest()# ".encode" encodes password, ".hexdigest" turns data into hex
        hashed_password = hashlib.sha256(password.encode()).hexdigest()# ".encode" encodes password, ".hexdigest" turns data into hex
        user = [username, hashed_username, hashed_password] #puts input into a list called user
        database.append(user)#adds it to database, used for logging in
        print("you will now be returned to the main menu")
        print(database)
        main_menu()
        return
    
    elif user == "player":#below will run if parameter is "player"
        username = input("Enter username: ")
        password = input("Enter password: ")
        while username=="" or password=='':
            username = input("Enter username: ")
            password = input("Enter password: ")
        hashed_username = hashlib.sha256(username.encode()).hexdigest()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = [username, hashed_username, hashed_password, 5]
        database.append(user)
        print("you will now be returned to the main menu")
        print(database)
        main_menu()
        return


'''login function for both players and admin, it takes a parameter, which helps to see which login is needed''' 
def login(number):
    global player1
    global player2
    if number=='1':# if the parameter is 1, it will run admin login
        login_counter = 3#initialises variable to 3, used to keep track of the attempts left
        while login_counter > 0:#while loop makes the block of code below to repeat as long as login_counter is not 0
            print("this is the admin login system")
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            for user in database:#iterates through 2d list called database
                if user[1] == hashlib.sha256(username.encode()).hexdigest() and user[2] == hashlib.sha256(password.encode()).hexdigest() and len(user)==3:#encodes user inputs, checks if second and third value in sublist matches to the encoding, check if length of sublist is 3. All 3 conditions must be met
                    print("hello " +user[0]+".")
                    admin_menu()
            else:#runs if conditions of if statement are not met
                login_counter =login_counter- 1#subtracts 1 from login_counter
                print("you either got your details wrong, or you are not an admin")
                print('attempts left: ', login_counter)
                if login_counter == 0:#will check if login_counter has a value of 0
                    print("you will be returned to the main menu, since you had three failed login attempts")
                    main_menu()#returns to the main menu

    else:#will run code below, if parameter is not 1
        login_counter = 3
        while login_counter >0:
            print('this is the player login')
            username1 = input("enter player1 username: ")
            password1 = input("enter player1 password: ")
            username2 = input("\nenter player2 username: ")
            password2 = input("enter player2 password: ")
            for user in database:#iterates 2d list called database
                if user[1] == hashlib.sha256(username1.encode()).hexdigest() and user[2]==hashlib.sha256(password1.encode()).hexdigest() and len(user)==4:#checks encoding of username1 and password1 matches second and third value in the sublist of database, checks if the length of the sublist is 4, users with 5 in sublist can play 
                    print("player1 you have logged in")
                    
                    for user2 in database:
                        if user2[1] == hashlib.sha256(username2.encode()).hexdigest() and user2[2]==hashlib.sha256(password2.encode()).hexdigest() and len(user)==4:#checks encoding of username2 and password2 matches second and third value in the sublist of database, checks if the length of the sublist is 4, users with 5 in sublist can play 
                            #both if statements must be met for below to run
                            print("player2 you have logged in")
                            print('hello, '+username1+" and " +username2+".")
                            player1=username1
                            player2=username2
                            retrieve_player_health()#runs function
                            player_menu()#runs player menu function
                            return
            else:#
                login_counter = login_counter -1
                print("Either one of you got your details wrong,\nattempted to log in via an admin account\nor you do not have user details")
                print('attempts left: ', login_counter)
                if login_counter == 0:
                    print("you will be returned to the main menu, since you had three failed login attempts")
                    main_menu()
            #run main menu function


''' main menu function, allows users to login or make a new user'''
def main_menu():
    print('welcome to, codeword hangman\n press 1 to login as admin, \n press 2 to login as a player \n press 3 to exit the system: \n press 4 to create a new admin user \n press 5 to make a new player user ') #tells the user what options it has 
    num=str(input('enter a number: ')) #takes its input
    if num != '1' and  num != '2' and num!='3' and num!='4' and num!='5':#checks if the input is none of the three numbers
        print('YOU MUST PICK FROM THE CHOICES YOU HAVE BEEN GIVEN\n')
        main_menu()# if it has not picked from any of the choices then it will rerun the main menu

    elif num == '1':
        login('1')# if 1 pressed then it will go to the admin login
    elif num =="2":# if 2 pressed then it will go to the player login
        login(2)
    elif num =='3':# if 3 pressed then it will exit the program
        SystemExit
    elif num =='4':
        create_new_user('admin')# if 4 pressed start create_new_user function for admins
    else:
        create_new_user('player')# if 5 pressed then it will start create_new_user function for players
main_menu()