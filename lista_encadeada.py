class No:
    def __init__(self, valor):  # para armazenar o valor dentro do objeto
        self.valor = valor
        self.proximo = None  # incialmente não aponta para outro nó


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        # criar um nó
        novo_no = No(valor)  # por enquanto criamos apenas um nó que está separado do resto da lista
        # conectar o novo nó ao início atual
        novo_no.proximo = self.inicio
        # atualizar o início da lista
        self.inicio = novo_no

    def inserir_final(self, valor):
        # criamos o novo nó
        novo_no = No(valor)
        # se for o primeiro da lista nós modificamos apenas o atributo do objeto
        if self.inicio is None:
            self.inicio = novo_no
            return
        # criamos uma varíavel que aponta para o endereço atual
        atual = self.inicio
        # conectar o último nó ao novo nó
        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = novo_no

    def remover_no(self, valor):
        if self.inicio is None:
            return

        # caso o nó esteja no início da lista
        if self.inicio.valor == valor:
            self.inicio = self.inicio.proximo
            return

        # remove do meio ou do final em uma lista
        anterior = self.inicio
        atual = self.inicio.proximo

        while atual is not None and atual.valor != valor:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            return

        anterior.proximo = atual.proximo

    def imprimir_lista(self):
        atual = self.inicio

        while atual is not None:
            print(atual.valor)
            atual = atual.proximo

    def busca_lista(self, valor):
        atual = self.inicio

        while atual is not None and atual.valor != valor:
            atual = atual.proximo

        if atual is None:
            return False
        else:
            return True

    def tamanho_lista(self):
        atual = self.inicio
        contador = 0

        while atual is not None:
            contador += 1
            atual = atual.proximo

        return contador
    
    def bubble_sort(self):
        if not self.head or not self.head.next:
            return

        passou_limite = None
        trocou = True

        while trocou:
            trocou = False
            atual = self.head

            while atual.next != passou_limite:
                if atual.data > atual.next.data:
                    atual.data, atual.next.data = atual.next.data, atual.data
                    trocou = True
                
                atual = atual.next
            
            passou_limite = atual
