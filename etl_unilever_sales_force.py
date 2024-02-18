import pandas

#1 LENDO BASE DE DADOS A PARTIR DA PLANILHA Atena 2.0 _ Tempos & Movimentos _ Prévia de Resultado.xlsx

# necessario alterar path de acordo com o repositorio de execucao, lembrando de inverter contrabarra(\) para barra(/)
path = 'C:/Users/frederick.barros/Documents/PROJETOS/UNILEVER/unilever_dados/bucket/inputs/'
file_name = 'Atena 2.0 _ Tempos & Movimentos _ Prévia de Resultado.xlsx'
sheet = 'Base Consolidada'

df = pandas.read_excel(path + file_name, sheet_name=sheet, index_col=1)

print(df)

