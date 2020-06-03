class Generator:
    def __init__(self, n, a, c, m, x0):
        self.n = n
        self.a = a
        self.c = c
        self.m = m
        self.x0 = x0
        self.y_arr = [x0]
        self.generate_sequence()

    def get_sequence(self):
        return self.y_arr[1:]

    def generate_sequence(self):
        for idx in range(1, self.n + 1):
            next_y = (self.a * self.y_arr[idx - 1] + self.c) % self.m
            self.y_arr.append(next_y)
