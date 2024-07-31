from typing import Dict, List
from copy import deepcopy
from bisect import insort_right
from itertools import combinations


def solve_b():
    OLD_MOEDAS = [1, 5, 10, 25, 50, 100]

    dummy = list(0 for _ in range(len(OLD_MOEDAS) + 2))

    range_combinations = list(i for i in range(1, 100 + 1) if i not in OLD_MOEDAS)

    a = {}
    for new_moedas in combinations(range_combinations, 2):
        cur_moedas = deepcopy(OLD_MOEDAS)
        for new_moeda in new_moedas:
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
        a[new_moedas] = sum([sum(v) for v in moedas_utilizadas.values()]) / 100

    print(sorted(a.items(), key=lambda x: x[1])[:10])
    # First
    # ((2, 37), 3.05)
    # ((2, 38), 3.05)
    # Second
    # ((2, 36), 3.07)
    # ((2, 39), 3.07)
    # ((3, 36), 3.07)
    # ((3, 37), 3.07)
    # ((3, 38), 3.07)
    # ((3, 39), 3.07)
