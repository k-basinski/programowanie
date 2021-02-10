# Pętle

Czasem chcielibyśmy, aby nasz program wykonał jakąś rzecz kilka razy. Być może chcielibyśmy wykonać jakiś fragment kodu tak długo, aż jakiś warunek jest spełniony. W innych sytuacjach chcielibyśmy wykonać jakąś skomplikowaną operację na wszystkich elementach listy. Jak to zrobić? Do tego właśnie służą pętle.

## Pętla `while`

Najprostszym rodzajem pętli w Pythonie jest pętla `while`. Pętla ta wykonuje jakiś blok kodu do momentu, w którym wartość logiczna wyrażenia rozpoczynającego pętlę stanie się fałszywa. Na przykład:

liczba = 0

while liczba < 10:
    print(liczba)
    liczba = liczba + 1

Jak widać, jest to bardzo podobne do instrukcji `if`. Tym razem jednak zamiast wykonywać coś raz, dany blok kodu wykonuje się tak długo, aż warunek umieszczony u góry pętli stanie się fałszywy. Inny przykład:

haslo = input("Podaj hasło!")

while haslo != 'koniec':
    print('Wpisałeś złe hasło')
    haslo = input('Podaj hasło!')
    
print('Podałeś dobre hasło. Teraz dam Ci spokój.')

Ten lekko głupawy programik domaga się podania hasła w pierwszej linijce. Hasło podane przez użytkownika umieszczane jest w zmiennej `haslo`. W pętli `while` sprawdzany jest warunek `haslo != 'koniec'`. Pętla będzie "kręcić się" aż do momentu, w którym użytkownik nie wpiszę słowa _koniec_. Wtedy dopiero warunek pętli zmieni wartość logiczną na `False` i pętla się zakończy.

Uwaga! Pętlą `while` bardzo łatwo jest zawiesić Pythona! Jeśli przez przypadek zrobisz nieskończoną pętlę, przerwij działanie Pythona poprzez komendę _kernel -> restart kernel_ z menu górnego.

## Pętla `for`

Innym rodzajem pętli dostępnym w Pythonie jest pętla `for`. Pętla ta służy do przeglądania zawartości list (i innych _iterowalnych_ obiektów o których nie będziemy się uczyć na tym kursie). Zanalizuj ten prosty przykład:

imiona = ['Ania', 'Basia', 'Kasia', 'Zosia', 'Czesia']

for i in imiona:
    print(i)

Jak to działa? Najpierw deklarujemy listę złożoną z pięciu imion. Następnie pętla `for` "zagląda" do każdego z elementów listy po kolei i umieszcza wartość tego elementu w zmiennej `i`. Teraz mogę wykonać dowolne operację na każdym z elementów listy, ponieważ mam do niego dostęp poprzez zmienną `i`. 

Na marginesie: zmienna w pętli `for`, która przegląda zawartość listy to zwyczajowo `i`, ale może to być dowolna nazwa. Poniższy program robi dokładnie to samo:

for imie in imiona:
    print(imie)

Spróbujmy teraz czegoś bardziej skomplikowanego. Załóżmy, że mamy listę imion. Chcielibyśmy się dowiedzieć, jaka jest średnia ilość liter w tych imionach. Jak to zrobić? Najpierw będziemy musieli stworzyć drugą listę, w której umieścimy długość każdego z imion. Przyda nam się do tego funkcja `len()`.

imiona = ['Ala', 
          'Baltazar', 
          'Zenobiusz', 
          'Maks', 
          'Konstantyn', 
          'Jaś', 
          'Gosia',
          'Ewa']

# stwórzmy pustą listę, w której trzymać będziemy długości
dlugosc = []

# dla każdego z imion znajdźmy jego długość i umieśćmy na liście
for i in imiona:
    dlugosc_imienia = len(i)
    dlugosc.append(dlugosc_imienia)
    
dlugosc

Ok, otrzymaliśmy listę długość, w której przechowywane są długości poszczególnych imion. Żeby uzyskać średnią, możemy zsumować elementy listy po czym podzielić wynik przez ilość tych elementów. Nic prostszego:

sum(dlugosc) / len(dlugosc)

Widzimy, że nasze imiona średnio mają 5.625 litery.

## Pętla `for` a stringi

Ciekawostka - nic nie stoi na przeszkodzie, żeby użyć pętli `for` na napisie. Możemy na przykład policzyć, ile liter _z_ znajduje się w jakimś stringu.

napis = 'Brzęczyszczykiewicz'
licznik = 0

for i in napis:
    if i == "z":
        licznik += 1
        
licznik

Jak to działa? Najpierw deklarujemy zmienną z naszym napisem i drugą zmienną, w której przechowywać będziemy wynik naszego liczenia. Piszemy pętlę `for`, która zagląda do każdej litery w napisie `napis` i sprawdza, czy litera ta to _z_. Jeżeli tak, zwiększa wartość zmiennej `licznik` o 1. 

Na marginesie: zapis `licznik += 1` to skrót, który jest równoznaczny z `licznik = licznik + 1`.

## Czytanie danych z pliku

f = open('slowa.txt')

f = open('slowa.txt')
f.read()

f = open('slowa.txt')
f.read().splitlines()

## Czytanie danych z plików, moduły

Oprócz wprowadzania danych poprzez wpisywanie ich do kodu naszych programów,  możemy też (i powinniśmy!) korzystać z wielu innych sposobów wprowadzania danych. Jedną z najprostszych opcji jest pobieranie danych z plików.

Okazuje się, że w Pythonie nie ma wbudowanej funkcji, która pozwalałaby otwierać pliki. Nic straconego! Oprócz niewielkiej liczby wbudowanych funkcji Python posiada setki (o ile nie tysiące) funkcji, do których możesz uzyskać dostęp poprzez tzw. _moduły_. Moduł to po prostu zbiór funkcji, które coś robią. Sporo najpopularniejszych modułów już została zainstalowana poprzez Anacondę, możesz też doinstalować nowe jeśli tylko masz na to ochotę. My teraz skorzystamy z modułu `io` (skrót od _input/output_), który służy do wykonywania operacji na plikach.

Żeby skorzystać z funkcji wewnątrz modułu `io` wystarczy wpisać:

import io

Po wykonaniu tej komendy uzyskujemy dostęp do funkcji z modułu `io`. Skorzystamy teraz z funkcji z tego modułu do przeczytania danych z pliku, który stworzyłem wcześniej. Plik nazywa się `imiona.txt` i zawiera 100 najpopularniejszych imion nadawanych chłopcom w 2017 roku. Najpierw musimy otworzyć plik i umieścić go w zmiennej:

plik = open('imiona.txt')

Teraz stworzyliśmy zmienną, w której przechowywane jest odwołanie do pliku. Żeby przeczytać dane z pliku, możemy zastosować metodę `readlines()`.

imiona = plik.readlines()
imiona

Widzimy, że metoda `readlines()` pobrała nam dane z pliku, linijka po linijce, i umieściła na liście `imiona`. Jest tylko jeden szkopuł - z jakiegoś powodu do każdego imienia mamy doklejone `\n`. Czemu? Bo ten znak oznacza koniec linijki w pliku tekstowym (zwróć uwagę, że ostatni na liście Jeremi nie ma `\n`). Żeby się tego pozbyć, możemy zastosować metodę `replace()`, która zamienia fragment napisu na inny napis. W pierwszym argumencie podajemy to czego ma szukać a w drugim na co ma zamienić.

imiona_bez_n = []

for i in imiona:
    bez_n = i.replace('\n', '')
    imiona_bez_n.append(bez_n)

W porządku. Po tej operacji powinniśmy mieć już elegancką listę imion:

imiona_bez_n

Z tą listą możemy już robić wszystko to, co z innymi listami. Zastanawiasz się, które miejsce na liście frekwencyjnej zajmuje tradycyjne, staropolskie imie _Brajan_? Oto odpowiedź:

imiona_bez_n.index('Brajan')

