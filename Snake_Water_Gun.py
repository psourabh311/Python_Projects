def choose(p1, p2):
    # Check if Player 1's input is invalid
    if p1 > 3 or p1 < 1:
        print("Give Correct Input for Player 1")
        return False
    
    # Check if Player 2's input is invalid
    if p2 > 3 or p2 < 1:
        print("Give Correct Input for Player 2")
        return False
    
    # Displaying Player 1's choice
    print("Player 1 chooses: ", end=" ")
    if p1 == 1:
        print("Snake")
    elif p1 == 2:
        print("Water")
    elif p1 == 3:
        print("Gun")
        
    # Displaying Player 2's choice
    print("Player 2 chooses: ", end=" ")
    if p2 == 1:
        print("Snake")
    elif p2 == 2:
        print("Water")
    elif p2 == 3:
        print("Gun")
        
    return True  # Inputs are valid

# Game loop
while True:
    # Input for Player 1
    p1 = int(input("Player 1 - Choose: 1 for Snake, 2 for Water, 3 for Gun: "))
    
    # Input for Player 2
    p2 = int(input("Player 2 - Choose: 1 for Snake, 2 for Water, 3 for Gun: "))

    # Check if inputs are valid
    if not choose(p1, p2):  
        continue  # Restart the loop if input is invalid

    # Result Calculation
    if p1 == 1 and p2 == 2:
        print("Player 1 Wins")
    elif p1 == 2 and p2 == 3:
        print("Player 1 Wins")
    elif p1 == 3 and p2 == 1:
        print("Player 1 Wins")
    elif p1 == p2:
        print("It's a Draw")
    else:
        print("Player 2 Wins")

    # Ask if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break  # Exit the loop if the answer is not 'yes'
