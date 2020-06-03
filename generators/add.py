class Generator:
    def __init__(self, n, s, c, m, a_arr, x_arr):
        self.n = n
        self.s = s
        self.c = c
        self.m = m
        self.a_arr = a_arr
        self.x_arr = x_arr

        self.generate_sequence()

    def get_sequence(self):
        return self.x_arr[self.s:self.n + self.s]

    def generate_sequence(self):
        for i in range(self.n):
            sum = 0
            for j in range(self.s):
                sum = (sum + self.a_arr[j] * self.x_arr[i + j]) % self.m
            self.x_arr.append((sum + self.c) % self.m)
