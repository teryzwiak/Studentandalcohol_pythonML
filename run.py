class ankieta: 
    def gen_ankieta():
        print("Oceń swoje możliwości zdania roku")
        # age, traveltime1/5, studytime1/5, failures0/3, schoolsup0/1, famsup0/1, paid0/1, acticities0/1, nursery0/1, higher0/1, internet0/1, romantic0/1, freetime1/5, gout1/5, dalc1/5, wlac1/5, health1/5, absences0/93
        age = int(input("Podaj wiek: "))
        traveltime = int(input("Podaj czas podróży(1/5): "))
        studytime = int(input("Podaj czas nauki(1/5): "))
        failures = int(input("Podaj ilość niezdanych egzaminów(1/5): "))
        schoolsup = int(input("Czy miałeś wsparcie edukacyjne(0/1): "))
        famsup = int(input("Czy miałeś wsparcie rodziny(0/1): "))
        paid = int(input("Czy płaciłes za dodatkowe zajęcie(0/1): "))
        activities = int(input("Czy miałeś dodatkowe zajęcia(0/1): "))
        nursery = int(input("Czy chodziłeś do przedszkola(0/1): "))
        higher = int(input("Czy planujesz iść wyżej w edukacji(0/1): "))
        internet = int(input("Czy masz dostęp do internetu(0/1): "))
        romantic = int(input("Czy jesteś w jakiejś relacji(0/1): "))
        freetime = int(input("Podaj ilośc czasu wolnego(1/5): "))
        gout = int(input("Podaj ilość czasu na wyjścia(1/5: "))
        dalc = int(input("Podaj ile alkoholu spożywasz dziennie(1/5): "))
        walc = int(input("Podaj ile alkoholu spożywasz tygodniowo(1/5): "))
        health = int(input("Podaj jakość zdrowia(1/5): "))
        absences = int(input("Podaj ilość nieobecności(0/51): "))

        if absences > 51:
            wynik = 0
        return wynik
ankieta.gen_ankieta()
with open('alcholic_regressor_model.pickle', 'rb') as handle:
    clf = pickle.load(handle)

wynik = clf.predict([[age, traveltime, studytime, failures, schoolsup, famsup, paid, activities, nursery, higher, internet, romantic, freetime, gout, dalc, walc, health, absences]])
#wynik =* 5  
print("Twój wynik:")
print(wynik)