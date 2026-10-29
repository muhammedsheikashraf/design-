"""Question 1: Concurrent Linked List, Stack, and Queue.
Run this file directly. Each structure protects shared data with a lock.
"""
import threading
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ConcurrentLinkedList:
    def __init__(self):
        self.head = None
        self.lock = threading.Lock()

    def insert(self, data):
        with self.lock:
            node = Node(data)
            node.next = self.head
            self.head = node

    def display(self):
        with self.lock:
            values = []
            current = self.head
            while current:
                values.append(current.data)
                current = current.next
            return values


class ConcurrentStack:
    def __init__(self):
        self.items = []
        self.lock = threading.Lock()

    def push(self, item):
        with self.lock:
            self.items.append(item)

    def pop(self):
        with self.lock:
            return self.items.pop() if self.items else None

    def display(self):
        with self.lock:
            return self.items.copy()


class ConcurrentQueue:
    def __init__(self):
        self.items = deque()
        self.lock = threading.Lock()

    def enqueue(self, item):
        with self.lock:
            self.items.append(item)

    def dequeue(self):
        with self.lock:
            return self.items.popleft() if self.items else None

    def display(self):
        with self.lock:
            return list(self.items)


def list_worker(linked_list, start):
    for value in range(start, start + 3):
        linked_list.insert(value)


def stack_worker(stack, start):
    for value in range(start, start + 3):
        stack.push(value)


def queue_worker(queue, start):
    for value in range(start, start + 3):
        queue.enqueue(value)


def run_threads(worker, structure):
    threads = [
        threading.Thread(target=worker, args=(structure, 1)),
        threading.Thread(target=worker, args=(structure, 4)),
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    linked_list = ConcurrentLinkedList()
    run_threads(list_worker, linked_list)
    print("Concurrent Linked List:", linked_list.display())

    stack = ConcurrentStack()
    run_threads(stack_worker, stack)
    print("Concurrent Stack:", stack.display())
    print("Popped item:", stack.pop())

    queue = ConcurrentQueue()
    run_threads(queue_worker, queue)
    print("Concurrent Queue:", queue.display())
    print("Dequeued item:", queue.dequeue())
