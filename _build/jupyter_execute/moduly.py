# Moduły

Jedną z największych zalet Pythona jest jego modularność. Podstawowy Python zawiera tylko napotrzebniejsze funkcje, natomiast jego możliwości są znacznie rozszerzone poprzez _moduły_. Moduł to nic innego jak zbiór funkcji służących do realizacji określonych czynności. Wiele modułów dostępnych jest razem z podstawową instalacją Pythona (<https://docs.python.org/3/py-modindex.html>), jeszcze więcej zanistalowanych jest domyślnie wraz z Anacondą (<https://docs.anaconda.com/anaconda/packages/old-pkg-lists/4.3.1/py35/>). Możesz też instalować dodatkowe moduły poprzez Anacondę (<https://conda.io/docs/user-guide/tasks/manage-pkgs.html>).

## Moduł `pandas`

Jeżeli dany moduł jest zainstalowany na twoim komputerze, musisz go zaimportować zanim skorzystasz z jego funkcji. Zaimportujemy teraz moduł, który służy do analizy danych w Pythonie. Aby zaimportować moduł stosujemy słowo kluczowe `import` i nazwę modułu. Aby uniknąć konfliktów w nazwach funkcji najczęściej podajemy też krótką nazwę (alias), po której identyfikować będziemy funkcje z danego modułu. Zwyczajowo dla `pandas` jest to `pd`. Całość wygląda tak:

import pandas as pd

Dzięki tej linijce zaimportowane i dostępne są wszystkie funkcje odstępne w module `pandas`. Żeby z nich skorzystać, musimy ich nazwy poprzedzić prefiksem `pd.`. Skorzystamy teraz z funkcji `read_csv`, która otwiera plik `csv` znajdujący się na dysku, odczytuje go i umieszcza w czymś, co nazywa się `pandas dataframe` - strukturze służącej do przechowywania danych w formie tabel. Załadujemy plik `movies.csv` dostępny w repo przedmiotu w folderze `data/drugs`. W pliku tym znajdują się dane dotyczące spożycia substancji psychoaktywnych u ludzi w różnym wieku. Poniżej znajdziesz opis zmiennych w tym pliku (dostępny też w `README.md` w katalogu `drugs`).

## Drug Use By Age

This directory contains data behind the story [How Baby Boomers Get High](http://fivethirtyeight.com/datalab/how-baby-boomers-get-high/). It covers 13 drugs across 17 age groups.

Source: [National Survey on Drug Use and Health from the Substance Abuse and Mental Health Data Archive](http://www.icpsr.umich.edu/icpsrweb/content/SAMHDA/index.html).

Header | Definition
---|---------
`alcohol-use` | Percentage of those in an age group who used alcohol in the past 12 months
`alcohol-frequency` | Median number of times a user in an age group used alcohol in the past 12 months
`marijuana-use` | Percentage of those in an age group who used marijuana in the past 12 months
`marijuana-frequency` | Median number of times a user in an age group used marijuana in the past 12 months
`cocaine-use` | Percentage of those in an age group who used cocaine in the past 12 months
`cocaine-frequency` | Median number of times a user in an age group used cocaine in the past 12 months
`crack-use` | Percentage of those in an age group who used crack in the past 12 months
`crack-frequency` | Median number of times a user in an age group used crack in the past 12 months
`heroin-use` | Percentage of those in an age group who used heroin in the past 12 months
`heroin-frequency` | Median number of times a user in an age group used heroin in the past 12 months
`hallucinogen-use` | Percentage of those in an age group who used hallucinogens in the past 12 months
`hallucinogen-frequency` | Median number of times a user in an age group used hallucinogens in the past 12 months
`inhalant-use` | Percentage of those in an age group who used inhalants in the past 12 months
`inhalant-frequency` | Median number of times a user in an age group used inhalants in the past 12 months
`pain-releiver-use` | Percentage of those in an age group who used pain relievers in the past 12 months
`pain-releiver-frequency` | Median number of times a user in an age group used pain relievers in the past 12 months
`oxycontin-use` | Percentage of those in an age group who used oxycontin in the past 12 months
`oxycontin-frequency` | Median number of times a user in an age group used oxycontin in the past 12 months
`tranquilizer-use` | Percentage of those in an age group who used tranquilizer in the past 12 months
`tranquilizer-frequency` | Median number of times a user in an age group used tranquilizer in the past 12 months
`stimulant-use` | Percentage of those in an age group who used stimulants in the past 12 months
`stimulant-frequency` | Median number of times a user in an age group used stimulants in the past 12 months
`meth-use` | Percentage of those in an age group who used meth in the past 12 months
`meth-frequency` | Median number of times a user in an age group used meth in the past 12 months
`sedative-use` | Percentage of those in an age group who used sedatives in the past 12 months
`sedative-frequency` | Median number of times a user in an age group used sedatives in the past 12 months


## Import

drugs = pd.read_csv('data/drugs/drugs.csv')

## Różne sposoby pokazywania `df`

drugs

drugs.head()

drugs.tail()

drugs.info()

## Wybieranie poszczególnych kolumn

drugs['age']

drugs['alcohol-frequency']

drugs[['age', 'marijuana-use', 'marijuana-frequency']]

## Wybieranie wierszy

drugs[0:5]

drugs[10:]

drugs[-3:]

## `loc`

Lokalizowanie po etykiecie. Wprowadź dwie listy rozdzielone przecinkiem. Pierwsze rzędy, drugie kolumny.

drugs.loc[6:8, ['age', 'cocaine-use']]

drugs.loc[8, :]

## `iloc`

Lokalizowanie po indeksach. Tak samo jak poprzednio, wprowadź dwie listy rozdzielone przecinkiem. Pierwsze rzędy, drugie kolumny.

drugs.iloc[:5, 6:10]

drugs.iloc[[1, 3, 8], 2::2]

## Proste statystyki

drugs['n'].sum()

drugs['marijuana-use'].max()

drugs.iloc[drugs['marijuana-frequency'].idxmax(), :]

drugs.iloc[drugs['alcohol-frequency'].idxmax(), :]

