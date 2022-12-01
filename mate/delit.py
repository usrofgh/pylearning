import csv
import time
with open("output_csv_full.csv") as file:
    csv_reader = csv.reader(file, delimiter=',')
    c = 0
    s = time.perf_counter()
    for row in csv_reader:
        c += 1
        if c % 10000 == 0:
            print(c)
    print(f'Processed {c} lines.')
    e = time.perf_counter()
    print('Elapsed: ', e - s, ' sec.')
    print(csv_reader.line_num)
