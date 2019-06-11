import random
def play_slot_machine(symbols = ['sevens', 'oranges', 'lemons','cash','gold bar', 'cherries','WIN', 'grapes'], wheels = 5):
    roulette = []
    for x in range(0,wheels):
         roulette += random.sample(symbols, 1)
         print(roulette)
    return roulette

def calc_prize_five(selections):
    if selections[0] == selections[1] == selections[2] == selections[3] == selections[4] == 'WIN':
        calc_prize_five == 50
        return '50X'
    elif selections[0] == selections[1]  == selections[2] == selections[3] == selections[4] != 'WIN':
        calc_prize_five == 20
        return '20X'
    elif selections[0] == selections[4] and selections[1]  == selections[2] == selections[3]:
        calc_prize_five == 15
        return '15X'
    elif selections[0] == selections[2] == selections[4]:
        calc_prize_five == 10
        return '10X'
    elif selections[0] == selections[4]:
        calc_prize_five == 5
        return '5X'
    else:
        calc_prize_five == 0
        return 'LOSE'

# #Correct this function
# #You may not add or delete lines
# #You must correct lines in place, focus on indentation, logic, and correct usage of functions and variables

def gamble_sim(capital = int(input('How much money do you have?: ')) , bet_amount = int(input('How much do you want to bet?: ')), max_plays = 10000):
    counter = 0
    while float(capital) > 0 and counter < max_plays:
        capital += bet_amount
        counter += 1
        prize = calc_prize_five(play_slot_machine())
        #Needs rewritten, think what would capital be if prize is lose?
        if prize == 'LOSE':
            capital = bet_amount * prize
            return capital
print(gamble_sim())

#there should be no main program or test code in this file
#and especially NO INPUT LINES


import random

def play_slot_machine(symbols = ['sevens', 'oranges', 'lemons','cash','gold bar', 'cherries','WIN', 'grapes'], wheels = 3):
    roulette = []
    #we probably want to use wheelse in here somewhere... where could it go?
    #Hint: think what wheels is used for.
    for x in range(0,5):
         roulette += random.sample(symbols, 1)
    return roulette
play_slot_machine()

def calc_prize_five(selections):
    #1c) Examin these returns, looking fishy in 1b's logic
    #Also, VERY VERY dangerous having variables named exactly the same as a function, im guessing your trying to set the function equal
    #to those numbers, however you are creating a variable that is called that, not actually assigning the function to that value
    #the only way to assign a function a value is through the return keyphrase
    if selections[0] == selections[1] == selections[2] == selections[3] == selections[4] == 'WIN':
        calc_prize_five == 50
        return '50X'
    elif selections[0] == selections[1]  == selections[2] == selections[3] == selections[4] != 'WIN':
        calc_prize_five == 20
        return '20X'
    elif selections[0] == selections[4] and selections[1]  == selections[2] == selections[3]:
        calc_prize_five == 15
        return '15X'
    elif selections[0] == selections[2] == selections[4]:
        calc_prize_five == 10
        return '10X'
    elif selections[0] == selections[4]:
        calc_prize_five == 5
        return '5X'
    else:
        calc_prize_five == 0
        return 'LOSE'

# #Correct this function
# #You may not add or delete lines
# #You must correct lines in place, focus on indentation, logic, and correct usage of functions and variables

def gamble_sim(capital = int(input('How much money do you have?: ')) , bet_amount = int(input('How much do you want to bet?: ')), max_plays = 10000):
    counter = 0
    while float(capital) > 0 and counter < max_plays:
        capital += bet_amount
        counter += 1
        #1b) This is correct, keep this, however take a look at what calc_prize_five(play_slot_machine()) is returning, is it a number or a string? refer to 1c.
        prize = calc_prize_five(play_slot_machine())
        #This needs rewritten, you want to return lose if 'lose'
        #you want to make another elif statement handling non-losses
        if prize == 'LOSE':
            capital = bet_amount * prize
            return capital
#1a) Examin what this is doing as a function call, do you really need to pass in the other nested functions?, refer to comment 1b
gamble_sim(calc_prize_five(play_slot_machine()))

#there should be no main program or test code in this file
#and especially NO INPUT LINES
