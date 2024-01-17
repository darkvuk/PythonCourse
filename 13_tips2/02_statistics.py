import statistics


# mean - srednja vrijednost
marks = [1, 6, 9, 23, 2]
print(statistics.mean(marks))


# median (parni br. elemenata niza)
# vrijednost u sredini kad se niz sortira u rastucem poretku
marks = [1, 6, 9, 23, 2]
print(statistics.median(marks))


# median (neparan br. elemenata niza)
# prosjek dva broja u sredini kad se niz sortira u rastucem poretku
# median_low - vraca manji broj iz medijane
# median_high - vraca veci broj iz medijane
marks = [1, 6, 9, 7, 23, 2]
print(statistics.median(marks))
print(statistics.median_low(marks))
print(statistics.median_high(marks))