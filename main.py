import pandas as pd
#from enviaremail import enviar_email
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # opção, valor - Não ter maximo de colunas, exibir todas
    pd.set_option('display.max_columns', None)

    # Abre o CSV
    relatorio = pd.read_csv('relatorio.csv')

    # Converte em DataFrame
    df = pd.DataFrame(relatorio)

    # Conta qtd de linha do DataFrame
    total = len(df.index)

    # Conta qtd de tipo de ligações
    status = df['Status'].value_counts()

    # Exibir resultado
    print(f'Recebeu {total} ligações')
    print(f'Sendo elas: ')
    print(f'{status}')

    # Para converter e formatar
    df['Data'] = pd.to_datetime(df['Data'])

    # Para agrupar por hora
    horarios = df.groupby(pd.Grouper(key='Data', freq='H')).size().reset_index()

    # Para exibir somente hora, sem data e corrigir nome de coluna
    horarios = pd.DataFrame({
        "Hora": horarios['Data'].dt.time,
        "Qtd": horarios[0]
    })

    # Montar gráfico (astype: Converte object DataTime.time para String)
    x = horarios['Hora'].astype("|S")
    y = horarios['Qtd']
    plt.plot(x, y)
    plt.show()
    #enviar_email()
