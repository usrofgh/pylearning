# r — read. error if doesn't exist;
# w — writes data. overwrites if something exists there. Create new file if doesn't exist
# a — appends data, create if doesn't exist
# x — writes data,  returns an error if the file already exists
# t — is used only for textual files (text mode — we see the text);
# b — non text-files -  images, videos, etc. (binary mode — we see 0 and 1);
# r+w/b — t/w simultaneously


file = open("errors.txt")  # by default tr mode(text read). no difference between just r
# for avoiding system errors because of  large amount of computer memory because of forgottten closed file - close it,

print(file.read(10))  #  10:53 12/0 // red 10 symbols

print(file.tell())  # 10  // узнаем на каком символе сейчас
file.seek(60)  # пропускаем n символов
print(file.tell())  # 60

print(file.read())  # "min not found" // because of the code abot we missed 60 symbols and start reading from 60 to end
file.flush()  # сбрасываем буфер куда все копиться перед записанием в файл
print(file.fileno())  # номер файла потокового дескриптора
print(file.closed)  # Flasae closed file or not
file.close()  # закрываем файл  - вызывает flush
print(file.closed)  # True
# print(file.read())  # ValueError: I/O operation on closed file.


# readline() - return a line
# readlines() - returns a list where which element is a line
print("\n")

file = open("errors.txt")
print(file.readline())  # 10:53 12/09/2022 too many requests
print(file.readline())  # 21:17 13/09/2022 user admin not found // print after above line
print(file.readlines())  # [] - cause we read all lines
file.seek(0)  # переходим на начало файла
print(file.readlines())  # ['10:53 12/09/2022 too many requests\n', '21:17 13/09/2022 user admin not found']

# with help readline() we don't have any problem with memory in compression with read() which read all lines at time

# better use context manager
with open("errors_w.txt", "w") as file:
    # file.write(1/0)  # without context-manager i won't close the file after an error. You'll need to use
    # try/finally. Better use CM
    file.write("a")

