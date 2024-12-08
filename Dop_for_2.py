a = int(input("Введите число a: "))
b = int(input("Введите число b (b > a): "))
c = int(input("Введите число c: "))
d = int(input("Введите число d (d > c): "))
print(end='\t')
for i in range(c, d+1):
    print(i, end='\t')

for j in range(a, b+1):
    print(end='\n')
    print(j, end='\t')


    for k in range(c, d+1):
        print(j * k, end='\t')

