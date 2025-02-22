import random

class Solution:
    def __init__(self):
        self.Actual_Number = random.randint(1, 100)
        self.No_of_Guesses = 0
    
    def func(self):
        try:
            num = int(input("Guess a number: "))  # Input and conversion to int
            
            if num >= 1 and num <= 100:  # Allow 1 to 100 as valid inputs
                if self.Actual_Number == num:
                    print("Match Successful")
                    self.No_of_Guesses += 1
                    print(f"You guessed the number in {self.No_of_Guesses} tries.")
                
                    play_again = input("Do you want to play again? (yes/no): ").lower()
                    if play_again == 'yes':
                        self.Actual_Number = random.randint(1, 100)
                        self.No_of_Guesses = 0
                        self.func()
                    else:
                        print("Thank you for playing")
                    return
            
                elif self.Actual_Number > num:
                    print("Higher number please")
                    self.No_of_Guesses += 1
            
                elif self.Actual_Number < num:
                    print("Lower number please")
                    self.No_of_Guesses += 1
            
                self.func()
                
            else:
                print("Invalid Value! Please enter a number between 1 and 100.")
                self.func()  # Ask for input again if invalid
        
        except ValueError:
            # If input is not an integer, this block will run
            print("Invalid input! Please enter a numeric value.")
            self.func()  # Ask for input again if non-numeric

test = Solution()
test.func()
print("End of this Game")