#initialize data to be stored
#records
bob = {'fname':'Bob', 'lname':'Smith', 'age': 42, 'balance': 30000, 'job': 'dev'}
sue = {'fname':'Sue', 'lname':'Jones', 'age': 45, 'balance': 40000, 'job': 'hdw'}
tom = {'fname':'Tom', 'lname':'Doe','age': 50, 'balance': 0, 'job': None}

#database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__': #when run as a script
    for key in db:
        print(key, '=>\n ', db[key])