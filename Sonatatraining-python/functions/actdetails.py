class Account(Exception):
    def __init__(self,acccount_num,user_name,account_type,account_balance):
        self.act=acccount_num
        self.name=user_name
        self.type=account_type
        self.bal=account_balance
    def display(self):
        return self.act,self.name,self.type,self.bal


