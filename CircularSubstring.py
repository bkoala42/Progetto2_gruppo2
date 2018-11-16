from TdP_collections.text.find_kmp import find_kmp


def circular_substring(P, T):
    """
    TODO insert comments
    :param P:
    :param T:
    :return:
    """
    m, n = len(P), len(T)
    new_str = T[m-1:n] + T[0:m-1]
    if find_kmp(new_str, P) != -1:
        return True
    return False

