from initdata import db
import pickle
dbfile = open('accounts-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()