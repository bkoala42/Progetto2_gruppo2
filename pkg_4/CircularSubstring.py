from TdP_collections.text.find_kmp import find_kmp


def circular_substring(P, T):
    """
    To research a substring that is hypothetically circular or not we need to append a substring
    of the input text string of length m (len(pattern)) to the tail of the input text string.
    Complexity O(n+m)
    :param P: pattern string to search for
    :param T: input text string to research in
    :return: bool indicating whether or not the pattern is present or not
    """
    m, n = len(P), len(T)
    new_str = T + T[0:m]
    if find_kmp(new_str, P) != -1:
        return True
    return False
