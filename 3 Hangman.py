def mult(x, ls):
    ind = []
    for i, y in enumerate(ls):
        if x == y:
            ind.append(i)
    if len(ind) > 0:
        return ind
    else:
        return -1 
def hangman():
    import random
    print()
    options = ['python', 'java', 'kotlin', 'javascript']
    right = random.choice(options)
    open_word = len(right) * '-'
    open_word_list = list(open_word)

    counter = 0
    ls = []
    while counter < 8:
        print(open_word)
        guess_word = input('Input a letter:')

        if guess_word in ls and len(guess_word) == 1:
            print("You've already guessed this letter")
        elif len(guess_word) > 1:
            print('You should input a single letter')
        elif guess_word not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a lowercase English letter')  
        elif guess_word in 'abcdefghijklmnopqrstuvwxyz':


            if guess_word in right and guess_word not in open_word:
                idx = mult(guess_word, right)
                for i in idx:
                    open_word_list[i] = guess_word
                    open_word = str(''.join(open_word_list))
            else:
                counter += 1
                print("That letter doesn't appear in the word")
        ls.append(guess_word)



        if counter < 8 or open_word == right:
            print()

        if open_word == right:
            print(right, 'You guessed the word!', 'You survived!', sep='\n')
            break

    if open_word != right:
        print('You lost!', sep='\n')

print('H A N G M A N')
act = input('Type "play" to play the game, "exit" to quit:')
while act != 'exit':
    if act == 'play':
        hangman()
        act = ''
    else:
        act = input('Type "play" to play the game, "exit" to quit:')   
