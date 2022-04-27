<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Selenium_logo.svg/1280px-Selenium_logo.svg.png" alt="selenium" width="700" height="180">

<h1> testyAutomatyczne</h1>
Testy automatyczne UI sklepu internetowego na oprogramowaniu Sellingo na skórce Harmony (Prototype).

#Uruchomienie testów
1. Uruchomienie wszystkich testów
   1. Wykonujemy polecenie <b>$ pytest</b> znajdując się w katalogu <i>tests</i>, gdzie znajdują się wszystkie testy
2. Uruchomienie wybranego zestawu testów
   1. Wykonujemy polecenie <b>$ pytest nazwa_pliku.py</b>, przykładowo <b> pytest test_listing.py</b> znajdując się w katalogu <i>tests</i>
3. Uruchomienie testów wraz z generowaniem danych do raportu allure
   1. Wykonujemy polecenie <b>$ py.test --alluredir=%ścieżka_katalogu_na_pliki% </b>
   2. Aby wyświetlić raport wykonujemy polecenie <b>$ allure serve %ścieżka_katalogu_z_plikami%</b>
   3. Przed kolejnym procesem dobrze byłoby usunąć stare pliki i powtórzyć kroki 1 i 2.

#Przekazywanie testów do wykonania zdalnego
1. Wchodzimy na adres Selenoid-UI http://devsel.sellingo.pl:8080
2. Przechodzimy do zakładki <a href="http://devsel.sellingo.pl:8080/#/capabilities/">capabilities</a>
3. Wybieramy interesujący nas set, czyli przykładowo <b>chrome: 100.0</b> oraz <b>python</b>
4. Kopiujemy kod i wklejamy do pliku <i>driver_factory.py</i> - trzeba tam trochę to zmodyfikować, żeby było zgodne z patternem jak przy już istniejących opcjach
5. Wartość argumentu <b>command_executor</b> ustawiamy na <b>http://devsel.sellingo.pl:4444/wd/hub </b> - to tam przekierowywane będzie zdalne wykonanie testów
6. W pliku <i>conftest.py</i> w pierwszej linii funkcji <b>setup</b> dajemy nazwę naszej opcji, przykładowo <b>chrome</b> albo <b>firefox</b> 

#Wymagania
1. Python 3.7 lub nowszy  -> https://www.python.org/downloads/
2. Selenium w wersji 4 lub nowszej -> https://pypi.org/project/selenium/
3. Pytest -> https://docs.pytest.org/en/7.1.x/getting-started.html
4. Allure -> https://docs.qameta.io/allure/ https://pypi.org/project/allure-pytest/
   1. Do korzystania z allure potrzeba JRE i JDK -> https://www.oracle.com/java/technologies/downloads/ oraz https://java.com/pl/download/manual.jsp
5. Przy Selenium w wersji 4.2 (jeszcze nie nadeszło :D) zmienią się metody lokalizowania elementów na stronie i będzie trzeba zmienić trochę kod (z tego, co widze to nic wielkiego/trudnego, ale trzeba poswiecic na to troche czasu) -> https://www.selenium.dev/blog/2022/python-locators-se4/

#Uruchamianie kilku testów jednocześnie (parallel testing)
Tego nie udało mi się wdrożyć. Dało by to możliwość uruchamiania kilku testów jednocześnie obok siebie (czyli np. testy jednocześnie na kilku różnych przeglądarkach). Warto byłoby się temu bliżej przyjrzeć
i wdrożyć to. Tutaj znajduje się pomocny artykuł -> https://www.lambdatest.com/blog/pytest-tutorial-parallel-testing-with-selenium-grid/ 
Obecnie zestaw testów po wpisaniu komendy <b>pytest</b> będzie uruchamiał się na ustawionej w pliku <b>conftest.py</b> konfiguracji (argument przekazany w metodzie getDriver() będzie porównywany w pliku <b>driver_factory.py</b> i na tej podstawie będą uruchamiane testy w Selenoidzie).

#Inne informacje

Szczegóły dotyczące testów oraz metod w nich użytych znajdują się w plikach <b>Spis testów</b> oraz <b> Opis metod</b>. Testy są pisane według wzorca Page Object Pattern, który przynosi wymierne korzyści w utrzymaniu testów (przykładowo, gdy na skórce coś się zmieni i będzie trzeba zmienić jeden lokalizator to wystarczy go zmienić tylko w jednym miejscu w objekcie page, a nie we wszystkich testach, gdzie taki lokalizator byłby wpisany na sztywno). Mamy dwa główne katalogi: <i>pages</i> oraz <i>tests</i>. W katalogu <i>pages</i> 
znajdują się pliki odpowiadające stronom na sklepie, przykładowo listing, czy koszyk. W plikach znajdują się lokalizatory do elementów strony oraz metody, które są wykorzystywane przez testy. W katalogu <i> tests</i> znajdują się pliki z testami. Ogólnie przyjąłem zasadę, że jest jeden plik na jeden obszar sklepu, ale są wyjątki. W plikach z testami znajdują się przypadki testowe wraz z opisem, gdzie nawet osoba nietechniczna może zobaczyć mniej więcej, co dzieje się w teście. Co do testów to staram się zachować zasadę 1 asercja na 1 test, gdzie każdy test ma sprawdzić, czy konkretna funkcjonalność sklepu działa poprawnie, czyli na przykład w teście dodania do koszyka sprawdzam asercją, czy produkt, który dodałem do koszyka z karty produktu się w nim znajduje.

Jeśli będą jakieś pytania to proszę o kontaktowanie się ze mną
pod adresem e-mail 
<a href="mailto:konradczerwinski@icloud.com">konradczerwinski@icloud.com</a>
albo na firmowym Slacku (jeśli moje konto nie zostanie usunięte to będę 
tam zaglądał czasem z telefonu).
