class Student:
    def __init__(self,student_id,student_name,__studentdept):
        self.id=student_id
        self.name=student_name
        self.dept=__studentdept

    def studentdetails(self):
        return self.id,self.name,self.dept

setattr(std,'student_class',10)
print(getattr(std,'student_class'))
print(hasattr(std,'student_class'))

delattr(std,'student_class')
print(hasattr(std,'student_class'))

setattr(std,'student_class',12)
print(getattr(std,'student_class'))
print(hasattr(std,'student_class'))

print(sd)
print(getattr(std,'student_class'))


