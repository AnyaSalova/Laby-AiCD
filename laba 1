# -Шеснадцатиричные числа, не превышающие 102410 расположенные в порядке убывания. Для каждой такой последовательности максимальное число вывести прописью.


b = 0
with open('input.txt', 'r') as f:
    s = f.read(1024)
    if not s:
        print('the file is empty')
        b = 1
    while s:
        n = s.split()
        #print(n)
        a = -1
        L = []
        for i in n:
            try:
                if "'" in i or '"' in i:
                    i = i[1:-1]
                u = str(int(i, 16))
            except ValueError:
                #print('does not satisfy the condition')
                continue
            if a < int(i, 16):
                L.append(i)
            a = int(i, 16)
        s = f.read(1024)
    if not b:
        print('decision:', *L)
f.close()
