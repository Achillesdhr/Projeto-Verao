from time import sleep
import Lista_de_alimentos

calorias_totais = 0

while True:

    Lista_de_alimentos.lista_grupos()

    grupo = Lista_de_alimentos.escolha_grupo()

    calorias_totais += Lista_de_alimentos.calorias_ingeridas(grupo)

    if Lista_de_alimentos.continuar() in 'Nn':
        Lista_de_alimentos.horario_refeicao(calorias_totais)
        break
