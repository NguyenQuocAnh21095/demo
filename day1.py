#nhap vao n
#tinh gt(n)
# gt(4) = 1*2*3*4 = 24
n = int(input('nhap n:'))
gt=1
for i in range(n): 
    gt = gt*i
print(gt)