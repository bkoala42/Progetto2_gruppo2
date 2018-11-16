from TdP_collections.text.find_kmp import find_kmp


def circular_substring(P, T):
    m, n = len(P), len(T)
#    new_str = T[m-1:n] + T[0:m-1]
    new_str = T[n-(m+2):n] + T[0:2]
    if find_kmp(new_str, P) != -1:
        return True
    return False

