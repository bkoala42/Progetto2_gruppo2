from Statistics import Statistics


def test_add():
    stat1 = Statistics("empity.txt")
    stat1.add("Ampere", 1)
    stat1.add("Tesla", 1)
    stat1.add("Edison", 2)

    stat2 = Statistics("empity.txt")
    stat2.add("Plank", 3)
    stat2.add("Newton", 5)
    stat2.add("Schrodinger", 8)
    stat2.add("Kepler", 13)

    if stat1.len() == 3 and stat2.len() == 4:
        print("Test test_add passed")
    else:
        print("Test test_add failed")


def test_len():
    stat = Statistics("empity.txt")
    if stat.len() == 0:
        stat.add("Plank", 1)
        stat.add("Schrodinger", 1)
        if stat.len() == 2:
            print("Test test_len passed")
        else:
            print("Test test_len failed")
    else:
        print("Test test_len failed")


def test_occurrences():
    stat = Statistics("empity.txt")
    if stat.occurrences() == 0:
        stat.add("Plank", 1)
        stat.add("Newton", 1)
        stat.add("Schrodinger", 2)
        stat.add("Kepler", 3)
        stat.add("Plank", 5)
        stat.add("Schrodinger", 8)
        if stat.occurrences() == 6:
            print("Test test_occurrences passed")
        else:
            print("Test test_occurrences failed")
    else:
        print("Test test_occurrences failed")


def test_average():
    stat = Statistics("empity.txt")
    if stat.occurrences() == 0:
        stat.add("Plank", 1)
        stat.add("Newton", 1)
        stat.add("Schrodinger", 2)
        stat.add("Kepler", 3)
        stat.add("Plank", 5)
        stat.add("Schrodinger", 8)
        if stat.average() == (1 + 1 + 2 + 3 + 5 + 8) / stat.len():
            print("Test test_average passed")
        else:
            print("Test test_average failed")
    else:
        print("Test test_average failed")


def test_median():
    stat1 = Statistics("empity.txt")
    stat2 = Statistics("empity.txt")
    r1, r2 = stat1.median()
    r3, r4 = stat2.median()
    if r1 == r2 == r3 == r4 is None:
        for i in range(9):
            stat1.add(chr(65 + i), i + 1)
            stat2.add(chr(74 + i), 10 + i)
        stat2.add(chr(74 + 8 + 1), 19)
        if stat1.len() % 2 == 1 and stat2.len() % 2 == 0:
            r1, r2 = stat1.median()
            r3, r4 = stat2.median()
            if r1 == "E" and r2 is None and r3 == "O" and r4 == "P":
                print("Test test_median passed")
            else:
                print("Test test_median failed")
        else:
            print("Test test_median failed")
    else:
        print("Test test_median failed")

#nel test genero un vettore che contiene l'alfabeto da A a J.
# il 25% percentile dovrebbe essere C ma l'algoritmo restituisce J in quanto mi genera in maniera errata il vettore su cui calcolare il percententile
#in particolare esce questo ['A', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B']
#ho lasciato una stampa nel codice di percentile() nella classe Statistic
def test_percentile_file_empity():
    stat = Statistics("empity.txt")
    if stat.len() == 0:
        for i in range(10):
            stat.add(chr(65 + i), i + 1)
        if stat.percentile(20) == "B":
            print("Test test_percentile_file_empity passed")
        else:
            print("Test test_percentile_file_empity failed")
    else:
        print("Test test_percentile_file_empity failed")

#In questo test il 25% percentile è Mila e quindi il risultato è giusto ma il vettore utilizzato per calcolarlo non rispetta l'ordine imposto
#ho lasciato una stampa nel codice di percentile() nella classe Statistic
def test_percentile_file_dataset():
    stat = Statistics("dataset.txt")
    if stat.len() != 0:
        if stat.percentile(25) == "Mila":
            print("Test test_percentile_file_dataset passed")
        else:
            print("Test test_percentile_file_dataset failed")
    else:
        print("Test test_percentile_file_dataset failed")


def test_percentile2_file_empity():
    stat = Statistics("empity.txt")
    if stat.len() == 0:
        for i in range(10):
            stat.add(chr(65 + i), i + 1)
        if stat.percentile2(25) == "C":
            print("Test test_percentile2_file_empity passed")
        else:
            print("Test test_percentile2_file_empity failed")
    else:
        print("Test test_percentile2_file_empity failed")
#
def test_percentile2_file_dataset():
    stat = Statistics("dataset.txt")
    if stat.len() != 0:
        if stat.percentile2(25) == "Mila":
            print("Test test_percentile2_file_dataset passed")
        else:
            print("Test test_percentile2_file_dataset failed")
    else:
        print("Test test_percentile2_file_dataset failed")


def test_mostFrequent():
    stat = Statistics("empity.txt")
    if stat.len() == 0 and stat.mostFrequent(2) is None:
        stat.add("Plank", 1)
        stat.add("Newton", 1)
        stat.add("Plank", 2)
        stat.add("Newton", 3)
        stat.add("Schrodinger", 5)
        stat.add("Plank", 8)
        stat.add("Newton", 13)
        if stat.mostFrequent(2)[0][1] == "Newton" and stat.mostFrequent(2)[1][1] == "Plank":
            print("Test test_mostFrequent passed")
        else:
            print("Test test_mostFrequent failed")
    else:
        print("Test test_mostFrequent failed")


def run_test_statistics():
    #test_add()
    #test_len()
    #test_occurrences()
    #test_average()
    #test_median()
    test_percentile_file_dataset()
    test_percentile_file_empity()
    test_percentile2_file_dataset()
    test_percentile2_file_empity()
    #test_mostFrequent()


if __name__ == "__main__":
    run_test_statistics()
