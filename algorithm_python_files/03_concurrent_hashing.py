"""Question 3A: Concurrent Hash Table using a lock and separate chaining."""
import threading


class ConcurrentHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.lock = threading.Lock()

    def _index(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._index(key)
        with self.lock:
            for position, (old_key, _) in enumerate(self.table[index]):
                if old_key == key:
                    self.table[index][position] = (key, value)
                    return
            self.table[index].append((key, value))

    def search(self, key):
        index = self._index(key)
        with self.lock:
            for stored_key, value in self.table[index]:
                if stored_key == key:
                    return value
            return None

    def display(self):
        with self.lock:
            return [bucket.copy() for bucket in self.table]


def worker(table, start):
    for key in range(start, start + 3):
        table.insert(key, key * 10)


if __name__ == "__main__":
    table = ConcurrentHashTable()
    threads = [
        threading.Thread(target=worker, args=(table, 1)),
        threading.Thread(target=worker, args=(table, 4)),
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print("Hash table:", table.display())
    print("Search key 3:", table.search(3))
