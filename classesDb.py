class User:
    def __init__(self, fname, lname, email, accountNo, balance):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.balance = balance
        self.accountNo = accountNo

    def __str__(self):
        return ('<%s => %s>' % (self.lname,self.accountNo))