#!/usr/bin/env python3

import threading
from threading import Thread, current_thread
from queue import PriorityQueue

q = PriorityQueue()


def helper(func, index, args):
    print(f"About to invoke {func.__name__} on {args}")
    output = func(*args)
    print(f"Done invoking, got {output}")
    q.put((index, output))


def threadify(func, all_args):
    # Launch the threads
    for index, args in enumerate(all_args):
        Thread(target=helper, args=(func, index, args)).start()

    # Wait for (join) the threads
    while len(threading.enumerate()) > 1:
        for t in threading.enumerate():
            if current_thread() == t:
                continue
            t.join(0.1)

    # Collect the thread outputs
    output = []
    while not q.empty():
        index, result = q.get()
        output.append(result)

    return output


if __name__ == '__main__':
    def add(a, b):
        return a + b

    print(threadify(add, [(10, 3),
                          (20, 4),
                          (30, 5)]))
