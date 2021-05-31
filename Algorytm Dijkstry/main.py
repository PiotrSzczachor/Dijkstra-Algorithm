import json
import numpy as np


# Wczytujemy dane z pliku json
file = open("input.json")
data = json.load(file)

# Tansformujemy nasze dane do numpy array
matrix = np.asarray(data)

# Sprawdzamy liczbe wierzcholkow
nodesCount = np.shape(matrix)[0]
# print(nodes_count)

# Pobieramy index poczatkowego wierzcholka
startNode = int(input("Wprowadź początkowy wierzchołek (wierzchołki indeksowane są od 0): "))

successors = []  # Jest to lista poprzednikow zawierajaca informacje o indexie poprzednika i jego wage
for i in range(0, nodesCount):
    nodeNeighbours = []
    for j in range(0, nodesCount):
        if matrix[i][j] != 0:
            nodeNeighbours.append([j, matrix[i][j]])
    successors.append(nodeNeighbours)

nodes = []
distance = []
predecessors = []
wasChecked = []

for i in range(0, nodesCount):  # Ustawaianie poprzednikow kazdego wierzchołka na "-1" (nie znamy poprzednika)
    predecessors.append(-1)
for i in range(0, nodesCount):  # Wpisujemy wszystkie wierzcholki do listy
    nodes.append(i)
for i in range(0, nodesCount):  # Ustawiamy dystans do karzego wierzcholka na inf (na poczatku nie znamy dystansu)
    distance.append(np.inf)
for i in range(0, nodesCount):  # Wypelniamy liste ktora bedzie nas informowac czy wierzcholek zostal odwiedzony
    wasChecked.append(False)    # Jezeli tak to zmienna przyjmie wartosc True (na poczatku wszystkie musza miec False)


distance[startNode] = 0  # Dystans do samego siebie jest rowny 0
predecessors[startNode] = -1  # Poczatkowy wierzcholek nie ma poprzednika wiec ustawiamy jego wartosc na "-1"
currentNode = startNode  # Ustawiamy wierzcholek poczatkowy jako aktualnie rozpatrywany wierzcholek

while currentNode != -1:
    wasChecked[currentNode] = True  # Ustawiamy informacje ze wierzcholek zostal odwiedzony
    for successor in successors[currentNode]:
        if successor[1] > 0 and successor[1] + distance[currentNode] < distance[successor[0]]:
            distance[successor[0]] = successor[1] + distance[currentNode]
            predecessors[successor[0]] = currentNode
    index = 0
    # Wyszukujemy minimum
    minimum = np.inf
    minimumIndex = -1
    for dist in distance:
        if dist < minimum and wasChecked[index] == False:
            minimumIndex = index
            minimum = dist
        index += 1
    currentNode = minimumIndex


# Wyswietlanie outputu
for node in range(0, nodesCount):
    if node == startNode:
        continue
    else:
        nodeToPrint = node
        print("Droga o dystansie " + str(distance[node]) + " do wierzcholka " + str(node) + " z wierzcholka " + str(startNode) + ": ", end=" ")
        path = []
        while predecessors[node] != -1:
            path.append(predecessors[node])
            node = predecessors[node]
        for i in range(len(path)-1, -1, -1):
            print(path[i], end=" -> ")
        print(nodeToPrint)
        print(" ")





