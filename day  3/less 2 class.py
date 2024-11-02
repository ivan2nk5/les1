class human:
    height = 170
    gladness = 22

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