from Statistics import Statistics

def test_add():
    stat1 = Statistics("empty.txt")
    stat1.add("Ampere", 1)
    stat1.add("Tesla", 1)
    stat1.add("Edison", 2)

    stat2 = Statistics("empty.txt")
    stat2.add("Plank", 3)
    stat2.add("Newton", 5)
    stat2.add("Schrodinger", 8)
    stat2.add("Kepler", 13)

    if stat1.len() == 3 and stat2.len() == 4:
        print("Test test_add passed")
    else:
        print("Test test_add failed")


def test_len():
    stat = Statistics("empty.txt")
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
    stat = Statistics("empty.txt")
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
    stat = Statistics("empty.txt")
    if stat.occurrences() == 0:
        stat.add("Plank", 1)
        stat.add("Newton", 1)
        stat.add("Schrodinger", 2)
        stat.add("Kepler", 3)
        stat.add("Plank", 5)
        stat.add("Schrodinger", 8)
        if stat.average() == (1 + 1 + 2 + 3 + 5 + 8) / stat.occurrences():
            print("Test test_average passed")
        else:
            print("Test test_average failed")
    else:
        print("Test test_average failed")


def test_median():
    stat = Statistics("empty.txt")
    if stat.len() == 0:
        for i in range(9):
            stat.add(chr(65 + i), i + 1)
        r1 = stat.median()
        if r1 == "E":
            print("Test test_median passed")
        else:
            print("Test test_median failed")
    else:
        print("Test test_median failed")

def test_percentile_file_empty():
    stat = Statistics("empty.txt")
    if stat.len() == 0:
        for i in range(10):
            stat.add(chr(65 + i), i + 1)
        if stat.percentile(20) == "B":
            print("Test test_percentile_file_empty passed")
        else:
            print("Test test_percentile_file_empty failed")
    else:
        print("Test test_percentile_file_empty failed")

def test_percentile_file_dataset():
    stat = Statistics("dataset.txt")
    if stat.len() != 0:
        if stat.percentile(25) == "Kaori":
            print("Test test_percentile_file_dataset passed")
        else:
            print("Test test_percentile_file_dataset failed")
    else:
        print("Test test_percentile_file_dataset failed")

def test_mostFrequent():
    stat = Statistics("empty.txt")
    if stat.len() == 0:
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
    test_add()
    test_len()
    test_occurrences()
    test_average()
    test_median()
    test_percentile_file_dataset()
    test_percentile_file_empty()
    test_mostFrequent()


if __name__ == "__main__":
    run_test_statistics()
