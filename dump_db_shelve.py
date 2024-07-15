import shelve
db = shelve.open('accounts-shelve')
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['lname'])
db.close()