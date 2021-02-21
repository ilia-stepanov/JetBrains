def remaining(water, milk, beans, cups, money):
    if money != 0:
        print('''The coffee machine has:
%s of water
%s of milk
%s of coffee beans
%s of disposable cups
$%s of money \n''' % (water, milk, beans, cups, money))
        return [water, milk, beans, cups, money]
    else:
        print('''The coffee machine has:
%s of water
%s of milk
%s of coffee beans
%s of disposable cups
%s of money \n''' % (water, milk, beans, cups, money))
        return [water, milk, beans, cups, money]
    
    
def buy(water, milk, beans, cups, money):
    ex = [water, milk, beans, cups, money]
    buy = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n')
    if buy == 'back':
        return [water, milk, beans, cups, money]
    else:
        buy = int(buy)
        if buy == 1:
            water -= 250
            beans -= 16
            money += 4
            cups -= 1
        elif buy == 2:
            water -= 350
            milk -= 75
            beans -= 20
            money += 7
            cups -= 1
        elif buy == 3:
            water -= 200
            milk -= 100
            beans -= 12
            money += 6
            cups -= 1
    
    if min([water, milk, beans, cups, money]) >= 0:
        print('I have enough resources, making you a coffee!')
        return [water, milk, beans, cups, money]
    else:
        if water < 0:
            print('Sorry, not enough water!')
        if milk < 0:
            print('Sorry, not enough milk!')
        if beans < 0:
            print('Sorry, not enough beans!')
        if cups < 0:
            print('Sorry, not enough cups!')
        return ex


def fill(water, milk, beans, cups):
    water += int(input('Write how many ml of water do you want to add: \n'))
    milk += int(input('Write how many ml of milk do you want to add: \n'))
    beans += int(input('Write how many grams of coffee beans do you want to add: \n'))
    cups += int(input('Write how many disposable cups of coffee do you want to add: \n')) 
    return [water, milk, beans, cups]

def take(money):
    print('I gave you $%s' % money)
    money = 0
    return money 
    
water = 400
milk = 540
beans = 120
cups = 9
money = 550
action = ''

while action != 'exit':
    action = input('Write action (buy, fill, take, remaining, exit): \n')
    print()
    
    if action == 'remaining':
        water, milk, beans, cups, money = remaining(water, milk, beans, cups, money)
    elif action == 'buy':
        water, milk, beans, cups, money = buy(water, milk, beans, cups, money)
    elif action == 'fill':
        water, milk, beans, cups = fill(water, milk, beans, cups)
    elif action == 'take':
        money = take(money)
