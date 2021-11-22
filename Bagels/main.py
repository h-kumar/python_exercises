import random

# constants
NUM_LIMIT = 3
MAX_GUESS = 10

def main():
    while True:
        secretNum = getSecretNum()
        print('I have though up of a number {}.'.format(secretNum))
        print('You have {} guess to get it.'.format(MAX_GUESS))
        numGuess = 1
        while numGuess <= MAX_GUESS:
            guess = ''
            while len(guess) != NUM_LIMIT or not guess.isdecimal():
                print('Guess #{}'.format(numGuess))
                guess = input('> ')
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuess+=1

            if guess == secretNum:
                break
            if numGuess > MAX_GUESS:
                print('You ran out of guesses.')
                print(f'The secret number was {secretNum}')

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break

    print('Thanks for playing!')

            



def getSecretNum():
    nums = list('0123456789')
    random.shuffle(nums)

    secretNum = ''
    for i in range(NUM_LIMIT):
        secretNum += str(nums[i])
    return secretNum



def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for c in range(len(guess)):
        if guess[c] == secretNum[c]:
            clues.append('Fermi')
        elif guess[c] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return '_'.join(clues)

if __name__ == '__main__':
    main()