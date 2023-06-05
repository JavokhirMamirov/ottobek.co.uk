n = int(input('n = '))
a = []
b = []
for i in range(n):
    x = input(f'a{i+1} = ')
    a.append(x)

for i in range(n):
    x = input(f'b{i+1} = ')
    b.append(x)

is_like = True
for k in a:
    if k in b:
        continue
    else:
        is_like = False

if is_like:
    print("ushbu massiv o'xshash")
else:
    print("ushbu massiv o'xshash emas")
