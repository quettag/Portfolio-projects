player1_score = 0
player2_score = 0
player1_health = 5
player2_health = 5
lst = []

while True:
    player = input("Enter Player1 or Player2?: ")#To indentify who is player1 and player2
    if player.lower() == "end":#check if the players want to end the game
        print("player1 score",player1_score)
        print("player2 score",player2_score)
        if player1_score > player2_score:
            print("PLAYER1 WINS")
        else:
            print("PLAYER2 WINS")
        break
    while player == '' or player.isspace() == True or player.lower() != 'player1' and player.lower() != 'player2':
        player = input("Re-enter Player1 or Player2?: ")#data validation to ensure the proper input is entered
        
    
    if player.lower() == 'player2':
        userint = input("Enter a word ")
        dash = ((len(userint)*'-'))#converting the word into dashes
        for i in range(35):
            print('-')#prints 35 dashes to cover the word entered by previous player
        
        while dash != userint and player2_health >0:#asks to input a letter of the word
            userint_2 = input("Enter a letter ")
            
            if player2_health <= 1:
                print("YOU LOSE")
            if userint_2 in userint:
                pos = userint.find(userint_2)
                dash = dash[:pos] + userint_2 + dash[pos + 1:]#finds the position of characters and replaces it with dashes.
            
                for index,item in enumerate(userint):
                    if item == userint_2:
                        lst.append(index)
                    
                        for elem in lst:
                            dash = dash[:elem] +            userint_2 + dash[elem + 1:]
                            lst.clear()
                            
            else:
                player2_health -= 1#health decreases if the letter entered is wrong
                print("Incorrect!")
                print("Health left: "+ str(player2_health))
                            
            if dash == userint:
                player2_score += 1
                print("You win Player2, your score is",player2_score)
            else:
                print(dash)
            
    if player.lower() == 'player1':
        userint = input("Enter a word ")
        dash = ((len(userint)*'-'))
        for i in range(35):
            print('-')
        while dash != userint and player1_health >0:
            userint_2 = input("Enter a letter ")
            
            if player1_health <= 1:
                print("YOU LOSE")
            if userint_2 in userint:
                pos = userint.find(userint_2)
                dash = dash[:pos] + userint_2 + dash[pos + 1:]
            
                for index,item in enumerate(userint):
                    if item == userint_2:
                        lst.append(index)
                    
                        for elem in lst:
                            dash = dash[:elem] +            userint_2 + dash[elem + 1:]
                            lst.clear()
                            
            else:
                player1_health -= 1
                print("Incorrect!")
                print("Health left: "+ str(player1_health))
                            
            if dash == userint:
                player1_score += 1
                print("You win Player1, your score is",player1_score)
            else:
                print(dash)