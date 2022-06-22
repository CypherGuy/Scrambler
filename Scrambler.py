import random
import time

run = True

userStats = {'streak': 0}
def sendFail(unscrambledWord):
    run = False
    userStats['streak'] = 0
    return print(f"Wrong. it was -> {unscrambledWord}. Your streak has been reset.")

def main(userStats):
    with open('scramblewords.txt', 'r') as f: 
        lines = f.readlines()
    unscrambledWord = str(random.choice(lines))
    print(unscrambledWord)
    shuffledList = list(unscrambledWord[:-1])
    random.shuffle(shuffledList)
    shuffledWord = ''.join(shuffledList)
    answer = input(f"Unscramble this word: {shuffledWord}\n")
    if answer in unscrambledWord:
        if '\n' in unscrambledWord: #Accounts for \n
            if len(answer) + 1 == len(unscrambledWord):
                '''Prevents a 1 letter answer being right, and ensures the right 
                length'''
                userStats['streak'] += 1
                print("Correct!")
                time.sleep(0.3)
                print(f"Your streak is now: {userStats['streak']}.")
            else:
                sendFail(unscrambledWord)
        else:
            sendFail(unscrambledWord)
    else:
        sendFail(unscrambledWord)
        
while run == True:
    main(userStats)

