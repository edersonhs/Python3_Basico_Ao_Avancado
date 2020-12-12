import json

with open('dicionario.json', 'r') as file:
    d1_json = file.read()   # Lê o arquivo
    d1_json = json.loads(d1_json)   # Transforma o json em um dicionario novamente
    # print(d1_json)


# Demonstração de utilização do dicionario após converter o json
for key, value in d1_json.items():
    print(key)
    print('----------')
    for key1, value1 in value.items():
        print(key1, value1)
    print()
