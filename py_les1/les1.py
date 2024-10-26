
class student:
    amount_of_s = 0

    def __init__(self, age,heigt = 160,):
        self.age = age
        self.heigt  = heigt
        #self.name  = name
        student.amount_of_s += 1

    def h_b(self):
        self.age += 1
    def h_b10(self):
        self.age += 10

    def __str__(self):
        # return f"<student age  ={self.age}  height={self.heigt}>"






s1 = student(21,190)
s1.h_b()
s1.h_b()
s1.h_b()
print("s1","age",  s1.age,"heigt",s1.heigt)

s2 = student(25,166)
s2.h_b10()
print("s2","age",  s2.age,"heigt",s2.heigt)


s3 = student(24)
print("s3","age",  s3.age,"heigt", s3.heigt)

print(f"all students\n",student.amount_of_s)
print(s3)



class cir:
    def  __int__(self,radius):
        self.radius = radius

    def calc_area(self):
        return 3.14 * self.radius ** 2

cir_10 = cir(10)
print(cir_10.calc_area())

cir_3 = cir(10)
print(cir_3.calc_area())
