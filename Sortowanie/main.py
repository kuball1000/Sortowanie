import copy
import random
import time
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        n = i - 1
        while n >= 0 and arr[n] < key:
            arr[n + 1] = arr[n]
            n -= 1
        arr[n + 1] = key
    return arr


def shell_sort(arr):
    odstepy = get_hibbard(arr)
    n = len(arr)
    for d in odstepy:
        # print("Wartosc przyrostu: ", d)
        for i in range(n):
            for j in range(0, n - i - d):
                if arr[j] < arr[j + d]:
                    arr[j], arr[j + d] = arr[j + d], arr[j]
    return arr


def get_hibbard(lista):
    Hibbard = []
    x = 1
    p = (2 ** x) - 1
    while p <= len(lista):
        x += 1
        Hibbard.append(p)
        p = (2 ** x) - 1
    Hibbard.reverse()
    return Hibbard


def merge_sort(arr):
    global counter
    l = len(arr)
    if l > 1:
        Left = arr[:l // 2]
        Right = arr[l // 2:]
        merge_sort(Left)
        merge_sort(Right)
        i = 0
        j = 0
        k = 0
        while i < len(Left) and j < len(Right):
            if Left[i] > Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1

        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1
        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1
        counter += 1
    return arr, counter


def quick_sort(arr, p, r):
    if p < r:
        q = Partition(arr, p, r)
        quick_sort(arr, p, q)
        quick_sort(arr, q + 1, r)
    return arr


def Partition(A, p, r):
    pivot = A[p]
    # print("Wartosc pivota to: ", pivot)
    i = p
    j = r
    while True:
        while A[i] > pivot:
            i += 1
        while A[j] < pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        else:
            return j


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        get_heap(arr, n, i)
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        get_heap(arr, i, 0)
    return arr


def get_heap(arr, n, i):
    father = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[i] > arr[left_child]:
        father = left_child
    if right_child < n and arr[right_child] < arr[father]:
        father = right_child
    if father != i:
        arr[i], arr[father] = arr[father], arr[i]
        get_heap(arr, n, father)


czasy_lista = []


def test(funkcja, ilosc, rodzaj=""):
    print(funkcja, rodzaj if rodzaj != "" else "random")
    czasy = 0
    for el in ilosc:
        print("dla", el)
        # generujemy listę dla każdego rozmiaru danych
        czasy_lista1 = []
        for i in range(10):
            # powtarzane 10-krotnie dla każdego rozmiaru danych
            lista = []
            for x in range(el):
                lista.append(random.randint(1, 10 * el))
            # poniżej formatujemy listę w zależności od potrzeb
            # "A" - A-kształtny "V" - V-kształtny
            if rodzaj == "A" or rodzaj == "V":
                mid = len(lista) // 2
                G = lista[:mid]
                F = lista[mid:]
                G.sort()
                F.sort(reverse=True)
                if rodzaj == "A":
                    lista = G + F
                elif rodzaj == "V":
                    lista = F + G
            # "R" - rosnący "M" - malejący
            if rodzaj == "R":
                lista.sort()
            if rodzaj == "M":
                lista.sort(reverse=True)
            # print("Lista wejsciowa: ", lista)
            # ponieważ quick sort wymaga więcej parametrów,
            # musimy odróżnić wykonanie jej od reszty funkcji sortowania
            if funkcja != quick_sort:
                start = time.time()
                funkcja(lista)
                end = time.time()
            else:
                start = time.time()
                funkcja(lista, 0, len(lista) - 1)
                end = time.time()
                # print("Lista posortowana: ", lista)
            czas = end - start
            czasy_lista1.append(czas)
            print("Test", i, "-", czas)
            czasy += czas
        print("srednia", el, "-", czasy / 10)
        czasy_lista.append(czasy_lista1)
        # print(czasy_lista)


counter = 0
# lista_to_sort = copy.copy(lista)
wielkosci = [
    100, 1000, 5000, 10000, 50000, 100000, 250000, 500000, 750000, 1000000
]
# wielkosci = [100]
qq = 0

wybor = ""
while wybor != "1" and wybor != "2":
    wybor = input(
        "Wybierz tryb wprowadzenia danych. 1 - z klawiatury, 2 - uruchom testy: ")
    if wybor != "1" and wybor != "2":
        cls()
        print("Wprowadzono niepoprawna opcje!")
    cls()

if wybor == "1":
    lista = []
    while True:
        lista = input(
            "Podaj ciag liczb naturalnych oddzielonych spacja. Ciag nie moze zawierac wiecej niz 10 elementow: "
        ).split()
        if len(lista) > 10:
            cls()
            print("Ciag jest za dlugi!")
        elif lista == []:
            cls()
            print("Nie podano zadnego ciagu!")
        else:
            try:
                lista = [int(x) for x in lista]
                break
            except:
                cls()
                print("Nie podales liczb naturalnych!")
        cls()

    while True:
        lista_to_sort = copy.copy(lista)
        if qq == 0:
            qq = 1
            print("Twoja lista: ", lista)
            wybor = input(
                "Wybierz metode do sortowania.\n 1 - insertion sort \n 2 - shell sort "
                "\n 3 - merge sort \n 4 - heap sort \n 5 - quick sort \n 0 - wyjdz \n")
            print("")
        else:
            wybor = input("Wybierz nowa metode: ")
            print("")
        if wybor == "0":
            exit("Do zobaczenia :)")
        if wybor == "1":
            print("Metoda insertion sort")
            start = time.time()
            print("Posortowana lista: ", insertion_sort(lista_to_sort))
            end = time.time()
            print("Czas wykonania: ", end - start, "\n")
        elif wybor == "2":
            print("Metoda shell sort")
            start = time.time()
            print("Posortowana lista: ", shell_sort(lista_to_sort))
            end = time.time()
            print("Czas wykonania: ", end - start, "\n")
        elif wybor == "3":
            print("Metoda merge sort")
            counter = 0
            start = time.time()
            print("Posortowana lista: ", merge_sort(lista_to_sort))
            end = time.time()
            print("Czas wykonania: ", end - start, "\n")
        elif wybor == "4":
            print("Metoda heap sort")
            start = time.time()
            print("Posortowana lista: ", heap_sort(lista_to_sort))
            end = time.time()
            print("Czas wykonania: ", end - start, "\n")
        elif wybor == "5":
            print("Metoda quick sort")
            start = time.time()
            print("Posortowana lista: ",
                  quick_sort(lista_to_sort, 0,
                             len(lista_to_sort) - 1))
            end = time.time()
            print("Czas wykonania: ", end - start, "\n")
        else:
            print("Nie wybrano poprawnej opcji!")

elif wybor == "2":
    # test(insertion_sort, wielkosci)
    # test(shell_sort, wielkosci)
    # test(merge_sort, wielkosci)
    # test(heap_sort, wielkosci)
    # test(quick_sort, wielkosci)

    # test(insertion_sort, wielkosci, rodzaj="V")
    # test(shell_sort, wielkosci, rodzaj="V")
    # test(merge_sort, wielkosci, rodzaj="V")
    test(heap_sort, wielkosci, rodzaj="V")
    # test(quick_sort, wielkosci, rodzaj="V")

    # test(insertion_sort, wielkosci, rodzaj="A")
    # test(shell_sort, wielkosci, rodzaj="A")
    # test(merge_sort, wielkosci, rodzaj="A")
    test(heap_sort, wielkosci, rodzaj="A")
    # test(quick_sort, wielkosci, rodzaj="A")

    # test(insertion_sort, wielkosci, rodzaj="R")
    # test(shell_sort, wielkosci, rodzaj="R")
    # test(merge_sort, wielkosci, rodzaj="R")
    test(heap_sort, wielkosci, rodzaj="R")
    # test(quick_sort, wielkosci, rodzaj="R")

    # test(insertion_sort, wielkosci, rodzaj="M")
    # test(shell_sort, wielkosci, rodzaj="M")
    # test(merge_sort, wielkosci, rodzaj="M")
    test(heap_sort, wielkosci, rodzaj="M")
    # test(quick_sort, wielkosci, rodzaj="M")

    # print(czasy_lista)
    f = open("wyniki.txt", mode="w")
    for i in range(len(czasy_lista)):
        a = czasy_lista[i]
        a = [str(x) for x in a]
        linia = " ".join(a)
        f.write(linia)
        f.write("\n")
    f.close()