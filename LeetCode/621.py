import heapq
import collections
from typing import List


def leastInterval(tasks: List[str], n: int) -> int:
    counter = collections.Counter(tasks)
    result=0
    while True:
        sub_count=0

        for task,_ in counter.most_common(n+1):
            sub_count+=1
            result+=1

            counter.subtract(task)
            counter+=collections.Counter()

        if not counter:
            break
        result+=n-sub_count+1
    return result

if __name__ == '__main__':
    print(leastInterval(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2))
