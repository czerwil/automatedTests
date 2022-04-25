# testyAutomatyczne
Testy automatyczne sklepu internetowego na oprogramowaniu Sellingo.

#Uruchomienie testów
1. Uruchomienie wszystkich testów
   1. Wykonujemy polecenie <b>$ pytest</b> w katalogu <i>tests</i>, gdzie znajdują się wszystkie testy
2. Uruchomienie wybranego zestawu testów
   1. Wykonujemy polecenie <b>$ pytest nazwa_pliku.py</b>, przykładowo <b> pytest test_listing.py</b> znajdując się w katalogu <i>tests</i>
3. Uruchomienie testów wraz z generowaniem danych do raportu allure
   1. Wykonujemy polecenie <b>$ py.test --alluredir=%ścieżka_katalogu_na_pliki% </b>
   2. Aby uruchomić raport wykonujemy polecenie <b>$ allure serve %ścieżka_katalogu_z_plikami%</b>
   3. Przed kolejnym procesem dobrze byłoby usunąć stare pliki i powtórzyć kroki 1 i 2.

#Przekazywanie testów do wykonania zdalnego
1. Wchodzimy na adres Selenoid-UI http://devsel.sellingo.pl:8080
2. Przechodzimy do zakładki <a href="http://devsel.sellingo.pl:8080/#/capabilities/">capabilities</a>
3. Wybieramy interesujący nas set, czyli przykładowo <b>chrome: 100.0</b> oraz <b>python</b>
4. Kopiujemy kod i wklejamy do pliku <i>driver_factory.py</i> - trzeba tam trochę to zmodyfikować, żeby było zgodne z patternem jak przy już istniejących opcjach
5. W pliku <i>conftest.py</i> w pierwszej linii funkcji <b>setup</b> dajemy nazwę naszej opcji, przykładowo <b>chrome</b> albo <b>firefox</b> 

        