def add_dollar(dollar):
    money=dollar*15141.75
    print('Rp',money)

def add_idr(idr):
    money=idr*0.000066
    print('$',money)

while True:
    j=input('USD or IDR? ')
    if j == 'USD':
        f=float(input('How many USD? '))
        add_dollar(f)
    elif j == 'IDR':
        k=float(input('How many IDR? '))
        add_idr(k)
    else:
        break