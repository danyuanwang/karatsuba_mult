from cases import Cases
from values import Values
import math
import random
def twoSAT(link):
    rules = Cases(link)
    answer = Values(rules)
    for i in range(int(math.log(answer.n, 2))):
        answer.generate()
        for j in range(int((answer.n ** 2) * 2)):
            print(i, j)
            result = rules.test_all_cases(answer.values)
            if(result == -1):
                return True
            
            answer.flip(int(random.choice(rules.cases[result])))
    return False

print(twoSAT("case3.txt"))
