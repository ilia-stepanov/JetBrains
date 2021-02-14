from math import ceil, log, floor
import argparse

parser = argparse.ArgumentParser()


parser.add_argument("-a1", "--type", choices=["annuity", "diff"])
parser.add_argument("-a2", "--payment", type=float)
parser.add_argument("-a3", "--principal", type=float)
parser.add_argument("-a4", "--periods", type=int)
parser.add_argument("-a5", "--interest", type=float)


args = parser.parse_args()
if args.type == 'annuity':
    if args.principal != None and args.payment != None and args.interest != None and args.periods == None:
        i = args.interest / 12 / 100
        b = args.payment / (args.payment - i * args.principal)
        n = ceil(log(b, 1 + i))
        y = n // 12  #year
        m = n % 12  #month
        o = round(args.payment * n - args.principal)
        
        
        if m == 0:
            print('\nIt will take %s years to repay this loan!' % y)
            
        else:
            print('\nIt will take %s years and %s months to repay this loan!' % (y, m))
        print('Overpayment = %s' % o)
            
            
    elif args.principal != None and args.payment == None and args.interest != None and args.periods != None:
        i = args.interest / 12 / 100
        a = ceil(args.principal * ((i * (1 + i)**args.periods) / ((1 + i)**args.periods - 1)))
        o = round(a * args.periods - args.principal)
        
        print('\nYour annuity payment = %s!' % a)
        print('Overpayment = %s' % o)
    
    
    elif args.principal == None and args.payment != None and args.interest != None and args.periods != None:
        i = args.interest / 12 / 100
        p = floor(args.payment / ((i * (1 + i)**args.periods) / ((1 + i)**args.periods - 1)))
        o = ceil(args.payment * args.periods - p)
        
        print('\nYour loan principal = %s!' % p)
        print('Overpayment = %s' % o)
    else:
        print('Incorrect parameters.')
        
elif args.type == 'diff':
    if args.principal != None and args.payment == None and args.interest != None and args.periods != None:
        i = args.interest / 12 / 100
        pp = 0
        for j in range(1, args.periods + 1):
            a = ceil((args.principal / args.periods) + i * (args.principal - (args.principal * (j - 1)) / args.periods))
            pp += a
            print('Month %s: payment is %s' % (j, a))
        
        o = ceil(pp - args.principal)
        print('Overpayment = %s' % o)
    else:
        print('Incorrect parameters.')
