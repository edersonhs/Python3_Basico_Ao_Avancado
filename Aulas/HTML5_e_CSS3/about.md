# HTML

### Tags:
**h1:** Titulo
**p:** Paragrafo
**br:** Serve para quebra de linha (não tem corpo)
**div:** bloco (Container Generico)
**style:** Normalmente fica no head, utilizada para incluir o css no html
**meta:** Normalmente fica no head, contem metadados para o navegador
**blockquote:** Bloco de citação (Atributo cite serve para inserir a fonte da citação)
**hr:** Cria uma linha de ponta a ponta. É uma tag sem corpo
**code:** citar codigo
**pre:** tag de texto préformatado, mantem espaços e quebra de linhas

### Tags inline
**span:** Estilo in line, não quebra linha nem nada do tipo (Container generico)
**b:** bold/Negrito
**strong:** É uma tag semantica que indica uma palavra/frase importante (deixa negrito também)
**i:** Italico
**em:** Deixa visualmente italico também, mas serve para dar enfase para o google ou leitores de tela para deficientes.
**del:** Deixa o conteudo "riscado" (Semanticamente)
**s:** Deixa o conteudo riscado
**small:** Deixa o texto pequeno 
**q:** Citação
**a:** Link
```
Atributos de a:
href: Caminho ou endereço do link

target: é a forma que o link será aberto. (em nova guia, mesma guia, etc).
Atributos de target:
_self: Load the URL into the same browsing context as the current one. This is the default behavior.
_blank: Load the URL into a new browsing context. This is usually a tab, but users can configure browsers to use new windows instead.
_parent: Load the URL into the parent browsing context of the current one. If there is no parent, this behaves the same way as _self.
_top: Load the URL into the top-level browsing context (that is, the "highest" browsing context that is an ancestor of the current one, and has no parent). If there is no parent, this behaves the same way as _self.

rel: No caso de determinados links no site, convém informar ao Google qual é sua relação com a página vinculada. Para fazer isso, use um dos seguintes valores de atributo rel na tag <a>. (mais informações em https://developers.google.com/search/docs/advanced/appearance/qualify-outbound-links?hl=pt-br)
```
**img:** tag de imagem no html
```
Atributos:
src: caminho da imagem, pode ser link ou diretorio

alt: texto alternativo (descrever a imagem para leitores de texto)
width: Largura
height: Altura
```



### Utils:
* Atributos de tag sem valor são definidos com valor booleano true pelo navegador.
* Valores de atributos podem ser colocados sem as aspas mas é recomendado utilizar.
* Atributo id(comum) éprecisa ser unico.
* Atributo class diferente do id pode se repetir.
* Uma tag pode ter mais que uma classe. (ex: `<h1 class="classe1 classe2">exemplo</h1>`)

## Headings - H1 a H6
Headings são as tags mais importantes do cabeçalho, principalmente em termos de busca, os buscadores vão escanear o documento e os seus cabeçalhos do para entender do que se trata.

A diferença padrão dos headings é o tamanho da fonte, mas isso pode ser alterado por CSS, portanto o ideal é utilizalos para manter a semantica correta.



# CSS

### Utils:
* Para especificar uma classe no CSS deve-se seguir o exemplo:
    ```
    .fundo-vermelho {
                background-color: black;
                color: white;
            }
    ```

* Para especificar um id no CSS utiliza-se da # antes do nome do id, exemplo:
    ```
    #heading-two {
                background-color: green;
            }
    ```

* O id é um dos elementos que tem a maior especificidade no CSS. Portanto para sobrescrever um id seria necessario utilizar outro id ou apesar de não indicado, utilizar do `!important` para informar ao CSS que o conteudo é importante e precisa ter prioridade. Exemplo:
    ```
            #heading-two { /* Aplicando estilo pelo id */
                background-color: green;
            }

            .fundo-vermelho { /* Alterando o mesmo conteudo pela classe */
                background-color: black !important;
                color: white !important;
            }
    ```