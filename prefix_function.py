def find_all_prefixes(s: str) -> list:
    prefixes = []
    for i in range(len(s)):
        prefixes.append(s[:i+1])
    return prefixes

def find_all_suffixes(s: str) -> list:
    suffixes = []
    for i in range(len(s)):
        if len(s[i:]) != len(s):
            suffixes.append(s[i:])
        else:
            suffixes.append('')
    return suffixes

def prefix_func(s: str) -> list:
    pref_result = []
    prefixes = find_all_prefixes(s)

    for i in range(len(prefixes)):       # len1() == len2()
        prefixes_inner = find_all_prefixes(prefixes[i])
        suffixes_inner = find_all_suffixes(prefixes[i])

        print(i, prefixes_inner, suffixes_inner)

        k = 0
        for j in range(len(prefixes_inner)):       # len1() == len2()
            for c in range(len(prefixes_inner)):
                if prefixes_inner[j] == suffixes_inner[c]: k += len(prefixes_inner[j])
        pref_result.append(k)

    return pref_result

if __name__ == '__main__':
    print(prefix_func('ASDFGASDFG'))