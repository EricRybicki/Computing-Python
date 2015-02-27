print "Please think of a number between 0 and 100!"
x = 50
numGuesses = 0
possibilities = { "l", "h", "c"}
low = 0
high = 100
test = ""
ans = (high + low)/2
while True:
    print("Is your secret number " + str(round(ans)) + "?")
    test = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if test == "c":
        break
    if test not in possibilities:
        print "Sorry, I did not understand your input." 
    elif test == "l":
        low = ans
        ans = (high + low)/2
    else:
        high = ans
        ans = (high + low)/2
print('Game over. Your secret number was: ' + str(round(ans)))        
    