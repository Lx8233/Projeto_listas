lista = []


def lista_recebe(num_add):
    print('Que número "int" deseja adicionar?(Um por vez!):')
    num_add = int(input())
    num_add = num_add
    lista.append(num_add)


escolha = ''

while escolha == '':
    print('Deseja adicionar números?')
    escolha = str(input('Y/n: '))
    escolha = escolha.upper()
    if escolha == 'Y':
        print('Total de números que vai adicionar: ')
        quantidade_num = int(input())
        for numero in range(quantidade_num):
            lista_recebe('')
        print(lista)
    elif escolha == 'N':
        print('Saindo...')
        break
    else:
        print('Erro! Reiniciando...')
        escolha = ''
print('Deseja organizar os números em ordem crescente ou decrescente?')
ordem = str(input('Y/n: '))
ordem = ordem.upper()
tipo_ordem = str(input('C para crescente | D para decrescente: '))
tipo_ordem = tipo_ordem.upper()

if ordem == 'Y':
    if tipo_ordem == 'C':
        lista.sort()
        print(lista)
    elif tipo_ordem == 'D':
        lista.sort(reverse=True)
        print(lista)
elif ordem == 'N':
    print('Certo, Finalizando...')
else:
    print("Comando não reconhecido, Finalizando!...")
