from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    queue = deque(people)
    
    while queue:
        if len(queue) > 1:
            if queue[0] + queue[-1] <= limit:
                queue.popleft()
        queue.pop()
        answer += 1
    
    return answer