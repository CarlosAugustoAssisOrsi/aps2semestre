import random


def cripto(crip):

    frase = ''

    for letra in crip:

        seila = str(random.choice(
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ))

        if letra in 'Aa':
            frase += seila
        elif letra in 'Ee':
            frase += seila
        elif letra in 'Ii':
            frase += seila
        elif letra in 'Oo':
            frase += seila
        elif letra in 'Uu':
            frase += seila
        elif letra in 'Bb':
            frase += seila
        elif letra in 'Cc':
            frase += seila
        elif letra in 'Dd':
            frase += seila
        elif letra in 'Ff':
            frase += seila
        elif letra in 'Gg':
            frase += seila
        elif letra in 'Hh':
            frase += seila
        elif letra in 'Jj':
            frase += seila
        elif letra in 'kK':
            frase += seila
        elif letra in 'Ll':
            frase += seila
        elif letra in 'Mm':
            frase += seila
        elif letra in 'Nn':
            frase += seila
        elif letra in 'Pp':
            frase += seila
        elif letra in 'Qq':
            frase += seila
        elif letra in 'Rr':
            frase += seila
        elif letra in 'Ss':
            frase += seila
        elif letra in 'Tt':
            frase += seila
        elif letra in 'Vv':
            frase += seila
        elif letra in 'Ww':
            frase += seila
        elif letra in 'Xx':
            frase += seila
        elif letra in 'Yy':
            frase += seila
        elif letra in 'Zz':
            frase += seila
        elif letra in ' ':
            frase += seila
        elif letra in ',':
            frase += seila
        else:
            kkk = None
    return str(frase)


pcrip = input('Qual a frase que deseja criptografar ? : ')
ciptografado = cripto(pcrip)
print(ciptografado)
quer = input('Voce deseja ver a solução da criptografia? (S/N): ').upper()

if quer == 'S':
    print(pcrip)
    print(ciptografado)
    n1, n2 = 0, 0
    for qq in pcrip:
        print(pcrip[n1])
        print(ciptografado[n2])
        n1 += 1
        n2 += 1
    print('Fim do programa')
else:
    print('Fim do programa')
