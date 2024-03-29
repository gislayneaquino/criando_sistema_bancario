saldo = 0
extrato = ''
limite_saque = 500
QUANT_SAQUES = 3
cont_saque = 0

print('='*45)
print('Caixa Eletrônico'.center(45))
print('='*45)
while True:
    print('''Operações Disponíveis:
[ 1 ] Depósito
[ 2 ] Saque
[ 3 ] Extrato''')
    opc = int(input('Digite a operação desejada: '))
    print('_' * 45)
    if opc == 1:
        print('Depósito'.center(45))
        dep = float(input('Valor: R$ '))
        saldo += dep
        extrato += (f'-> Depósito no valor de R$ {dep:.2f}\n'.replace('.', ','))
    if opc == 2:
        print('Saque'.center(45))
        saq = float(input('Valor: R$ '))
        if saq > saldo:
            print(f'Operação indisponível! Saldo Atual de R$ {saldo:.2f}.'.replace('.',','))
        elif saq > limite_saque:
            print(f'Operação Indisponível! \nValor excede o limite de R$ {limite_saque:.2f} por saque'.replace('.', ','))
        elif cont_saque >= QUANT_SAQUES:
            print(f'Operação indisponível! \nVocê atingiu o limite de {QUANT_SAQUES} saques diários.')
        elif saq > 0:
            saldo -= saq
            cont_saque += 1
            extrato += (f'-> Saque no valor de R$ {saq:.2f}\n'.replace('.', ','))
        else:
            print('Inválido!')
    if opc == 3:
        print('Extrato'.center(45))
        if extrato == '':
            print('Não foram realizadas movimentações.')
        print(f'''{extrato}
Saldo Atual R$ {saldo:.2f}'''.replace('.', ','))
    print('_'*45)
    print('''Deseja realizar uma nova operação?
[ 1 ] Sim
[ 2 ] Não''')
    resp = int(input('Opção desejada: '))
    print('_' * 45)
    if resp == 2:
        break
    else:
        continue
print('Finalizado'.center(45))
print('='*45)
