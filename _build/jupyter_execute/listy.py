# Listy

W Pythonie możemy przechowywać w jednej zmiennej wiele rzeczy. Służą do tego (między innymi) listy. Lista to uporządkowany zbiór wartości. Każda wartość ma swój indeks liczbowy. W Pythonie indeksy numerujemy kolejnymi liczbami całkowitymi od zera. Listę definiujemy w ten sposób:

lista = ['jabłko', 'gruszka', 'śliwka', 'morela', 'ananas', 'pomarańcza']

Aby dostać się do elementów na liście, wystarczy po jej nazwie podać indeks w nawiasach kwadratowych. Pamiętaj! Listy numerujemy **od zera!**

lista[0]

lista[1]

lista[2]

Możemy też zastosować ujemne indeksy. Wtedy Python policzy je od końca listy:

lista[-1]

lista[-3]

Można też wybrać podzbiór listy, przy pomocy takiego zapisu:

lista[0:3]

Działa to tak, że po lewej stronie dwukropka podajemy indeks początkowy a po prawej końcowy, ale *rozłącznie*. Kilka przykładów:

lista[2:5] # czyli pozycje 2, 3 i 4

lista[4:5] # tylko pozycja 4

lista[1:-1] # od pozycji 1 do przedostatniej

Można też nie podawać indeksu po jednej ze stron dwukropka. Wtedy Python wybierze wszystkie elementy od początku/do końca listy, tak jak poniżej:

lista[:3]

lista[3:]

lista[:]

**Ciekawostka:** okazuje się, że tak samo jak listy możemy kroić zwykłe napisy. Działa to, ponieważ `string` w Pythonie jest uporządkowaną sekwencją. Możemy więc napisać tak:

nazwisko = "Brzęczyszczykiewicz"
nazwisko[:7]

nazwisko[7:12]

nazwisko[12:]

## Operacje na listach

Na listach możemy wykonywać różne operacje. Możemy dodawać nowe elementy, usuwać elementy istniejące, sortować listy i robić wiele innych rzeczy. W tym celu będziemy korzystać z **metod**. O metodach będziemy się jeszcze uczyć, na tą chwilę wystarczy tylko wiedzieć, że są to funkcje które *należą* do zmiennej. Odwołujemy się do nich poprzez zapis w postaci `nazwa_zmiennej.nazwa_metody(argumenty)`. 

Żeby dodać do istniejącej listy element na jej koniec, korzystamy z metody `append()`.

filmy = ['Święty Graal', 'Sens Życia']
filmy.append('Żywot Briana')
filmy

Aby dorzucić do listy element w konkretnym jej miejscu, korzystamy z metody `insert()`. Oczywiście indeksy numerowane są od zera, więc wstawienie elementu z indeksem 1 zaskutkuje umieszczeniem go na drugiej pozycji na liście.

filmy.insert(1, 'And now for something completely different')
filmy

Aby usunąć element z listy, stosujemy metodę `pop()`. Jako argument podajemy indeks elementu, który chcemy usunąć. Jako bonus, metoda `pop()` zwraca to, co usunęliśmy.

filmy.pop(2)

Możemy też usunąć element podając jego nazwę. Służy do tego metoda `remove()`. 

filmy.remove("Święty Graal")
filmy

Listy możemy sortować za pomocą metody `sort()`. Jeśli, tak jak w poniższym przykładzie, lista składa się z liczb, Python posortuje ją od najmniejszej do największej. Jeśli lista składa się ze stringów, sortowanie jest alfabetyczne. Metoda `reverse()` odwraca kolejność elementów na liście.

liczby = [1, 7, -400, 19, 3, 25, 123, 1233, -2]
liczby.sort()
print("liczby po posortowaniu:", liczby)
liczby.reverse()
print("liczby po odwróceniu", liczby)

## Listy list*

Skoro na liście mogą znaleźć się elementy różnych typów, nic nie stoi na przeszkodzie aby jako elementy na liście umieścić inne listy. W ten sposób możemy stworzyć strukturę danych przypominającą tabelę. W poniższym przykładzie zmieniłem listę `filmy` tak, by jej pierwszym elementem była lista z tytułami filmów, a drugim lista z rokiem powstania każego z filmów.

filmy = [
    ['Święty Graal', 'And now for something completely different', 'Sens Życia', 'Żywot Briana'],
    [1975, 1971, 1983, 1979]
]
filmy

Elementy na liście list możemy wybierać tak samo jak w zwykłej liście, tylko zamiast jednego potrzebujemy dwóch indeksów. Najpierw podajemy indeks listy "zewnętrznej", a później "wewnętrznej". Na przykład:

print("Film", filmy[0][3], "powstał w", filmy[1][3])
print("Film", filmy[0][0], "powstał w", filmy[1][0])