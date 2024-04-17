print('Programa para Censo por Idade')
menor = 0
media = 0
maior = 0
idade = 'inicial'


while idade != 'SAIR':
    idade = input('Digite a idade (ou digite SAIR para terminar):')
    if idade == 'SAIR':
        break
    censo = int(idade)
    if censo <= 25:
        menor += 1
    else:
        if censo <= 60:
            media += 1
        else:
            maior += 1


print('Existem {menor} pessoas com idade entre 0 e 25 anos; \nExistem {media} pessoas com idade entre 25 e 60 anos e\nExistem {maior} pessoas com idade acima de 60 anos'.format(menor=menor, media=media, maior=maior))