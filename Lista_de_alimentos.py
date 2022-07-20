
def alimentos():
    return {'CARNES E OVOS' :[['ALMONDEGA', 51],['BIFE', 56],['CARNE DE PANELA', 21], ['BISTECA', 98], ['ALMONDEGA', 23],
           ['CARNE BOVINA GORDA', 63], ['CARNE MOIDA', 45], ['COXA DE FRANGO',27], ['FRANGO GRELHADO', 32],
           ['HAMBURGUER BOVINO', 30], ['HAMBURGUER FRANGO', 23], ['LINGUIÇA', 45], ['OMELETE', 40], ['OVO',23],
           ['STROGONOFF 3 COLHERES', 45]],

            'PEIXES':[['CAMARAO',40], ['FILE DE PEIXE', 64]],

            'GRÃOS':[['ARROZ', 10], ['ARROZ INTEGRAL', 10], ['AVEIA', 5], ['FEIJAO', 5], ['MANDIOCA', 10], ['PIPOCA', 20],
                     ['SUCRILHOS', 10],],

            'FRUTAS':[['ABACAXI', 10], ['BANANA MAÇA', 20], ['BANANA NANICA', 30], ['BANANA PRATA', 20], ['LARANJA', 3],
                      ['MAÇÃ', 25], ['MAMÃO', 10], ['MANGA', 5], ['MELANCIA', 10], ['SALADA DE FRUTA', 5], ['TANGERINA', 15],
                      ['TOMATE', 5]],

            'LEITES E IOGURTES':[['DANONINHO', 50], ['IOGURTE', 40], ['LEITE', 35], ['TODDYNHO', 55], ['YAKULT', 15]],

            'PAES E BOLACHAS':[['BISCOITO DE LEITE', 7], ['BISCOITO RECHEADO', 20], ['BISNAGUINHA', 20],
                                ['PÃO CASEIRO', 46], ['PÃO DE BATATA', 40], ['PÃO DE FORMA', 20], ['PÃO FRANCES', 40],
                                ['PÃO DE HAMBURGUER', 60], ['PÃO INTEGRAL', 20]],

            'BOLOS':[['BANANA', 45], ['MAÇÃ', 35], ['FORMIGUEIRO', 47]],

            'QUEIJOS':[['CATUPIRY', 20], ['CHEDDAR', 36], ['MORTADELA', 15], ['MUSSARELA', 20], ['PEITO DE PERU', 10],
                    ['BRANCO', 21], ['MINAS', 5], ['PRATO', 15], ['REQUEIJÃO', 20], ['CREME DE RICOTA', 10]],

            'BEBIDAS':[['ENERGETICO LATA', 32], ['CERVEJA', 40], ['CHOPP', 35], ['REFRIGERANTE', 23], ['SUCO', 35],
                       ['WISKEY', 30], ['VINHO', 40], ['VODKA', 30]],

            'DOCES':[['PICOLE', 20], ['BIS', 11], ['BRIGADEIRO', 14], ['CHOCOLATE BARRA', 40], ['DOCE DE LEITE', 30],
                     ['LEITE CONDENSADO', 15], ['PUDIM', 55], ['SORVETE', 55], ],

            'PIZZAS':[['CALABREZA', 100], ['FRANGO COM CATUPIRY', 85], ['MUSSARELA', 81], ['QUATRO QUEIJOS', 103]]

            }

def lista_grupos():
        print(f'GRUPO DE ALIMENTOS:\n{alimentos().keys()}')

def escolha_grupo():
        escolha = input(f'Insira o grupo de alimentos ingerido:  ').upper().strip()
        if escolha in 'CARNES E OVOS':
                return carnes_ovos()

        elif escolha in 'FRUTAS':
                return frutas()
        elif escolha in 'GRAOS':
                return graos()
        elif escolha in 'PEIXES':
                return peixes()
        elif escolha in 'LEITES E IOGURTES':
                return leites_iogurtes()
        elif escolha in 'PAES E BOLACHAS':
                return paes_bolachas()
        elif escolha in 'BOLOS':
                return bolos()
        elif escolha in 'QUEIJOS':
                return queijos()
        elif escolha in 'BEBIDAS':
                return bebidas()
        elif escolha in 'DOCES':
                return doces()             
        elif escolha in 'PIZZAS':
                return pizzas()

def carnes_ovos():
        print('Lista de alimentos:')
        for z, c in enumerate(alimentos()['CARNES E OVOS']):
            print(f'{z} ---- {alimentos()["CARNES E OVOS"][z]} ')
        print('')
        calorias = alimentos()['CARNES E OVOS'][escolha_alimento()][1] * quantidade_alimento()
        print('')
        print(f'voce ingeriu {calorias} calorias')
        return calorias

def frutas():
        print('Lista de Alimentos: ')
        for z, c in enumerate(alimentos()['FRUTAS']):
            print(f'{z} ---- {alimentos()["FRUTAS"][z]} ')
        calorias = alimentos()['FRUTAS'][escolha_alimento()][1] * quantidade_alimento()
        print('')
        print(f'voce ingeriu {calorias} calorias')
        return calorias

def graos():
        print('Lista de Alimentos: ')
        for z, c in enumerate(alimentos()['GRÃOS']):
            print(f'{z} ---- {alimentos()["GRÃOS"][z]} ')
        calorias = alimentos()['GRÃOS'][escolha_alimento()][1] * quantidade_alimento()
        print('')
        print(f'voce ingeriu {calorias} calorias')
        return calorias

def peixes():
        print('Lista de Alimentos: ')
        for z, c in enumerate(alimentos()['PEIXES']):
            print(f'{z} ---- {alimentos()["PEIXES"][z]} ')
        calorias = alimentos()['PEIXES'][escolha_alimento()][1] * quantidade_alimento()
        print('')
        print(f'voce ingeriu {calorias} calorias')
        return calorias

def leites_iogurtes():
        print('Lista de Alimentos: ')
        for z, c in enumerate(alimentos()['LEITES E IOGURTES']):
                print(f'{z} ---- {alimentos()["LEITES E IOGURTES"][z]} ')
        calorias = alimentos()['LEITES E IOGURTES'][escolha_alimento()][1] * quantidade_alimento()
        print('')
        print(f'voce ingeriu {calorias} calorias')
        return calorias

def paes_bolachas():
        print('Lista de Alimentos: ')
        for z, c in enumerate(alimentos()['PAES E BOLACHAS']):
                print(f'{z} ---- {alimentos()["PAES E BOLACHAS"][z]} ')
        calorias = alimentos()['PAES E BOLACHAS'][escolha_alimento()][1] * quantidade_alimento()
        print('')
        print(f'voce ingeriu {calorias} calorias')
        return calorias

def queijos():
        print('Lista de Alimentos: ')
        for z, c in enumerate(alimentos()['QUEIJOS']):
            print(f'{z} ---- {alimentos()["QUEIJOS"][z]} ')
        calorias = alimentos()['QUEIJOS'][escolha_alimento()][1] * quantidade_alimento()
        print('')
        print(f'voce ingeriu {calorias} calorias')
        return calorias

def bolos():
        print('Lista de Alimentos: ')
        for z, c in enumerate(alimentos()['BOLOS']):
            print(f'{z} ---- {alimentos()["BOLOS"][z]} ')
        calorias = alimentos()['BOLOS'][escolha_alimento()][1] * quantidade_alimento()
        print('')
        print(f'voce ingeriu {calorias} calorias')
        return calorias

def bebidas():
        print('Lista de Alimentos: ')
        for z, c in enumerate(alimentos()['BEBIDAS']):
            print(f'{z} ---- {alimentos()["BEBIDAS"][z]} ')
        calorias = alimentos()['BEBIDAS'][escolha_alimento()][1] * quantidade_alimento()
        print('')
        print(f'voce ingeriu {calorias} calorias')
        return calorias

def doces():
        print('Lista de Alimentos: ')
        for z, c in enumerate(alimentos()['DOCES']):
                print(f'{z} ---- {alimentos()["DOCES"][z]} ')
        calorias = alimentos()['DOCES'][escolha_alimento()][1] * quantidade_alimento()
        print('')
        print(f'voce ingeriu {calorias} calorias')
        return calorias

def pizzas():
        print('Lista de Alimentos: ')
        for z, c in enumerate(alimentos()['PIZZAS']):
            print(f'{z} ---- {alimentos()["PIZZAS"][z]} ')
        calorias = alimentos()['PIZZAS'][escolha_alimento()][1] * quantidade_alimento()
        print('')
        print(f'voce ingeriu {calorias} calorias')
        return calorias

def escolha_alimento():
        return int(input('Qual item da lista? '))

def quantidade_alimento():
        quantidade = int(input('Quantidade ?'))
        return quantidade

def calorias_ingeridas(funcao):
        return funcao
        
def continuar():
        continuar = input('Deseja continuar?[S/N]')
        return continuar

def horario_refeicao(total):
        refeicao = str(
            input('Qual foi a refeição? [CAFÉ/ALMOÇO/JANTA]')).upper().strip()
        if refeicao in 'CAFE':
                cafe(total)
        if refeicao in 'ALMOÇO':
                almoco(total)
        if refeicao in 'JANTA':
                janta(total)

def cafe(total):
        cafe = total
        print(f'O total de calorias ingeridas no café foi: {cafe}')

def almoco(total):
        almoco = total
        print(f'O total de calorias ingeridas no almoço foi: {almoco}')

def janta(total):
        janta = total
        print(f'O total de calorias ingeridas na jantoa foi: {janta}')



