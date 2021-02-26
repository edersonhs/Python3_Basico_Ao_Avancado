import subprocess

# Windows - ping 127.0.0.1
# Linux - ping 127.0.0.1 - c 4

proc = subprocess.run(
    ['ping', '127.0.0.1'],
    # Impededindo que a saida do comando saia no terminal guardando o conteudo
    # na variavel stdout da instancia proc.
    capture_output=True,
    text=True   # Configurando a saída para texto, o formato padrão é bits
)

print(proc.stdout)

"""
print(proc.stderr)   # É None caso não ocorra nenhum erro
print(proc.stdout)   # É a saída do comando (dependendo da situação é None)
print(proc.returncode)   # Se for executado com sucesso é zero
print(proc.args)   # Vai mostrar os argumentos informados
"""
