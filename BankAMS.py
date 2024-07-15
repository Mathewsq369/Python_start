import shelve
'''
db = shelve.open('accounts-shelve')

for obj in db:
    print(obj)

name1 = str(input("Input your first name: "))
name2 = str(input("Input your last name: "))
email_addr = str(input("Input your email address: "))

import random

account_number = random.randint(1000000,10000000)

db = shelve.open('accounts-shelve')
def check_account_number(account_number, database):
    if account_number in db:
        print(f"The account number {account_number} already exists! sign in instead?")
        return False
    else:
        db[account_number] = User(name1,name2,email_addr,account_number,0)
        db.close()
        print(f"Your account number is {account_number}")
        return True

#check_account_number(1234567, db)



class User:
    def __init__(self, fname, lname, email, accountNo, balance):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.balance = balance
        self.accountNo = accountNo

    def __str__(self):
        return ('<%s => %s>' % (self.lname,self.accountNo))
'''

def view_account_details():
    fieldnames = ('fname','lname', 'age', 'balance', 'job')
    maxfield = max(len(f) for f in fieldnames)
    db = shelve.open('accounts-shelve')

    while True:
        key = input('\nkey? => ')
        if not key: break
        try:
            record = db[key]
        except:
            print('No such key "%s"!' % key)
        else:
            for field in fieldnames:
                print(field.ljust(maxfield), '=>', db[key][field])

view_account_details()