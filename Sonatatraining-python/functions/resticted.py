from leave import Leave
class RestrictedLeave(Leave):
    def __init__(self,employeeid,name,LeaveBalance,DateofBirth):
        super().__init__(employeeid, name, LeaveBalance)
        self.dob=DateofBirth
    def applyLeave(self):
        return self.name,self.dob
