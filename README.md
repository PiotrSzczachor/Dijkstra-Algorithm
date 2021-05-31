# Teoria-Grafow-PS
---
# OPIS ALGORYTMU:
Algorytm Dijkstry jest algorytmem szukającym najkrótszej ścieżki w grafie, z wierzchołka startowego do wszystkich pozostałych wierzchołków. Sprawdza się on w przypadku problemów o dodatniej wadze krawędzi grafu (w przypadku grafów z krawędziami o wagach ujemnych, możemy korzystać z algorytmu Forda Bellmana). Algorytm Dijkstry jest wykorzystywany w sieciach komputerowych przy tak zwanym routingu. Polega to na wyznaczeniu jak najlepszej trasy i wysłaniu na nią pakietu danych w sieci komputerowej. Innym zastosowaniem algorytmu Dijkstry jest stosowanie go w celu wyznaczenia jak najkrótszej drogi do danej miejscowości z punktu startowego. W takiej sytuacji drogi traktujemy jako krawędzie o różnych wagach, natomiast skrzyżowania traktujemy jako węzły grafu. 
---
# INSTRUKCJA:
Aby skorzystać z powyższego algorytmu, input należy podać w pliku json jako macierz sąsiedztwa, w której zamiast wpisywac "1" w sytuacji gdy dane wierzchołki są połączone krawędzią wpisujemy wagę tej krawędzi. Na przyklad, w sytuacji, w ktorej wierzchołek 0 jest połączony z wierzchołkiem 2 krawędzią skierowaną o wadze 5, to w macierzy sąsiedztwa na pozycji "[0][2]" powinno się znaleźć "5". W przypadku gdy nie ma połączenia wpisujemy "0".
