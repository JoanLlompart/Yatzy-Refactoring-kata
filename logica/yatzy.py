
@staticmethod
def yatzy(dado):
    counts = [0]*(len(dado)+1)
    for die in dado:
        counts[die-1] += 1
    for n in range(len(counts)):
        if counts[n] == 5:
            return 50
    return 0

