from typing import Dict, List
from copy import deepcopy
from itertools import combinations


def solve_c():
    NUMBER_OF_COINS = 5
    dummy = list(0 for _ in range(NUMBER_OF_COINS))

    range_combinations = list(i for i in range(2, 100 + 1))

    a = {}
    count = 0
    for new_moedas in combinations(range_combinations, NUMBER_OF_COINS - 1):
        count += 1
        if (count % 10_000) == 0:
            print(count)
        #
        moedas_utilizadas: Dict[int, List[int]] = dict(
            (v, deepcopy(dummy)) for v in range(1, 100 + 1)
        )
        for v in range(1, 100 + 1):
            counter = moedas_utilizadas[v]
            for pos, m in enumerate(reversed(new_moedas)):
                qtd = 0
                while m <= v:
                    v -= m
                    qtd += 1
                counter[pos] = qtd
            else:
                # Number of number 1 coins
                counter[-1] = v
        #
        #
        a[new_moedas] = sum([sum(v) for v in moedas_utilizadas.values()]) / 100

    # NOTE(hspadim): it does not print the value '1' coin
    print(sorted(a.items(), key=lambda x: x[1])[:10])
    # First
    # ((1, 3, 7, 18, 45), 3.5)
