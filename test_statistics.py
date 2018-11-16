from Statistics import Statistics


def test_add():
    stat1 = Statistics(False)
    stat1.add("Armando", 1)
    stat1.add("Mei", 1)
    stat1.add("Ilia", 2)

    stat2 = Statistics(False)
    stat2.add("Plank", 3)
    stat2.add("Newton", 5)
    stat2.add("Schrodinger", 8)
    stat2.add("Kepler", 13)

    if stat1.len() == 3 and stat2.len() == 4:
        print("Test test_add passed")
    else:
        print("Test test_add failed")


def test_len():
    stat = Statistics(False)
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
    stat = Statistics(False)
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
    stat = Statistics(False)
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
    stat1 = Statistics(False)
    stat2 = Statistics(False)
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


def test_percentile():
    stat = Statistics(False)
    if stat.len() == 0:
        for i in range(10):
            stat.add(chr(65 + i), i + 1)
        if stat.percentile(20) == "B":
            print("Test test_percentile passed")
        else:
            print("Test test_percentile failed")
    else:
        print("Test test_percentile failed")


def test_mostFrequent():
    stat = Statistics(False)
    if stat.len() == 0 and stat.mostFrequent(2) is None:
        stat.add("Plank", 1)
        stat.add("Newton", 1)
        stat.add("Plank", 2)
        stat.add("Newton", 3)
        stat.add("Schrodinger", 5)
        stat.add("Plank", 8)
        stat.add("Newton", 13)
        # tmp = stat.mostFrequent(2)
        if stat.mostFrequent(2)[0] == "Plank" and stat.mostFrequent(2)[1] == "Newton":
            print("Test test_mostFrequent passed")
        else:
            print("Test test_mostFrequent failed")
    else:
        print("Test test_mostFrequent failed")


def run_test_statistics():
    test_add()
    test_len()
    test_occurrences()
    test_average()
    test_median()
    test_percentile()
    test_mostFrequent()


if __name__ == "__main__":
    run_test_statistics()
