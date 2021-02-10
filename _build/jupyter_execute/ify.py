# Instrukcje warunkowe

Czasem chcielibyśmy, żeby nasz program zrobił coś tylko wtedy, gdy spełniony jest jakiś warunek. Wracając do analogii z pralką - pralka nie wykona wirowania jeśli naciśniemy odpowiedni przycisk. Tego rodzaju funkcję w Pythonie spełniają konstrukcje `if`, `elif` i `else`.

## If

Jeżeli chcemy, żeby jakiś fragment kodu wykonał się wtedy i tylko wtedy gdy jakiś warunek jest spełniony (ma wartość logiczną `True`), używamy konstrukcji `if`:

papugi = 11

if papugi > 10:
    print("Jest więcej niż 10 papug!")
    
if papugi < 1:
    print("Nie ma żadnej papugi. Papuga przestała być.")

Widzimy, że nasz program wykonał instrukcję po pierwszym `if`ie, zignorował zaś instrukcję po drugim. Stało się tak dlatego, że w pierwszej instrukcji jest prawdziwy, a w drugiej nie. Zwróć uwagę na składnię: po warunku mamy dwukropek, kolejna linia zaś zaczyna się od wcięcia (czterech spacji, jednego taba). To wcięcie oznacza *blok kodu*, fragment programu który traktowany jest jak jedna całość przez interpreter Pythona. W tym wypadku blok ma tylko jedną linijkę, ale może mieć dużo więcej, jak na przykładzie poniżej:

if "spam" != "eggs":
    spam = "eggs"
    eggs = "spam"
    if spam == "eggs":
        eggs = "eggs"
        spam = "spam"
        eggs = spam
        if "eggs" != spam:
            print("SPAAAAAM!!!")

## Else

Gdy chcemy, żeby program zrobił coś w razie spełnionego warunku, a coś zupełnie innego w przeciwnym wypadku, stosujemy komendę `else`.

food = "eggs"
if food == "spam":
    print("SPAAAM!")
else:
    print("And now for something completely different...")

### Elif

Jeśli chcemy przetestować wiele warunków po kolei, możemy skorzystać z komendy `elif` (skrót od *else if* czyli *w przedciwnym wypadku, jeżeli...*). W ten sposób tworzymy ciąg instrukcji warunkowych, a jeżeli skończymy na `else` to mamy pewność, że wykona się dokładnie jedna z instrukcji. Przykład poniżej pokazuje, w jaki sposób można wykonać różne fragmenty kodu dla różnych wartości jakiejś zmiennej - jest to bardzo częsta praktyka programistyczna. Uwaga na wcięcia!

imie = "Robin"
if imie == "Artur":
    print("Jestem Artur, Król Brytonów!")
elif imie == "Lancelot":
    print("Jestem Sir Lancelot, odważny!")
elif imie == "Robin":
    print("Jestem Sir Robin, nie-tak-odważny-jak-Lancelot!")
else:
    print("Nie bardzo wiem kim jestem...")