import requests
import colorama
import inspect
inspect.isclass(colorama)

print(requests.__version__)
print(requests.__name__)

print("###########")
print(dir(colorama))

print(inspect.getsource(colorama.init))

print(inspect.getdoc(colorama.init))

for item in dir(__builtins__):#все функции и тд
    print(item)
print("version colorama",getattr(colorama, '__version__',))

print("\n metod")
for member in inspect.getmembers(colorama):
    print(member)
inspect.getdoc(colorama)
"""
version colorama 0.4.6
colorama отвечает за цвета текста стили курсив 
смена цвета Fore.RED,Fore.GREEN
metod
('AnsiToWin32', <class 'colorama.ansitowin32.AnsiToWin32'>)
('Back', <colorama.ansi.AnsiBack object at 0x00000225BC419E20>)
('Cursor', <colorama.ansi.AnsiCursor object at 0x00000225BC41A450>)
('Fore', <colorama.ansi.AnsiFore object at 0x00000225BC419DF0>)
('Style', <colorama.ansi.AnsiStyle object at 0x00000225BC39ADB0>)
"""