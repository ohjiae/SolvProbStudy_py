def check_good_seq(_seq):
    for i in range(1, 1 + len(_seq) // 2):
        if _seq[-i:] == _seq[-(i * 2):-i]:
            return False
    return True


def make_good_seq(_seq):
    if len(_seq) == N:
        return _seq

    return check_good_seq(_seq + '1') and make_good_seq(_seq + '1') or \
        check_good_seq(_seq + '2') and make_good_seq(_seq + '2') or \
        check_good_seq(_seq + '3') and make_good_seq(_seq + '3')


N = int(input())
print(make_good_seq(''))
