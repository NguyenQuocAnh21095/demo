#nhap n
#in ra cac so chan <=n
n = 20
for i in range(n+1):
  if (i % 2 != 0 ):
    continue
  print(i, end=' ')
