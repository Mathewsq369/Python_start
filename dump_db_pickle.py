import pickle
dbfile = open('accounts-pickle', 'rb')
db = pickle.load(dbfile)
for key in db:
    print(key, '=>\n ', db[key])
    print(db['sue']['fname'])