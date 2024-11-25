result = []
numbererror = 1
def divider(a, b):
    if a < b:
        raise ValueError
    if a > 100:
        raise IndexError
    return a/b
data = {10: 2, 20: 5, 12.3: 4, 18: 3, 25: 15, 8: 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
        numbererror += 1 #этап ошибки в словаре
    except ValueError:
        print(f"stage {numbererror} error ValueError plese try again")
    except IndexError:
        print(f"stage {numbererror} error IndexError plese try again")
    except ZeroDivisionError:
        print(f"stage {numbererror} error ZeroDivisionError plese try again")
print(result)

print("\n DONE")