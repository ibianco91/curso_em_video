v = int(input('Qual o valor a ser sacado? R$'))
t=v
c=50
tc=0
while True:
    if t >=c:
        t -= c
        tc +=1
    else:
        if tc > 0:
            print(f'{tc} cedulas de R${c}')
        if c == 50:
            c =20
        elif c == 20:
            c = 10
        elif c ==10:
            c = 1
        tc = 0
        if t ==0:
            break
