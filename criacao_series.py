import pandas as pd

print('Criando uma instância de Series a partir de uma lista numérica.')

print('Criando uma instância de Series a partir de uma lista numérica.')
copa_do_mundo = pd.Series([1952, 1962, 1970, 1994, 2002])
print('Anos em que o Brasil foi campeão mundial de futebol')
print(f'{copa_do_mundo}')


s = pd.Series((1, 2, 3))
print('\nCriando uma série a partir de uma tupla')
print(s)
print(f'Tipo de variável  {type(s)}')


s = pd.Series({'a': 1, 'b': 2, 'c': 3})  # Dicionário usa dois pontos :
print('\nCriando uma série a partir de um dicionário.')
print(s)
print(f'Tipo da variável {type(s)}')


s = pd.Series(['Wes Mckinney', 'Criador da Pandas'], index=['Pessoa', 'Quem'])
print('\nCriando uma série a partir  de uma lista de  velores e outra de rótulos')
print(s)
print(f'Tipo de variável {type(s)}')
