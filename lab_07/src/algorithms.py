def create_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
                
    return lps



def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = create_lps(pattern)
    indices = -1
    
    i = 0
    j = 0
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
            if j == m:
                indices = i - j
                break
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return indices


def kmp_search_count_comparisons(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = create_lps(pattern)
    comparisons = 0
    
    i = 0
    j = 0
    
    while i < n:
        if pattern[j] == text[i]:
            comparisons += 1
            i += 1
            j += 1
            
            if j == m:
                break
        else:
            comparisons += 1
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return comparisons



def bm_search(text, pattern):
    n = len(text)
    m = len(pattern)
    bad_char = {}
    indices = -1

    for i in range(m):
        bad_char[pattern[i]] = i

    i = 0
    while i <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[i+j]:
            j -= 1
      
        if j < 0:
            indices = i
            break
        else:
            if text[i+j] in bad_char:
                i += max(1, j - bad_char[text[i+j]])
            else:
                i += max(1, j)
    
    return indices


def bm_search_count_comparisons(text, pattern):
    n = len(text)
    m = len(pattern)
    bad_char = {}
    comparisons = 0

    for i in range(m):
        bad_char[pattern[i]] = i

    i = 0
    while i <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[i+j]:
            comparisons += 1
            j -= 1
        comparisons += 1
      
        if j < 0:
            break
        else:
            if text[i+j] in bad_char:
                i += max(1, j - bad_char[text[i+j]])
            else:
                i += max(1, j)
    
    return comparisons
