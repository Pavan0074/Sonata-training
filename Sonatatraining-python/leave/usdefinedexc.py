class lowbalance_exception:
    def __init__(self,message):
        self.msg=message
    def displayerror(self):
        print(self.msg)
