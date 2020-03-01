To jest tłumaczenie ściągi przygotowanej przez Adama Pritcharda i dostępnej w oryginale [tutaj](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). Jako, że tamta ściąga była przygotowana dla [Markdown Here](https://markdown-here.com/), usunąłem z niej rzeczy specyficzne i zostawiłem tylko to, co powinno działać własciwie w każdej specyfikacji MD.

## Nagłówki

```no-highlight
# H1
## H2
### H3
#### H4
##### H5
###### H6

Alternatywnie, dla H1 i H2, można zastosować niby-podkreślenie:

Alt-H1
======

Alt-H2
------
```

# H1
## H2
### H3
#### H4
##### H5
###### H6

Alternatywnie, dla H1 i H2, można zastosować niby-podkreślenie:

Alt-H1
======

Alt-H2
------



## Wyróżnienia

```
Kursywa, za pomocą *gwiazdek* lub _podkreśleń_.

Pogrubienie, za pomocą **gwiazdek** lub __podkreśleń__.

Połączenie kursywy i pogrubienia za pomocą **gwiazdek i _podkreśleń_**

Przekreślenie robi się podwójną tyldą. ~~Wymaż to.~~
```

Kursywa, za pomocą *gwiazdek* lub _podkreśleń_.

Pogrubienie, za pomocą **gwiazdek** lub __podkreśleń__.

Połączenie kursywy i pogrubienia za pomocą **gwiazdek i _podkreśleń_**

Przekreślenie robi się podwójną tyldą. ~~Wymaż to.~~



## Listy

(W tych przykładach spacje wykorzystane do wcięć oznaczono kropkami: ⋅)

```no-highlight
1. Pierwszy element listy numerowanej
2. Kolejny element
⋅⋅* Nieponumerowana pod-lista. 
1. Nieważne jakie cyfry, ważne żeby były cyfry (markdown sam numeruje)
⋅⋅1. Numerowana podlista
4. Jeszcze jeden element.

⋅⋅⋅Możesz zrobić poprawnie wcięte akapity wewnątrz elementów listy. Zwróć uwagę na pustą linię powyżej i na więcie (co najmniej jedna spacja, jednak trzy wyglądają lepiej w surowym Markdownie).

⋅⋅⋅By zrobić podział linii bez nowego paragrafu, potrzebujesz dwóch spacji wcięcia.⋅⋅
⋅⋅⋅Zwróć uwagę, że ta linia jest osobno, ale wewnątrz tego samego akapitu⋅⋅

* Nienumerowane listy mogą używać gwiazdek
- Albo minusów
+ Albo plusów
```

1. Pierwszy element listy numerowanej
2. Kolejny element
  * Nieponumerowana pod-lista. 
1. Nieważne jakie cyfry, ważne żeby były cyfry (markdown sam numeruje)
  1. Numerowana podlista
4. Jeszcze jeden element.

   Możesz zrobić poprawnie wcięte akapity wewnątrz elementów listy. Zwróć uwagę na pustą linię powyżej i na więcie (co najmniej jedna spacja, jednak trzy wyglądają lepiej w surowym Markdownie).

   By zrobić podział linii bez nowego paragrafu, potrzebujesz dwóch spacji wcięcia.
   Zwróć uwagę, że ta linia jest osobno, ale wewnątrz tego samego akapitu

* Nienumerowane listy mogą używać gwiazdek
- Albo minusów
+ Albo plusów


## Linki

Linki tworzymy na dwa sposoby.

```no-highlight
[Jestem linkiem](https://www.google.com)

[Jestem linkiem z tytułem](https://www.google.com "Google's Homepage")

[Jestem linkiem relatywnym](../blob/master/LICENSE)

Można też umieścić URL w nawiasach trójkątnych.
<http://www.example.com>
```

[Jestem linkiem inline](https://www.google.com)

[Jestem linkiem inline z tytułem](https://www.google.com "Google's Homepage")

[Jestem linkiem relatywnym](../blob/master/LICENSE)

Można też umieścić URL w nawiasach trójkątnych.
<http://www.example.com>



## Images

```
Tak wstawia się obrazki (najedź kursorem, by zobaczyć tekst):

Inline-style: 
![Tekst alternatywny](https://github.com/dcurtis/markdown-mark/raw/master/png/66x40.png "Logo Title Text 1")
```

Tak wstawia się obrazki (najedź kursorem, by zobaczyć tekst):

Inline-style: 
![Tekst alternatywny](https://github.com/dcurtis/markdown-mark/raw/master/png/66x40.png "Logo Title Text 1")



## Kod i kolorowanie składni

Bloki kodu są częścią specyfikacji Markdown, jednak kolorowanie składni nie. Jednak wiele rendererów wspiera kolorowanie składni. Które dokładnie języki są wspierane i jak dokładnie należy je oznaczać - to już zależy od renderera.

```no-highlight
`Kod` w linijce tekstu jest w `apostrofach` (czy tak na pewno to się nazywa?:P).
```

`Kod` w linijce tekstu jest w `apostrofach` (czy tak na pewno to się nazywa?:P).

Bloki kodu są otoczone linijką zawierającą trzy apostrofy i, opcjonalnie, nazwę języka.

<pre lang="no-highlight"><code>```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
 
```python
s = "Python syntax highlighting"
print s
```
 
```
Język niezdefiniowany więc nie ma kolorowania składni.
```
</code></pre>

Javascript:


```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```


Python:

```python
s = "Python syntax highlighting"
print s
```


Niezdefiniowany język:

```
Język niezdefiniowany więc nie ma kolorowania składni.
```
