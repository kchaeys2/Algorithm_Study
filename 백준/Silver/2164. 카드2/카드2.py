from typing import Deque


N = int(input())

cards = Deque([i for i in range(1,N+1)])

while len(cards) > 1:
    cards.popleft()
    cards.rotate(-1)

print(cards[0])
