import random
import math
import pyxel

def calcular_distancia_euclidiana(ponto_a, ponto_b):
    return math.sqrt((ponto_b[0] - ponto_a[0]) ** 2 + (ponto_b[1] - ponto_a[1]) ** 2)

def obter_pontos(matriz):
    coordenadas = []
    tamanho = len(matriz)
    for i in range(tamanho):
        for j in range(tamanho):
            if matriz[i][j] == 1:
                coordenadas.append((i, j))
    return coordenadas

def gerarTeia(dimensao):
    matriz = []
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            valor = random.randint(0, 100)
            linha.append(1 if valor >= 99 else 0)
        matriz.append(linha)
    return matriz

class Aplicacao:
    def __init__(self):
        self.dimensao = 25
        self.matriz_teia = gerarTeia(self.dimensao)
        self.lista_pontos = obter_pontos(self.matriz_teia)
        self.primeiro_ponto = None
        self.segundo_ponto = None
        self.encontrados = False

        pyxel.init(25, 25, fps=10)

    def desenhar(self):
        pyxel.cls(0)
        self.desenhar_pontos()
        if self.primeiro_ponto and self.segundo_ponto:
            pyxel.rect(self.primeiro_ponto[0], self.primeiro_ponto[1], 1, 1, 8)
            pyxel.rect(self.segundo_ponto[0], self.segundo_ponto[1], 1, 1, 8)

    def atualizar(self):
        if not self.encontrados:
            menor_distancia, self.primeiro_ponto, self.segundo_ponto = self.encontrar_pontos_proximos(self.lista_pontos)
            pyxel.rect(self.primeiro_ponto[0], self.primeiro_ponto[1], 1, 1, 6)
            pyxel.rect(self.segundo_ponto[0], self.segundo_ponto[1], 1, 1, 6)
            pyxel.flip()
            pyxel.cls(0)

            if menor_distancia == 1:
                self.encontrados = True
                print("Os pontos mais próximos são:", self.primeiro_ponto, self.segundo_ponto)

    def desenhar_pontos(self):
        for ponto in self.lista_pontos:
            pyxel.rect(ponto[0], ponto[1], 1, 1, 7)

    def encontrar_pontos_proximos(self, pontos):
        if len(pontos) < 2:
            return float('inf'), None, None

        menor_dist = float('inf')
        p1 = p2 = None

        for i in range(len(pontos)):
            for j in range(i + 1, len(pontos)):
                distancia = calcular_distancia_euclidiana(pontos[i], pontos[j])
                if distancia < menor_dist:
                    menor_dist = distancia
                    p1, p2 = pontos[i], pontos[j]

                pyxel.rect(pontos[i][0], pontos[i][1], 1, 1, 7)
                pyxel.rect(pontos[j][0], pontos[j][1], 1, 1, 7)
                pyxel.flip()
                pyxel.cls(0)

        self.encontrados = True
        print(p1)
        print(p2)
        return menor_dist, p1, p2

    def executar(self):
        pyxel.run(self.atualizar, self.desenhar)

if __name__ == "__main__":
    Aplicacao().executar()
