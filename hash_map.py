class HashMap:
    def __init__(self):
        self.l = [[] for _ in range(1000000)]

    def put(self, key: int, value: int) -> None:
        self.l[key] = value

    def get(self, key):
        return self.l[key]

    def remove(self, key):
        self.l[key] = -1


if __name__ == '__main__':
    obj = HashMap()
    obj.put(1, 1)
    print(obj.get(1))