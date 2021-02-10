# Operatory

## Operatory porównania

W Pythonie możemy porównywać obiekty ze sobą. Służą do tego operatory porówania. Rezultatem działania takiego operatora jest wartość logiczna (typu `bool`) - albo prawda (`True`) albo fałsz (`False`). Najprościej to zrozumieć na prostych przykładach z matematyki, ale musisz wiedzieć, że porównywać możemy nie tylko liczby, ale też napisy a nawet wartości logiczne.

3 > 2 # większe

3 < 2 # mniejsze

3 >= 2 # większe równe

2 <= 2 # mniejsze równe

2 == 2 # równe (uwaga na podwójny znak równości!!!)

2 != 2 # nierówne

## Operatory logiczne

Na wartościach logicznych możemy wykonywać operacje znane z logiki formalnej. Są to:

- `and` czyli koniunkcja (prawdziwa wtedy, gdy obie strony są prawdziwe)
- `or` czyli alternatywa (prawdziwa wtedy, gdy co najmniej jedna strona jest prawdziwa)
- `not` czyli negacja (wartość przeciwna do wartości po prawej stronie operatora)

Kilka prostych przykładów

True and True

True and False

False or True

False or False

not True

not False

Oczywiście najczęściej operatorów logicznych używamy jednocześnie z operatorami porównania. Na przykład:

a = 2
b = 3
c = 4
d = True

a < b and b < c

a > b or c > b 

a == b or not d

not a == c and a > d

Tego typu testy logiczne zdażają się w programowaniu bardzo często. Zanalizuj poniższe przykłady i spróbuj odgadnąć, jaka jest ich wartość logiczna bez korzystania z interpretera Pythona:

```Python
2 * 3 > 3 * 2 or 2 == 3 or 3 != 3
not (not True and not True) and not (False or not True)
30 % 2 == 0 and 45 % 3 > 0
[True, False, True] and not [False, False, False]
```