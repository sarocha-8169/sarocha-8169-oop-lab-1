import csv
from functools import reduce
with open ("numbers.csv","w",newline='') as fw:
    w = csv.writer(fw)
    w.writerow([2,4,6])
    w.writerow([3,7,5])
    w.writerow([8,9,7])

with open ("numbers.csv") as fw, open("numbers2.csv", "w") as file:
    rows = csv.reader(fw)
    file = csv.writer(file)
    for row in rows:
        row.reverse()
        row_ints = map(int, row)
        avg = reduce(lambda a,b: a+b ,row_ints)/ len(row) 
        print(f"{row[0].strip()},{row[1].strip()},{row[2].strip()},{avg}")
        file.writerow([row[0], row[1], row[2], avg])