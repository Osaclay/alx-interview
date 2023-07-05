#!/usr/bin/python3
"""Solves the lock boxes puzzle """
def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    stack = [0]  # Start with the first box (boxes[0])

    while stack:
        box = stack.pop()
        if not visited[box]:
            visited[box] = True
            for key in boxes[box]:
                if key < n:
                    stack.append(key)

    return all(visited)
