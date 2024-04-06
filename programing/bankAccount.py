class BankAccount(object):
    def __init__(self,userName,Account):
        self.userName=userName
        self.Account=Account
        self.Balance=' '
    def setuserName(self,newuserName):
        self.userName=newuserName
    def getuserName(self):
        return self.userName
    def setAccount(self,newAccount):
        self.Account=newAccount
    def getAccount(self):
        return self.Account












    #     self.balance=newbalance
    #     if self.balance >= 0:
    #         outmoney = input("How much you want?")
    #         if outmoney >= 0 or outmony>newbalance:
    #             self.balance = self.balance - outmoney
    #         else:
    #             return("type a valid number")
    #     inmoney = input("Howe much you wan to save?")
    #     if inmoney >= 0:
    #         self.balance = self.balance + inmoney
    #         else:
    #     return("type a valid number")
    # else:
    #     return("type a valid number")









bank=BankAccount
print(bank)
print(bank.balance)






