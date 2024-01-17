from collections import deque

queue = deque(['Zero', 'One', 'Two'])
print(queue)
queue.pop()

queue.append('Four')
queue.append('Five')
print(queue)

queue.appendleft('Minus One')
print(queue)

queue.popleft()
print(queue)