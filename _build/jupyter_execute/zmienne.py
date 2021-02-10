# Twój pierwszy program

Zwyczaj nakazuje, żeby ucząc się jakiegoś języka programowania na początku nauczyć się wyświetlić na ekranie jakiś napis. Tradycyjnie jest to napis *"witaj świecie"* (*hello, world!*). Zmuśmy wiec Pythona, żeby pokazał nam ten napis.

print("Witaj, świecie!")

Zastosowaliśmy tutaj funkcję `print()`, która wyświetla ("drukuje") napis na ekranie. Funkcje mają swoje argumenty, podane w nawiasie. W tym wypadku funkcja `print()` przyjmuje jeden argument - treść napisu, który ma wyświetlić. Zwróć uwagę, że napis jest w cudzysłowie, inaczej Python nie wiedziałby, że słowa *"Witaj, świecie!"* ma potraktować jako napis (a nie np. jako nazwę zmiennej).

## Komentarze

Komentarz to fragment programu, który jest nie jest wykonywany. Komentarze służą do umieszczania uwag i wyjaśnień programisty, poprawiają czytelność kodu. W Pythonie komentarze zaczynają się od `#` i trwają do końca linii. 

# To nie zostanie wykonane
print("To zostanie wykonane") # A to też nie

## Obliczenia

Python to świetny kalkulator. Potrafi dodawać...

print(2 + 2) # dodawanie

...odejmować...

print(2 - 2) # odejmowanie

...mnożyć i dzielić...

print(3 * 8) # mnożenie
print(10 / 2) # dzielenie

Potrafi też wykonywać na prawdę skomplikowane obliczenia. `**` to operator potęgowania, `%` to dzielenie *modulo*, inaczej zwane resztą z dzielenia.

# dziwolągi
print(17.54 * (1234 ** 3))
print(13 % 3)

# o co tu chodzi?
print(1 + (15 ** 15 > 150412 * 2))

## Zmienne

Zmienne służą do przechowywania rzeczy. Rzeczy w zmiennych umieszcza się za pomocą operatora przypisania `=`. Z tych rzeczy później można korzystać, podając *nazwę zmiennej*. Przykładowo:

name = "Lancelot"
quest = "Holy Grail"

print("What is your name?")

print(name)

print("And what is your quest?")

print("To find the", quest)

### Nazwy zmiennych

Zmiennej w Pythonie możemy nadać właściwie dowolną nazwę, jednak trzeba pamiętać o kilku zasadach. Nazwa zmiennej nie może:

- zaczynać się od cyfry
- nie może zawierać spacji (używaj znaku `_`)
- nie może zawierać symboli specjalnych `:'",<>/\?|()!@#$%^&*~-+`

Dobrą praktyką jest nadawanie zmiennym nazw składający się z **małych liter**. Nie powinniśmy używać też słów zastrzeżonych (pełna lista w dokumentacji, Jupyter podpowie zaznaczając nazwę zmiennej innym kolorem). Używanie polskich znaków w nazwach zmiennych **jest błędem** - może spowodować bardzo dziwne efekty, problemy z reprodukowalnością na innych komputerach i jest przejawem złego stylu programistycznego.


## Funkcja `print()` i programowanie interaktywne

Uwaga! Od tego momentu nie będziemy już "drukować" rzeczy na ekranie przy pomocy funkcji `print()`. Okazuje się, że Jupyter Lab (a tak na prawdę IPython) wypisuje zawartość zmiennej na ekranie, jeśli tylko podamy jej nazwę. Czyli zamiast pisać: 

jedzenie = "mielonka"
print(jedzenie)

Możemy napisać po prostu:

jedzenie

Pamiętaj, że jest to specyficzne zachowanie dla IPython Shella i Jupyter Notebooków. Jeśli będziesz pisać zwykły skrypt w Pythonie i uruchamiać go interpreterem, koniecznie musisz stosować funkcję `print()`. Pamiętaj też, że IPython/Jupyter pokazuje wartość ostatniego obiektu przywołanego w obrębie jednej komórki. Czyli np. takie coś:

"Ala"
"ma"
"kota"

...jak widać spowoduje tylko wyświetlenie słowa `'kota'` (ostatni obiekt w obrębie komórki). Żeby wyświetlić wszystkie obiekty, każdy powinien być w osobnej komórce.

"Ala"

"ma"

"kota"

### Typy zmiennych

W zmiennych można umieszczać różne rzeczy. W zależności od tego **jaka** rzecz umieszczona jest w zmiennej, zmienna posiada **typ**. Do tej pory w zmiennych umieszczaliśmy tylko napisy. Ten typ w Pythonie nazywa się **string**. Oprócz tego mamy do dyspozycji wiele innych typów. Najczęściej używane podstawowe typy to: 

- `str` (skrót od *string*) - napisy
- `int` (skrót od *integer*) - liczby całkowite
- `float` (*floating point number*) - liczby rzeczywiste
- `bool` (*boolean*) - wartości logiczne, prawda lub fałsz

Jeśli chcesz sprawdzić typ jakiejś zmiennej, zastosuj funkcję `type()`. Stwórzmy teraz kilka zmiennych:

a = 2
b = 22.0
c = True
d = '33.0'

Sprawdźmy teraz typ każdej ze zmiennych funkcją `type()`:

type(a)

type(b)

type(c)

type(d)

### Rzutowanie typów

Często będziemy na zmiennych wykonywać operacje. Wynik tych operacji będzie zależny od typu zmiennej. Przeanalizuj poniższe przykłady:

2 + 2

Tutaj dodaliśmy dwa inty i otrzymaliśmy inta.

2.0 + 2.0

Teraz dodaliśmy dwa floaty i otrzymaliśmy floata.

2 + 2.0

Tu z kolei dodaliśmy int (`2`) i float (`2.0`). W tej sytuacji Python sam zamieni nam typ tak, żeby po obu stronach działania był `float`.

Nie zawsze jednak operacje na różnych typach się udadzą. Nie możemy np. dodawać napisów do liczb:

"napis" + 2

W tym przypadku trzeba poradzić sobie za pomocą funkcji *rzutującej typ*, czyli wymuszającej zmianę typu na konkretny. Poniżej skorzystałem z funkcji `str()`, zmieniającej typ na string.

x = 12.3
napis = " to liczba typu float"
str(x) + napis

W ten sam sposób można rzutować pozostałe typy. Wykorzystujemy do tego funkcje `str()`, `int()`, `float()` oraz `bool()`. Kilka przykładów:

a = 0
b = " jest mniejsze niż "
c = 1.0

str(a) + b + str(c)

Tutaj zamieniamy zmienne na stringi, aby połączyć je ze sobą. Tak Python rozumie "dodawanie" stringów.

a + int(c)

Teraz zamieniliśmy floata na inta, aby dodać dwie liczby całkowite i uzyskać wynik całkowity.

str(float(a)) + " to to samo co zero"

Teraz zamieniliśmy inta na floata a floata na stringa...

bool(a)

...a teraz z liczby (0) zrobiliśmy wartość logiczną.

str(bool(c)) + " or " + str(bool(a))

A tu co się wydarzyło?

