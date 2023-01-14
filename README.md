Nasz model miał na celu ocenę wpływu codziennych nawyków na szanse zdania egzaminu końcowego. 

Data set, który przyjęliśmy na początku zawierał nieistotne dane, które usunęliśmy:
- miejsce zamieszkania (miasto lub przedmieścia/wieś)
- wielkość rodziny (mniejsza lub równa 3; większa niż 3) 
- status związku rodziców (żyjący razem lub osobno)
- wykształcenie rodziców (rozbite na kolumny per rodzic)
- pracę rodziców (j.w.)
- powód wyboru danej szkoły (dobra lokalizacja, prestiż, jakość kształcenia lub inne)
- kto jest prawnym opiekunem ucznia (matka lub ojciec)
- do której szkoły chodzi (GP lub MS, skrót nazwy)
- relacje z rodziną

Naszym celem było obliczenie tylko egzaminu końcowego (kolumna G3), ale macierz korelacji pokazała nam, że wyniki na koniec pierwszego i drugiego semestru (odpowiednio G1 i G2) są bardzo determinujące czy ostatni egzamin również się powiedzie. Pomysł na to, aby nie usuwać tych kolumn oparliśmy na teście jaki wykonaliśmy, czyli usunięciu ich. Model drastycznie się mylił co do oceny jaką student dostał.

Trenowanie modelu wykazało, że najlepszym modelem był Random Forest Regressor, który uzyskał accuracy mierzone metodą MAE na poziomie 79,83%. Testy manualne wskazały, że w jego przypadku jest to wystarczające - dla pilnego ucznia, który uzyskał prawie maksymalne oceny ze wszystkich egzaminów (odpowiednio 19, 19 i 20), regresor wykazał wynik na poziomie 19 punktów, gdzie uczeń uzyskał faktycznie 20.

Poprawa modelu poprzez zwiększenie domyślnej ilości budowanych drzew (100 drzew) do 200 przy trenowaniu modelu, wykazało poprawę o 0,1 punktu procentowego. Jest to maksymalna wartość jaką udało nam się uzyskać.
