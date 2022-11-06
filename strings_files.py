import string
import sys


print('''foo 
bar''')  # foo / bar


print('What do you think '
      'about this game?')


print(r'\tell me')  # указываем что это не экранизация а нужная строка

#urf-8/16/32, ucs-2/4 - в python 3+ кодировка выбирается в завимимости от символов, динамически
print(list(map(ord, 'hello')))  # [104, 101, 108, 108, 111] - UCS-1
print(list(map(ord, 'привет')))  # [1087, 1088, 1080, 1074, 1077, 1090] - UCS-2
print(ord(' '))  # 32

var_h = '\u0068'
var_h1 = '\U00000068'
print(var_h, ord(var_h))  # h 104
print(var_h1, ord(var_h1))  # h 104

#  символ юникода по его коду
print(chr(0x68), chr(1087))  # h п
print(ord('ё'))  # 1105 - сначала одинаковые значения кириллики, потом уникальные в конце, такие как ё
ch = '\N{LATIN SMALL LETTER SHARP S}'
print(ch, ch.upper())  # ß SS - немный и вправду заменяют на SS если нужно написать в верхнем регистре
print(ch.upper().lower())  # ss
#-----------------------------------------------------------------------------------------------------------------------









#-----------------------------------------------------------------------------------------------------------------------

s = 'foo bar'
print(s.capitalize())  # Foo bar
print(s.title())  # Foo Bar
print(s.upper())  # FOO BAR
print(s.title().swapcase())  # fOO bAR



# по умолчанию используется пробел
print(s.ljust(16, '~'))  # foo bar~~~~~~~~~
print(s.rjust(16, '~'))  # ~~~~~~~~~foo bar
print(s.center(16, '~'))  # ~~~~foo bar~~~~~ - firstly right added, then left
print(s.center(1, '~'))  # foo bar


s = ']>>]]>]>1>foo bar><['
print(' ff '.strip())  # по умолчанию удаляет пробелы
print(s.lstrip('>]'))  # 1>foo bar><[ - слева направо удаляет каждое вхождение любого из этих символов
print(s.rstrip('[<'))  # ]>>]]>]>1>foo bar>
print(s.strip('[]<>'))  # 1>foo bar - с обеих сторон. По умолчанию удаляет пробелы


s = 'foo-bar'
print(s.split('-'))  # ['foo', 'bar'] # по умолчанию разделяет по пробелу с права на лево
s = 'foo---bar'
print(s.split('-'))  # ['foo', '', '', 'bar']

s = 'foo-bar-baz'
print(s.partition('-'))  # ('foo', '-', 'bar-baz') - кортеж

filename = 'security.gov.ua.py'
print(filename.rsplit('.', 1))  # ['security.gov.ua', 'py'] - получили имя файла и расширение

s = 'foo-bar-baz'
print(s.partition('-'))  # ('foo', '-', 'bar-baz') - 3 э-та - до вхождения разделителя/разделитель/подстрока после
# вхождения разделителя

print(s.rpartition('-'))  # ('foo-bar', '-', 'baz')

# зачем partition если есть split?
s = 'foobar'
print(s.rsplit('-', 1))  # ['foobar'] - возвращает "сколько-то" элементов
print(s.partition('-'))  # ('foobar', '', '') - всегда возвращает 3 элемента


# abz join принимает что-то по чему можно проитерироваться и соединяет указанным разделителем
s = ', '.join(['foo', 'bar', 'baz'])
print(s)  # foo, bar, baz


print('foo' in 'ua-foobar')  # True
print('foo' not in 'ua-english')  # True
print('foobar'.startswith('foo'))  # True
print('foobar'.endswith('ar'))  # True


s = 'abracadabra'
print(s.find('ra'))  # 2 - индекс первого символа в указанной поиска строки
print(s.find('ra', 0, 4))  # 2 - нашло
print(s.find('ra', 0, 3))  # -1 - не нашло
print(s.index('ra', 0, 3))  # Ошибка если юзать index

print(s.count('o'))  # 2
print(s.count('a', 4, -2))  # 2 // найти а с 4 по -2 символ
# для поиска последних вхождений
print(s.rfind('ra'))  # 9
print(s.rindex('ra'))  # 9

print('-' * 15)  # ---------------

# abz replace

s = 'abracadabra'
print(s.replace('ra', '*'))  # ab*cadab*
print(s.replace('ra', '*', 1))  # ab*cadabra - только первое вхождение

translation_map = {ord('a'): '*', ord('b'): '?'}  # меняем сразу несколько значений
print(s.translate(translation_map))  # *?r*c*d*?r*


# abz предикаты - позволяет убедиться что строка относится к тому либо иному типу
print('100500'.isdigit())  # True
print('foo100500'.isalnum())  # True
print('footbar'.isalpha())  # True
print('footbar'.islower())  # True
print('Footbar'.istitle())  # True
print(' \t\n\r'.isspace())  # True

# abz сортировка sort
print(max('Privet'))  # v

# abz format строк - помнить это не нужно, но просто знать об этом - хорошо

s = '{} {}, how are you?'
print(s.format('Hello', 'Putin'))  # Hello Putin, how are you?

hi = 'hello'
name = 'nikita'
age = '25'
print(f'{hi}, {name}. I\'m %s' % age)  # hello, nikita. I'm 25

s = 'я строка'
print('{!s}'.format(s))  # я строка - для человека
print('{!r}'.format(s))  # 'я строка' - для откладки
# '\u044f \u0441\u0442\u0440\u043e\u043a\u0430'  чтобы не думать по кодировку, ибо она гарантировано ascii
print('{!a}'.format(s))

s = 'foo bar'
print('{:~^16}'.format(s))  # ~~~~foo bar~~~~~
print('int: {0:d} hex: {0:x} oct: {0:o} bin: {0:b}'.format(42))  # int: 42 hex: 2a oct: 52 bin: 101010
print('{!r:~^16}'.format(s))  # ~~~'foo bar'~~~~

print('{:+08.2f}'.format(-42.42))  # -0042.42 - после запятой указать 2 символа


# что если какой-то аргумент нужно использовать 2 раза?
print('{0},{1},{0}'.format('hello', 'kitty'))  # hello,kitty,hello
print('{say},{who},{say}'.format(say='hello', who='kitty'))  # hello,kitty,hello

point = 0, 10
print('x = {0[0]}, y = {0[1]}'.format(point))  # x = 0, y = 10. 0 - index of format's argument. [0] - index of argument
point = {'x': 0, 'y': 1}
print('x = {0[x]}, y = {0[y]}'.format(point))  # x = 0, y = 1
a = 1
print('${a}')


# abz ascii полезные константы
print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)  # 0123456789
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.whitespace)

#-----------------------------------------------------------------------------------------------------------------------





















#-----------------------------------------------------------------------------------------------------------------------
# abz файлы ввод вывод # https://youtu.be/7YIgaaaGpyA?list=PLlb7e2G7aSpTTNp7HBYzCBByaE1h54ruW&t=3745
handle = open('./1.txt', 'r')
print(handle.read(5))  # выводит 5 символов с файла
print(handle.readlines())  # ['\n', '4\n', '5\n', '6\n', '7\n', '8\n', '9\n'] # на практике почти не нужен

handle = open('./1.txt', 'a')
handle.write('15\n')

print(handle.fileno())  # 4 № файлового дескриптора
print(handle.tell())  # узнать на каком байте находишься
print(handle.seek(1))  # хз
handle.flush()  # сбрасываем буфер куда все копиться перед записанием в файл
handle.close()  # close вызывает flush
#-----------------------------------------------------------------------------------------------------------------------







#-----------------------------------------------------------------------------------------------------------------------
# abz потоки
# name = input('name: ')
print('hello', file=sys.stdout)  # hello
print('hello', file=sys.stderr)  # hello at the beginning. red color

# abz print

print(*range(5), sep='-')  # 0-1-2-3-4
print(*range(5), sep='-', end='\n--\n')  # 0-1-2-3-4 / --

handle = open('./1.txt', 'a')
print(*range(5), file=handle, flush=True)  # сразу записать
#-----------------------------------------------------------------------------------------------------------------------