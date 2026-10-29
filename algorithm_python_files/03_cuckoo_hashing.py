"""Question 3B: Basic Cuckoo Hashing with two tables and two hash functions.
If insertion cycles or exceeds the displacement limit, insertion fails;
a production implementation should rehash using new hash functions or a larger table.
"""


class CuckooHashing:
    def __init__(self, size=11):
        self.size = size
        self.table1 = [None] * size
        self.table2 = [None] * size

    def hash1(self, key):
        return key % self.size

    def hash2(self, key):
        return (key // self.size + 1) % self.size

    def search(self, key):
        return (
            self.table1[self.hash1(key)] == key
            or self.table2[self.hash2(key)] == key
        )

    def insert(self, key):
        if self.search(key):
            return True

        current = key
        for _ in range(2 * self.size):
            index1 = self.hash1(current)
            if self.table1[index1] is None:
                self.table1[index1] = current
                return True

            self.table1[index1], current = current, self.table1[index1]

            index2 = self.hash2(current)
            if self.table2[index2] is None:
                self.table2[index2] = current
                return True

            self.table2[index2], current = current, self.table2[index2]

        print("Insertion failed; rehashing is required.")
        return False

    def display(self):
        print("Table 1:", self.table1)
        print("Table 2:", self.table2)


if __name__ == "__main__":
    cuckoo = CuckooHashing()
    for item in [20, 33, 46, 15, 28]:
        print("Insert", item, ":", cuckoo.insert(item))
    cuckoo.display()
    print("Search 33:", cuckoo.search(33))
