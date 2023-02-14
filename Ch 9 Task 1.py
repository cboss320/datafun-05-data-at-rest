import sys 

sys.stdin
sys.stdout
sys.stderr

with open ('accounts.txt', mode='w') as accounts: 
    accounts.write('100 Jones 24.98\n')
    accounts.write('200 Doe 345.67\n')
    accounts.write('300 Williams 0.00\n')
    accounts.write('400 Stone -42.16\n')
    accounts.write('500 Rich 224.62\n')

with open('accounts.txt', mode='r') as accounts: 
    print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
    for record in accounts: 
        account, name, balance = record.split()
        print(f'{account:<10}{name:<10}{balance:>10}')

accounts = open('accounts.txt', 'r')
temp_file = open('temp_file.txt', 'w')

with accounts, temp_file: 
    for record in accounts: 
        account, name, balance = record.split()
        if account !='300':
            temp_file.write(record)
        else: 
                new_record = ' '.join([account, 'Williams', balance])
                temp_file.write(new_record + '\n')

import os 

os.remove('accounts.txt')
os.rename('temp_file.txt', 'accounts.txt')


accounts_dict = {'accounts': [
    {'account': 100, 'name': 'Jones', 'balance': 24.98}, 
    {'account': 200, 'name': 'Doe', 'balance': 345.67}]}

import json 

with open('accounts.json', 'w') as accounts:
    json.dump(accounts_dict, accounts)
    
with open ('accounts.json', 'r') as accounts: 
    accounts_json = json.load(accounts)
    accounts_json 

accounts_json['accounts']

accounts_json['accounts'][0]

accounts_json['accounts'][1]

with open('accounts.json', 'r') as accounts: 
    print(json.dumps(json.load(accounts), indent=4))

{
    "accounts": [
        {
            "account": 100, 
            "name": "Jones", 
            "balance": 24.98
        }, 
        {   
            "account": 200, 
            "name": "Doe", 
            "balance": 345.67
        }
    ]
}

value = int(input('Enter an integer: '))


#dividebyzero.py 
"""Simple exception handling example."""

while True: 
    # attempt to convert and divide values 
    try: 
        number1 = int(input('Enter numerator: '))
        number2 = int(input('Enter denominator: '))
        result = number1/number2 
    except ValueError: #tried to convert non-numeric value to int 
        print('You must enter two integers\n')
    except ZeroDivisionError: #demoinator was 0
        print('Attempted to divide by zero\n')
    else: #executes only if no exceptions occur 
        print(f'{number1:.3f} / {number2:.3f} = {result:.3f}')
        break #terminate the loop 

while True:

    try:
        print('try suite with no excpetions raised')
    except:
        print('this will not excute')
    else:
        print('else excutes because no exceptions in the try suite')
    finally:
        print('finally always executes')
        break #terminate the loop 

while True: 
    try: 
        print('try suite that raises an exception')
        int('hello')
        print('this will not excute')
    except ValueError: 
        print('a ValueError occurred')
    else: 
        print('else will not execute because an exception occurred')
    finally: 
        print('finally always executes')
        break #terminate the loop


while True: 
    try: 
        with open('gradez.txt', 'r') as accounts:
            print(f'{"ID":<3}{"Name":<7}{"Grade"}')
            for record in accounts: 
                student_id, name, grade = record.split()
                print(f'{student_id:<3}{name:<7}{grade}')
    except FileNotFoundError:
        print('The file name you specified does not exist')
        break #terminate the loop

def function1(): 
    function2()

def function2(): 
    raise Exception('An exception occurred')

import csv

with open ('accounts.csv', mode='w', newline= ' ') as accounts: 
    writer = csv.writer(accounts)
    writer.writerow([100, 'Jones', 24.98])
    writer.writerow([200, 'Doe', 345.67])
    writer.writerow([300, 'White', 0.00])
    writer.writerow([400, 'Stone', -42.16])
    writer.writerow([500, 'Rich', 224.62])

with open('accounts.csv', 'r', newline= '') as accounts: 
    print(f'{"Account":<10}{"Name":<10}{"Balance:>10"}')
    reader = csv.reader(accounts)
    for record in reader:
        account, name, balance = record 
        print(f'{account:<10}{name:<10}{balance:>10}')



