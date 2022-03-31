from random import shuffle
from time import sleep
while True:
    # MENU DE OPÇÕES
    print('ESCOLHA UM OPÇÃO PARA FORMA A ESCALA')
    print('''   [ 1 ] CULTO DE DOMINGO
   [ 2 ] BATISMO
   [ 3 ] RETIRO
   [ 4 ] PARA SAIR DO PROGRAMA''')
    opçao = int(input('Qual tipo de escala você deseja? '))
    if opçao == 1: # CULTO DE DOMINGO
        print('-==-'*20)
        p1 = str(input('Nome: ')).strip().title()
        p2 = str(input('Nome: ')).strip().title()
        p3 = str(input('Nome: ')).strip().title()
        responsavel = str(input('Responsável: ')).strip().title()
        print('-==--==--==--==--==--==--== ESCALA PARA DOMINGO --==--==--==--==--==--==--==-')
        lista = [p1, p2, p3]
        shuffle(lista)
        print('- Stories: {}'.format(lista[0]))
        print('- Live: {}'.format(lista[1]))
        print('- Foto: {}'.format(lista[2]))
        print('Responsável: {}'.format(responsavel))
        print('QUEM NÃO PUDER CUMPRIR POR FAVOR, ME AVISE!!!!!')
        print('-==-'*20)
    elif opçao == 2: # BATISMO
        print('-==--==--==--==--==--==--== ESCALA PARA O BATISMO --==--==--==--==--==--==--==-')
        p1 = str(input('Nome: ')).strip().title()
        p2 = str(input('Nome: ')).strip().title()
        p3 = str(input('Nome: ')).strip().title()
        p4 = str(input('Nome: ')).strip().title()
        p5 = str(input('Nome: ')).strip().title()
        p6 = str(input('Nome: ')).strip().title()
        responsavel = str(input('Responsável: ')).strip().title()
        print('-==-'*20)
        lista = [p1, p2, p3, p4, p5, p6]
        shuffle(lista)
        print('- Gravação: {}, {} e {}'.format(lista[0], lista[1], lista[2]))
        print('- Stories: {}'.format(lista[3]))
        print('- Foto: {} e {}'.format(lista[4], lista[5]))
        print('Responsável: {}'.format(responsavel))
        print('QUEM NÃO PUDER CUMPRIR POR FAVOR, ME AVISE!!!!!')
        print('-==-'*20)
    elif opçao == 3: # RETIRO
        print('-==--==--==--==--==--==--== ESCALA PARA O RETIRO --==--==--==--==--==--==--==-')
        p1 = str(input('Nome: ')).strip().title()
        p2 = str(input('Nome: ')).strip().title()
        responsavel = str(input('Responsável: ')).strip().title()
        print('-==-'*20)
        lista = [p1, p2]
        shuffle(lista)
        print('- Gravação: {}'.format(lista[0]))
        print('- Foto: {}'.format(lista[1]))
        print('Responsável: {}'.format(responsavel))
        print('QUEM NÃO PUDER CUMPRIR POR FAVOR, ME AVISE!!!!!')
        print('-==-'*20)
    elif opçao == 4:
        print('-==-'*20)
        print('Finalizando....')
        sleep(2)
        break
    else:
        print('-==-'*20)
        print('Opção Inválida. Tente Novamente!')
        print('-==-'*20)
print('Programa finalizado. Volte sempre!')