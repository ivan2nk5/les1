class human:
    height = 170
    gladness = 0

class student(human):
    gladness = 40

class worked(human):
    gladness = 60

nick = student()
ann  = worked()

print(nick.height)
print(ann.height)
print(nick.gladness)
print(ann.gladness)

class grandPa:
    height = 170
    gladness  = 90
    age= 70

class parent(grandPa):
    age = 30

class Child(parent):
    height =  100

    def __init__(self):
        print(self.height)
        print(self.gladness)
        print(self.age)


ch = Child()

class hello_word:
    hello  = "hello"
    _hello  = "hello"
    __hello = "hello"

    def __init__(self):
        self.word =  "word"
        self._word = "_word"
        self.__word = "__word"


    def printer(self):
        print(self.hello + self.word)
        print(self._hello + self._word)
        print(self.__hello + self.__word)

class test(hello_word):
    def test_print(self):
        print(self.hello + self.word)
        print(self._hello + self._word)
        #print(self.__hello + self.__word)

hello = hello_word()
hello.printer()
t = test()
t.test_print()
print("1")

class class1:
    def __init__(self):
        print("hello")

class class2(class1):

    def __init__(self):
        super().__init__()
        print("word")

x = class2()
print()
class class1:
    var = 20
    def __init__(self):
        self.var = 10

class class2(class1):

    def __init__(self):
        print(self.var)#=20
        super().__init__()#=10
        print(self.var)#=20
        print(super().var)#class1 = super = 10


x = class2()

class computer:
    def __init__(self,  model, *args , **kwargs):
        super().__init__(*args,**kwargs)
        self.memoery = 128

    def cal(self):

        print("calculating")

class display:
    def __init__(self,*args ,**kwargs):
        super().__init__(*args,**kwargs)
        self.resolution = "4k"
    def display(self):
        print("i show the image on scren")

class smartPhone(display,computer):


    def info (self):
        print(self.model)
        print(self.memoery)
        print(self.resolution)

iphone  = smartPhone(model="x2232")
iphone.display()
iphone.cal()
iphone.info()

