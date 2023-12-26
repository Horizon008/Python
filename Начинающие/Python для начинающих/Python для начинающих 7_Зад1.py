from pprint import pprint

def compare(s1, s2):
    s1, s2 = [s.lower() for s in [s1, s2]]
    ngrams = [s1[i:i + 3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count / max(len(s1), len(s2))

def int_val(s):
    try:
        return int(s)
    except ValueError:
        return "Неверный ввод: " + s

if __name__ == '__main__':
    out = []
    not_matching = []
    for a, b in [
            ('алгоритм', 'алгоритм'),
            ('алгоритм', 'алгоритмы'),
            ('алгоритм', 'алгоритмов'),
            ('стол', 'столик'),
            ('стол', 'стул'),
            ('маша', 'даша'),
            ('ольга', 'олег'),
            ('Ольга', 'Наташа'),
            ('маша', 'машенька'),
    ]:
        similarity = compare(a, b)
        if similarity < 0.5: 
            not_matching.append((a, b, similarity))
        out.append((a, b, similarity))

    pprint(out)
    pprint(not_matching)
    debug_info = [int_val(s) for s in ['старше', '30', 'но', '101']]
    pprint(debug_info)

