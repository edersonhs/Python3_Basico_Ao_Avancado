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

print()

"""
*************************************************************************************
Os módulos e pacotes devem ser importados levando em conta o arquivo de origem(ponto de entrada).
Ou seja: Se o __main__ esta em um diretorio, todos os outros modulos tem que fazer a
importanção levando em conta o caminho do main,e não do módulo.
"""

"""
Para ler modulos/pacotes que estão em um caminho superior ao do __main__ atual
Pode-se usar este "hack" para incluir a pasta onde os módulos superiroes estão no path
"""
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'   # Inclui a pasta anterior ao diretorio atual ao path
            )
        )
    )
except ImportError:
    raise

# ********************
import sys
print(sys.path)   # Mostra os caminhos dos quais o python esta varrendo para encontrar os módulos
