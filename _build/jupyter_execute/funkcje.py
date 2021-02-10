# Funkcje

Znasz już sporo funkcji w języku Python. Potrafisz wyświetlać tekst (`print()`), pobrać tekst od użytkownika i umieścić w zmiennej (`input()`), sprawdzać typ zmiennej (`type()`), zmienić zmienną w inta (`int()`), floata (`float()`) czy stringa (`str()`). Potrafisz też stosować _metody_ - specjalne funkcje skojarzone z obiektami, np. z listami. Za pomocą metod można np. dodawać elementy do listy (`append()`), usuwać elementy z listy (`remove()` albo `pop()`) Wszystkie poznane przez ciebie do tej pory funkcje wyglądają i działają podobnie - najpierw podajesz nazwę funkcji a później, w nawiasach, _argumenty_. O funkcjach warto myśleć jako o _czarnych skrzynkach_. Dajemy im jakieś dane w postaci argumentów i oczekujemy, że zwrócą nam jakiś wynik. Niebardzo interesuje nas sposób, w jaki to robią - zależy nam na wyniku ich działania.

Nic nie stoi na przeszkodzie, żeby w Pythonie tworzyć własne funkcje. Jest to jedną z najważniejszych i najbardziej przydatnych umiejętności jakich się nauczymy na tym kursie. Przydatne jest to co najmniej z trzech powodów:

1. Żeby prosto i czytelnie realizować powtarzające się zadania
2. Żeby zwiększyć jasność i czytelność kodu
3. Żeby móc fragmenty napisanego kodu wykorzystać ponownie w innym programie


## Prosty przykład
Jak stworzyć własną funkcję w Pythonie? Popatrz na poniższy przykład. Powiedzmy, że chcemy napisać funkcję, która oblicza pierwiastek trzeciego stopnia z danej liczby. Funkcja bierze jeden argument, zmienną `a`, oblicza pierwiastek trzeciego stopnia i drukuje na ekranie wynik. Jej definicja wygląda jakoś tak:

def pierw_3(a):
    wynik = a ** (1 / 3)
    print('Pierwiastek trzeciego stopnia z', a, 'to', wynik)

W ten sposób _zdefiniowaliśmy_ funkcję o nazwie `pierw_3`. Nazwy funkcji muszą przestrzegać tych samych reguł co nazwy zmiennych. Możemy teraz z niej skorzystać:

pierw_3(8)
pierw_3(27)
pierw_3(1000)
pierw_3(123445)

Widzimy, że każde kolejne wywołanie funkcji `pierw_3()` spowodowało wykonanie całego kodu znajdującego się w definicji funkcji, dla odpowiedniej wartości argumentu a.

## Zwracanie wartości

Powiedzmy, że chcielibyśmy na wyniku naszego pierwiastkowania wykonać kolejne operacje matematyczne. Samo wydrukowanie wartości na ekranie jest rozwiązaniem mało elastycznym - jest duża szansa, że pisząc inny program w przyszłości nie będziemy w stanie skorzystać z napisanej przez nas funkcji. Musimy nieco zmodyfikować naszą funkcję tak, aby _zwracała_ ona wartość. Wartość tą możemy później wykorzystać poprzez przypisanie jej do zmiennej (operatorem `=`) albo umieszczenie w innej funkcji. Robimy to przy pomocy słowa kluczowego `return`.

def pierw_3(a):
    wynik = a ** (1 / 3)
    return wynik

x = pierw_3(8)
y = pierw_3(27)

print('Pierwiastek 3-go stopnia z 8 to', x, 'a z 27 to', y)

## Wiele argumentów

Co jeśli chcielibyśmy, aby nasza funkcja liczyła pierwiastek dowolnego stopnia a nie tylko trzeciego? Musimy przekazać jej kolejny argument - nazwijmy go `stopien`.

def pierwiastek(a, stopien):
    wynik = a ** (1 / stopien)
    return wynik

Teraz wywołanie naszej funkcji musi zawierać w sobie również drugi argument. Najprościej dodać go po przecinku:

print('Pierwiastek kwadratowy z 4 to', pierwiastek(4, 2))
print('Pierwiastek trzeciego stopnia z 8 to', pierwiastek(8, 3))
print('Pierwiastek 4 stopnia z 16 to', pierwiastek(16, 4))

## Odwołania przez pozycję i przez nazwę

W funkcji powyżej odwołowywaliśmy się do argumentów _przez pozycję_. Python przyporządkował pierwszy argument na liście do zmiennej `a`, dlatego że w definicji ta zmienna była podana jako pierwsza. Analogicznie, drugi argument na liście został przyporządkowany do zmiennej `stopnien`, ponieważ była druga na liście. Do argumentów w funkcjach możemy odwoływać się również przez ich nazwę. Robi się to tak:

print('Pierwiastek 5 stopnia z 100000 to', pierwiastek(stopien = 5, a = 100000))

Podając wprost nazwy argumentów, możemy je umieścić w dowolnej kolejności. Jest to bardzo praktyczne, jeżeli funkcje mają bardzo dużo argumentów.

## Wartości domyślne

Co, jeśli chcemy, aby niektóre argumenty przyjmowały wartości _domyślne_, tzn. jeżeli nie są podane na liście argumentów w wywołaniu funkcji, to przyjmują z góry określoną wartość? Np. chcielibyśmy, aby nasza funkcja pierwiastkująca po otrzymaniu tylko jednego argumentu domyślnie obliczała pierwiastek kwadratowy. Musimy zmodyfikować definicję funkcji w ten sposób:

def pierwiastek(a, stopien = 2):
    wynik = a ** (1 / stopien)
    return wynik

Teraz możemy skorzystać z wartości domyślnej poprzez nie podawanie drugiego argumentu.

print('Pierwiastek kwadratowy z 4 to', pierwiastek(4))
print('Pierwiastek kwadratowy z 9 to', pierwiastek(9))
print('Pierwiastek trzeciego stopnia z 8 to', pierwiastek(8, 3))

W ten sposób zdefiniowanych jest wiele funkcji w Pythonie. Zerknijmy w dokumentację funkcji `print()`:

?print()

Okazuje się, że oprócz argumentów do "wydrukowania" możemy w funkcji print przekazać argument `sep` (czyli separator, domyślnie spacja) oraz `end` (co dodać na końcu drukowanego stringa, domyślnie jest to znak końca linii.

## Zakresy zmiennych a funkcje

Pisząc własne funkcje trzeba koniecznie pamiętać o tym, że wszystkie zmienne definiowane wewnątrz funkcji pozostają _lokalne_, tj. nie są widoczne poza funkcją. Zwróć uwagę na poniższy przykład:

def pierwiastek(a, stopien = 2):
    wynik = a ** (1 / stopien)
    return wynik

a = pierwiastek(16, 2)
print(wynik)

Skąd ten błąd? `NameError: name 'wynik' is not defined` oznacza, że zmienna wynik nie została zdefiniowana. Python zdaje się _nie widzieć_ zmiennej znajdującej się wewnątrz funkcji. Musisz pamiętać, że jest to właściwe zachowanie - funkcje to "czarne skrzynki", do których dane trafiają poprzez argumenty a wynik ich działania zwracany jest poprzez słowo kluczowe `return`. 

