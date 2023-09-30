
import testcheck


def canBeMadeNonDecreasing(l):
    i = 1
    length = len(l)
    patternBreakCount = 0
    threshold = 1
    while i < length:
        if l[i] < l[i-1]:
            patternBreakCount += 1
        if patternBreakCount > threshold:
            return False
        i+=1
    return True

def test():
    l = [10, 5, 7]
    res = canBeMadeNonDecreasing(l)
    testcheck.test_check(True, res, "check true case.")

    testcheck.test_check(
        False,
        canBeMadeNonDecreasing([10, 5, 1]),
        "check false case"
    )
test()