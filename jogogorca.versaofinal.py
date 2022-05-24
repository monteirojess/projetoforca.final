from random import choice
print('''
    BEM VINDO (A) AO JOGO DA FORCA !
    O objetivo deste jogo é descobrir uma palavra adivinhando as letras que ela possui. 
    A cada rodada, os jogadores irão simultaneamente escolher uma letra que suspeitem fazer parte da palavra. 
    Caso a palavra contenha esta letra, será mostrado em que posição(ões) ela está. Ao contrário, o jogador será enforcado.
    Você tem 6 chances.
    BOA SORTE !

==== MENU: ====
[a] - Alimentos
[l] - Lugares
[o] - Objetos
''')
alimentos = ['JABOTICABA', 'PINHA', 'MELANCIA', 'MANGA', 'GOIABA']
lugares = ['GRAMADO', 'PARATI', 'SALVADOR', 'BANANEIRAS', 'MEXICO']
objetos = ['TECLADO', 'POLTRONA', 'QUADRO', 'TAPETE', 'TALHER']
usuario = (input('DIGITE A OPÇÃO DESEJADA:'.upper()))
if usuario == 'a':
    sorteio_alimentos = choice(alimentos)
    qtd_caracteres = len(sorteio_alimentos)
    gabarito = [''] * qtd_caracteres
    print('A palavra é:{}'.format(gabarito))
    for i in range(6):
        usuario = input('Digite uma letra ou palavra:')
        usuario = usuario.upper()
        if len(usuario) > 1 and usuario == sorteio_alimentos:
            print(('PARABÉNS, você ganhou. A palavra era {} !'.format(sorteio_alimentos)))
            break
        elif usuario in sorteio_alimentos:
            for x in range(len(sorteio_alimentos)):
              if (sorteio_alimentos[x]) == usuario:
                  gabarito[x] = usuario
            print(gabarito)
        else:
            print('Letra ou palavra não encontrada. Tente novamente!')
if usuario == 'l':
    sorteio_lugares = choice(lugares)
    qtd_caracteres = len(sorteio_lugares)
    gabarito = [''] * qtd_caracteres
    print('A palavra é:{}'.format(gabarito))
    for i in range(6):
        usuario = input('Digite uma letra ou palavra:')
        usuario = usuario.upper()
        if len(usuario) > 1 and usuario == sorteio_lugares:
            print(('PARABÉNS, você ganhou. A palavra era {} !'.format(sorteio_lugares)))
            break
        elif usuario in sorteio_lugares:
            for x in range(len(sorteio_lugares)):
              if (sorteio_lugares[x]) == usuario:
                  gabarito[x] = usuario
            print(gabarito)
        else:
            print('Letra ou palavra não encontrada. Tente novamente!')
if usuario == 'o':
    sorteio_objetos = choice(objetos)
    qtd_caracteres = len(sorteio_objetos)
    gabarito = [''] * qtd_caracteres
    print('A palavra é:{}'.format(gabarito))
    for i in range(6):
        usuario = input('Digite uma letra ou palavra:')
        usuario = usuario.upper()
        if len(usuario) > 1 and usuario == sorteio_objetos:
            print(('PARABÉNS, você ganhou. A palavra era {} !'.format(sorteio_objetos)))
            break
        elif usuario in sorteio_objetos:
            for x in range(len(sorteio_objetos)):
              if (sorteio_objetos[x]) == usuario:
                  gabarito[x] = usuario
            print(gabarito)
        else:
            print('Letra ou palavra não encontrada. Tente novamente!')


