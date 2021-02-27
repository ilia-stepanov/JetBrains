def luhn_digit(x):
    x2 = []
    for index, num in enumerate(str(x)):
        if index % 2 == 0:
            if int(num) * 2 > 9:
                x2.append(int(num) * 2 - 9)
            else:
                x2.append(int(num) * 2)

        else:
            if int(num) > 9:
                x2.append(int(num) - 9)
            else:
                x2.append(int(num))

    if sum(x2) % 10 == 0:
        return 0

    else:
        return 10 - sum(x2) % 10


def main_option():
    option = int(input('''1. Create an account
2. Log into account
0. Exit \n'''))
    return option

def log_option():
    option= int(input('''1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit \n'''))
    return option

def create_account():
    new_card =  random.randint(400000001000000, 400000009999999)
    last = luhn_digit(new_card)
    new_card = new_card * 10 + last
    new_pin = random.randint(1000, 9999)
     
    query = 'select * from card where number = "' + str(new_card) + '"'
    cur.execute(query)
    conn.commit()
    check = cur.fetchall()
    
    while check != []:
        new_card = random.randint(400000001000000, 400000009999999)
        last = luhn_digit(new_card)
        new_card = new_card * 10 + last
        query = 'select * from card where number = "' + str(new_card) + '"'
        cur.execute(query)
        conn.commit()
        check = cur.fetchall()


    query = 'insert into card (number, pin) values ("' + str(new_card) + '", "' + str(new_pin) + '")'
    cur.execute(query)
    conn.commit()
    print('''
Your card has been created
Your card number:
%s
Your card PIN:
%s\n''' % (new_card, new_pin))


def log_into():
    old_card = int(input('\nEnter your card number:\n'))
    old_pin = int(input('Enter your PIN:\n'))
    
    query = 'select number, pin from card where number = "' + str(old_card) + '" and pin = "' + str(old_pin) + '"'
    cur.execute(query)
    conn.commit()
    output = cur.fetchall()
    flag = output != []     
    
    if flag:        
        print('\nYou have successfully logged in!\n')
        return [old_card, old_pin]    

    else:
        print('\nWrong card number or PIN!\n')
        return [-1, -1]
    
def transfer_into(old_card):
    transfer_card = input('''\nTransfer 
Enter card number:\n''')
    
    query = 'select number from card where number like "' + str(transfer_card) + '%"'
    cur.execute(query)
    conn.commit()
    output = cur.fetchall()
    flag = output != []      
    

    if int(str(transfer_card)[-1]) != luhn_digit(int(str(transfer_card)[:-1])):
        print('Probably you made a mistake in the card number. Please try again!\n')


    elif flag: 
        transfer_sum = input('Enter how much money you want to transfer:\n')

        query = 'select balance from card where number = "' + str(old_card) + '"'
        cur.execute(query)
        conn.commit()
        output = cur.fetchall()

        if int(transfer_sum) <= int(output[0][0]):
            query = 'update card set balance = balance - ' + str(transfer_sum) + ' where number = "' + str(old_card) + '"'
            cur.execute(query)
            conn.commit()

            query = 'update card set balance = balance + ' + str(transfer_sum) + ' where number = "' + str(transfer_card) + '"'
            cur.execute(query)
            conn.commit()   

            print('Success!\n')

        else:
            print('Not enough money!\n')
            

    else:
        print('\nSuch a card does not exist.\n')
        
    
def close_account(old_card):
    query = 'delete from card where number = "' + str(old_card) + '"'
    cur.execute(query)
    conn.commit()
    print('\nThe account has been closed!\n')


def enter_income(old_card):
    num = input('\nEnter income:\n')

    query = 'update card set balance = balance + ' + str(num) + ' where number = "' + str(old_card) + '"'
    cur.execute(query)
    conn.commit()
    print('Income was added!\n')
    
def get_balance(old_card):
    query = 'select balance from card where number = "' + str(old_card) + '"'
    cur.execute(query)
    conn.commit()
    balance = cur.fetchone()
    return balance[0]
    
    
import random
accounts = dict()

import sqlite3
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

cur.execute('drop table if exists card')
cur.execute('create table card (id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)')
conn.commit()

option = main_option()
while int(option) != 0:
    if option == 1:
        create_account()
        option = main_option()

    elif option == 2:
        old_card, old_pin = log_into()
        if old_card != -1:             
            option2 = log_option()
            if option2 == 0:
                option = 0
                
            while int(option2) != 0:
                if option2 == 1:
                    balance = get_balance(old_card)                    
                    print('\nBalance: %s\n' % balance)
                    option2 = log_option()
                if option2 == 2:
                    enter_income(old_card)
                    option2 = log_option()
                    
                if option2 == 3:
                    transfer_into(old_card)
                    option2 = log_option()

                if option2 == 4:
                    close_account(old_card)
                    option = main_option()
                    break                 
                    
                    
                if option2 == 5:
                    print('\nYou have successfully logged out!\n')
                    option = main_option()
                    break
                if option2 == 0:
                    option = 0
        else:
            option = main_option()

print('\nBye!')
