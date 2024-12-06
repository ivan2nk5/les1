
#1
name = input("Ваше ім'я :")

age = int(input("ваш вiк :"))

print(f"Привіт {name}, тобі {age}!")
#2
if age >= 18:
    print("дозволено")
else:
    print("заборенено")
#3
import random
num = random.randint(1, 10)
while True:
    y_num = int(input("вгадай число"))
    if num > y_num:
        print('число бiльше')
    elif num < y_num:
        print("число меньше")
    else:
        print(f"так число {num}")
        break

#4
while True:
    y_num1 = int(input("вiд число 1: "))
    y_num2 = int(input("до число 2: "))
    if  y_num1 > y_num2:
        pass
    else:
        break
while True:
    if y_num1 == y_num2:
        print(y_num1)
        print("готово")
        break
    else:
        print(y_num1)
        y_num1 += 1



score = int(input("кількість балів"))


if score < 0 or score > 100:
    pass
elif score >= 90:
    print("Ваша оцінка: Відмінно")
elif score >= 75:
    print("Ваша оцінка: Дуже добре")
elif score >= 60:
    print("Ваша оцінка: Добре")
elif score >= 50:
    print("Ваша оцінка: Задовільно")
else:
    print("Ваша оцінка: Незадовільно")





