import address from address
class Employee:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def getFullname(self):
        return self.firstname + ' ' +self.lastname
    def getinitials(self):
        return (self.firstname[0]+ self.lastname[0]).upper()



