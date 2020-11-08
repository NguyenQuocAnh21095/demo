#nhap n
#in ra tam giac vuong kich thuoc n
'''
*
* *
* * *
* * * *
* * * * *
       *
     * *
   * * *
 * * * *
'''
n = 5
#tam giac vuong ben phai
for i in range(n+1):
    print('  '*(n-i), '* '*i)
    #print('* '*(n-i))    

#tam giac vuong ben trai nguoc
for i in range(n+1):
    print('* '*(n-i))    

#tam giac deu
for i in range(n+1):
    print(' '*(n-i), '* '*i)

#tam giac deu nguoc
for i in range(n+1):
    print(' '*i, '* '*(n-i))

'''
for i in range(n+1):
    for j in range(i):
        print('* ', end='')
    print()
'''