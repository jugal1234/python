sum = 0
for i in range(2):
    a,b,c = input().split()
    a = int(a)
    b = float(b)
    c  = float(c)
    sum = sum + c*b
print("VALOR A PAGAR: R$ {:.2f}".format(sum))
