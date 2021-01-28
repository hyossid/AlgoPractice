def DFS(tickets, city, visit, depth):
    if len(tickets) + 1 == len(visit):
        return 0

    visit.append(city)

    for ticket in tickets:

        if city == ticket[0]:
            target = ticket[1]

            ticket[0] = False
            ticket[1] = False
            #  print(target)

            DFS(tickets, target, visit, depth + 1)


def solution(tickets):
    answer = []
    new_tickets = sorted(tickets, key=(lambda x: x[1]))

    DFS(new_tickets, "ICN", answer, 0)

    # BFS(tickets,"ICN",answer)
    # 1. BFS
    # 2.
    return answer

if __name__ == '__main__':
    print(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))