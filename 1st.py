class No:
    def __init__(self, chave):
        self.esquerda = None
        self.direita = None
        self.valor = chave

class ArvoreBinariaEquilibrada:
    def inserir(self, raiz, chave):
        if raiz is None:
            return No(chave)
        if chave < raiz.valor:
            raiz.esquerda = self.inserir(raiz.esquerda, chave)
        else:
            raiz.direita = self.inserir(raiz.direita, chave)
        return raiz

    def construir_arvore_equilibrada(self, elementos):
        if not elementos:
            return None
        meio = len(elementos) // 2
        raiz = No(elementos[meio])
        raiz.esquerda = self.construir_arvore_equilibrada(elementos[:meio])
        raiz.direita = self.construir_arvore_equilibrada(elementos[meio+1:])
        return raiz

    def percorrer_em_ordem(self, raiz, resultado):
        if raiz:
            self.percorrer_em_ordem(raiz.esquerda, resultado)
            resultado.append(raiz.valor)
            self.percorrer_em_ordem(raiz.direita, resultado)
        return resultado

    def imprimir_arvore(self, no, prefixo="", eh_esquerda=True):
        if no is not None:
            self.imprimir_arvore(no.direita, prefixo + ("│   " if eh_esquerda else "    "), False)
            print(prefixo + ("└── " if eh_esquerda else "┌── ") + str(no.valor))
            self.imprimir_arvore(no.esquerda, prefixo + ("    " if eh_esquerda else "│   "), True)

# Uso do código
valores = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
valores.sort()
arvore = ArvoreBinariaEquilibrada()
raiz = arvore.construir_arvore_equilibrada(valores)
valores_ordenados = arvore.percorrer_em_ordem(raiz, [])
print("Percorrendo a árvore binária de busca em ordem:", valores_ordenados)
print("\nVisualização ASCII da árvore binária de busca equilibrada:")
arvore.imprimir_arvore(raiz)
