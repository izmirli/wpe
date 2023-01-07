"""Threadify."""
import threading
from queue import PriorityQueue
from typing import Callable


def threadify(func: Callable, args_list: list[tuple]) -> list:
    """Run given function on given arguments and return results list.

    :param func: the function that should be invoked
    :param args_list: list of tuples, each representing arguments set for the function
    :return: list of function results in same order args were given
    """
    tasks = PriorityQueue()

    def pq_func(priority: int, q: PriorityQueue, *args):
        """Wraperr to add result to given PriorityQueue with given priority."""
        res = func(*args)
        q.put((priority, res))

    threads = []
    for p, thread_args in enumerate(args_list):
        this_thread = threading.Thread(target=pq_func, args=(p, tasks) + thread_args)
        threads.append(this_thread)
        this_thread.start()

    for this_thread in threads:
        this_thread.join()

    results = []
    while not tasks.empty():
        _, data = tasks.get()
        results.append(data)

    return results


if __name__ == '__main__':
    twice = lambda x: x * 2
    test_vals = (0, 3, 21)
    print(f"twice for {test_vals} is: {threadify(twice, [(v,) for v in test_vals])}")
