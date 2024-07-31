from typing import Dict, List
from copy import deepcopy
from bisect import insort_right


def solve_a():
    OLD_MOEDAS = [1, 5, 10, 25, 50, 100]

    dummy = list(0 for _ in range(len(OLD_MOEDAS) + 1))

    range_combinations = list(i for i in range(1, 100 + 1) if i not in OLD_MOEDAS)

    a = {}
    for new_moeda in range_combinations:
        cur_moedas = deepcopy(OLD_MOEDAS)
        insort_right(cur_moedas, new_moeda)
        #
        moedas_utilizadas: Dict[int, List[int]] = dict(
            (v, deepcopy(dummy)) for v in range(1, 100 + 1)
        )
        for v in range(1, 100 + 1):
            counter = moedas_utilizadas[v]
            for pos, m in enumerate(reversed(cur_moedas)):
                qtd = 0
                while m <= v:
                    v -= m
                    qtd += 1
                counter[pos] = qtd
        #
        #
        a[new_moeda] = sum([sum(v) for v in moedas_utilizadas.values()]) / 100

    print(sorted(a.items(), key=lambda x: x[1])[:10])
    # First
    # (2, 3.41)
    # (3, 3.41)
    # Second
    # (4, 3.61)
    # Third
    # (7, 3.73)
    # (8, 3.73)
