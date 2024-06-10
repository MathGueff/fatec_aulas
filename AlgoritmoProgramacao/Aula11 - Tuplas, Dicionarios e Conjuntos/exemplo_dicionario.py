filmes = {
    'avatar':2009,
    'titanic':1997,
    'starwars':2015,
    'harry-potter':2014,
    'avengers':2012
}

# fromkeys
filmes_novachave = filmes.fromkeys(filmes)
print(f"Criando um dicionário com valores None e chaves iguais ao outro dic:\n {filmes_novachave}")
filmes_novachave = filmes.fromkeys(filmes, 'bilionário')
print(f"Criando um dicionário com valores especificados e chaves iguais ao outro dic:\n {filmes_novachave}")

print("=================")

#get
print(f"Procurando Frozen: -> {filmes.get('frozen')}") #procura frozen mas não acha
print(f"Procurando Frozen (mas personalizando): -> {filmes.get('frozen', 'não deu!')}") #procura frozen, não acha e adiciona ao dicionário
print(filmes.get('avatar')) #procura avatar, acha e diz o valor

print("=================")

#items
print(f"O dicionário usando .items ->\n  {filmes.items()}")
print("---")
# keys
print(f"O dicionário usando .keys ->\n  {filmes.keys()}")
print("---")
# values
print(f"O dicionário usando .value ->\n  {filmes.values()}")
print("---")
# update
filmes.update({"frozen":2013})
print(f"O dicionário usando .update ->\n {filmes}")

print("=================")

for chave, valor in filmes.items():
    print(f"Eu assisti ao filme {chave}, lançado em {valor}")