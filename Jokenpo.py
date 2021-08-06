# fazer um jogo programa que simula um jogo de "pedra, papel e tesoura"
# entre você e a máquina
# retorna quem é o vencedor da rodada
import random
lista = ('pedra','papel','tesoura')
npc = lista[random.randint(0,2)]
player = input('pedra papel ou tesoura?: ')
print('A jogada do NPC foi: {}'.format(npc))
if player == npc:
    print('sua jogada:', player)
    print('jogada npc:', npc)  
    print('Empate') 
elif player == 'pedra':
    if npc == 'papel':
        print('Você perdeu')
    else:
        print('Você ganhou')
elif player == 'papel':
    if npc == 'pedra':
        print('Você ganhou')
    else:
        print('Você perdeu')
elif player == 'tesoura':
    if npc == 'papel':
        print('Você ganhou')
    else:
        print('Você perdeu')
else:
    print('Há algum erro de digitação em sua jogada')
 

