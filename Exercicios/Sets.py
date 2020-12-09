# Criando um set com elementos:
# Utiliza-se de chaves, entretanto não é um dicionário, visto que não possui chave nem um índice, possuindo apenas valores.

Set1 = {1, 2, 3, 4, 5}

# Criando um set vazio

Set2 = set()

# Pode ser utilizado para remover elementos duplicados de uma lista, visto que só pode conter elementos únicos. EX:
lista1 = [1, 2, 1, 1, 3, 4, 5, 6, 6, 6, 6, 6, 7, 8, 9, 'Luiz', 'Luiz']
l1 = set(lista1)
# print(l1)  # Saída: {1, 2, 3, 4, 5, 6, 7, 8, 9, 'Luiz'}

#####################################################################################################################

set1 = {1, 2, 3, 4, 5, 7}
set2 = {1, 2, 3, 4, 5, 6}

# ----------------------------------------------------------

# union ou |    //unir sets

set3 = set1 | set2
# print(set3)   # Saída: {1, 2, 3, 4, 5, 6, 7}

# ----------------------------------------------------------

# Intersection ou &     //Coleta apenas os elementos que estão nos dois sets.

set4 = set1 & set2
# print(set4)   # Saída: {1, 2, 3, 4, 5}

# ----------------------------------------------------------

# Difference ou -   //Coleta os elementos do set da esquerda que não estão no set da direita.

set5 = set1 - set2
# print(set5)   # Saída: {7}

# ----------------------------------------------------------

# Symmetric_difference ou ^     //Coleta elementos que estão nos dois sets mas não estão em ambos.

set6 = set1 ^ set2
# print(set6)   # Saída: {6, 7}
 
 