"""
Autor:
- Joe Martins de Pontes

Pré-diagnóstico com base nos valores de glicemia coletados quando o paciente está em jejum, pós-sobrecarga
e glicemia casual.

O programa é capaz de dizer se o paciente está com a Glicose Normal, Glicose Diminuída ou Apresentar o diagnóstico de
Diabetes Mellitus.

É ressaltado aqui que o resultado do programa não é um diagnóstico definitivo e suas respostas devem ser analisadas
por um profissional da área.
"""

from sklearn import tree


print(" ----------------------------------- \n"
      " Pré-diagnóstico Diabetes Mellitus \n"
      " ----------------------------------- \n")

print("#===================================================================#\n"
      "# Pré-diagnóstico com base nos valores de glicemia coletados quando #\n"
      "# o paciente está em jejum, pós-sobrecarga, e glicemia casual.      #\n"
      "#===================================================================#\n\n")

dados = [[90, 120, 98], [82, 100, 95], [70, 85, 77], [60, 82, 70], [85, 112, 100], [58, 94, 79], [52, 68, 59],
         [115, 157, 90], [120, 142, 60], [128, 191, 86], [109, 179, 81], [111, 169, 107], [119, 171, 77], [116, 149, 99],
         [129, 202, 261], [156, 223, 241], [128, 255, 272], [162, 211, 253], [132, 247, 268], [191, 222, 222], [208, 251, 243]]

# Normal = 0 | Tolerância diminuída = 1 | Diabetes mellitus = 2
labels = [0, 0, 0, 0, 0, 0, 0,
          1, 1, 1, 1, 1, 1, 1,
          2, 2, 2, 2, 2, 2, 2]      # Número de classes

classificador = tree.DecisionTreeClassifier()     # Utilizando o módulo tree para fazer a classificação

classificador.fit(dados, labels)      # Criando as decisões de acordo com os dados e labels


def diagnosticar():
    global consultar_novamente
    jejum, sobrecarga, casual = 0, 0, 0

    try:
        jejum = float(input("> [Em Jejum] < \nDigite quantos mg/dL está sua glicemia: "))
        sobrecarga = float(input("\n\n> [Pós-Sobrecarga] < \nDigite quantos mg/dL está sua glicemia: "))
        casual = float(input("\n\n> [Glicemia Casual] < \nDigite quantos mg/dL está sua glicemia: "))
    except ValueError:
        print('\n>>>> O valor deve ser apenas em números! <<<<')
        quit()

    diagnostico = classificador.predict([[jejum, sobrecarga, casual]])

    print('-------------------------------------------------------')

    if diagnostico == 0:
        print(f'\n=====> Glicemia normal\n'
              f'\nSeus dados de glicemia:\nJejum = {jejum}\nPós-Sobrecarga = {sobrecarga}\nCasual = {casual}\n')
    elif diagnostico == 1:
        print(f'\n=====> Tolerância a glicose diminuída\n'
              f'Recomendável procurar por um especialista para análise do resultado\n'
              f'\nSeus dados de glicemia:\nJejum = {jejum}\nPós-Sobrecarga = {sobrecarga}\nCasual = {casual}\n')
    else:
        print(f'\n=====> Diabetes Mellitus\n'
              f'Recomendável procurar por um especialista para análise do resultado\n'
              f'\nSeus dados de glicemia:\nJejum = {jejum}\nPós-Sobrecarga = {sobrecarga}\nCasual = {casual}\n')

    print('-------------------------------------------------------')
    print("\n* ===> Este programa foi feito apenas para calcular a probabilidade de alguma possível alteração na "
          "glicemia do usuário.\nO resultado exibido aqui NÃO é um diagnóstico definitivo e suas informações devem "
          "ser analisadas por um profissional da área. <=== *\n\n")

    try:
        consultar_novamente = int(input('Digite 0 para sair ou 1 para realizar outra consulta: '))
    except ValueError:
        quit()

    if consultar_novamente == 1:
        diagnosticar()


diagnosticar()
