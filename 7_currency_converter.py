def check_cash(cash, r_dict, wanted_currency):
    num = int(input())
    print('Checking the cache…')

# 5 Take a look at the cache. Maybe you already have what you need?
# 6 If you have the currency in your cache, calculate the amount.
    if wanted_currency in cash:
        print('Oh! It is in the cache!')
        print('You received %s %s.' % (round(num * cash[wanted_currency], 2), wanted_currency.upper()))
        return cash
# 7 If not, get it from the site, and calculate the amount.
# 8 Save all the information to your cache.
    else:
        print('Sorry, but it is not in the cache!')
        cash[wanted_currency] = r_dict[wanted_currency]['rate']
        print('You received %s %s.' % (round(num * cash[wanted_currency], 2), wanted_currency.upper()))
        return cash

import requests
# 1 Take the currency code, the amount of money that you have, and the currency code that you want to receive as the user input.
having_currency = input().lower()

# 2 Retrieve the data from FloatRates as in the previous exercises.
url = ('http://www.floatrates.com/daily/' + having_currency + '.json').lower()
r = requests.get(url)
r_dict = r.json()

# 3 Save the exchange rates for USD and EUR.
cash = dict()
if having_currency == 'eur':
    cash['usd'] = r_dict['usd']['rate']
elif having_currency == 'usd':
    cash['eur'] = r_dict['eur']['rate']
else:
    cash['usd'] = r_dict['usd']['rate']
    cash['eur'] = r_dict['eur']['rate']
    
# 4 Read the currency to exchange for and the amount of money.
wanted_currency = input().lower()
cash = check_cash(cash, r_dict, wanted_currency)

while wanted_currency != '':
    wanted_currency = input().lower()
    if wanted_currency != '':
        cash = check_cash(cash, r_dict, wanted_currency)
