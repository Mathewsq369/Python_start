import shelve
db = shelve.open('accounts-shelve')
sue = db['sue'] #fetch sue
sue['balance'] *= 1.50
db['sue'] = sue #update sue
#db['mat'] = mat     add a new record
db.close()