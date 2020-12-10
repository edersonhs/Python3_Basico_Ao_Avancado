# Módulos padrão do Python:
# Módulos são arquivos .py (que contém python) e servem para expandir as funçionalidades padrão da linguagem.
# Veja tpdps ps módulos padrão do Python em:
# https://docs.python.org/3/py-modindex.html

import sys   # importando o módulos sys
print(sys.platform)   # Para verificar todas as funcionalidades de um módulo pode-se usar o autocomplete di IDE ou a documentação

"""
Para instalar módulos de terceiros:
pip install nome_modulo

Para desinstalar módulos:
pip uninstall nome_modulo
"""

print(__name__)   # Mostra o nome do Módulo sendo executado
"""
Quando este arquivo for executado, ele será '__main__"

Se for importando como um modulo em outro arquivo e executado através do outro arquivo
ele se torna "Modulos_Padrao_Python" e o arquivo de origem será o "__main__".

Vale para todos os módulos.
"""