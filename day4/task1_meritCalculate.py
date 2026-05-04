class student:
    def __init__(self):
        self.name = ""
        self.matricmarks = 0.0
        self.fscmarks = 0.0
        self.ecatmarks = 0.0
        self.merit = 0.0
    def calculatemerit(self):
        merit=((0.25*self.matricmarks/1100)+(0.45*self.fscmarks/1100)+(0.3*self.ecatmarks/400))
        return merit*100
    
s=student()
s.name = input("enter name: ")
s.matricmarks = float(input("enter matric marks: "))
s.fscmarks = float(input("enter fsc marks: "))
s.ecatmarks = float(input("enter ecat marks: "))
print("merit: ",s.calculatemerit())