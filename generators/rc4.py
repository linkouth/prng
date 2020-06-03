class Generator:
    def __init__(self, n, w, keys):
        self.n = n
        self.w = w
        self.keys = keys
        self.states = [i for i in range(255 + 1)]
        j = 0
        for i in range(255 + 1):
            j = (j + self.states[i] + self.keys[i]) % 256
            self.states[i], self.states[j] = self.states[j], self.states[i]

        self.x_arr = []
        self.y_arr = []
        self.generate_sequence()

    def get_sequence(self):
        return self.y_arr

    def generate_sequence(self):
        i = 0
        j = 0
        n_iter = self.n
        bin_x = ''
        y = ''
        while n_iter > 0:
            i = (i + 1) % 256
            j = (j + self.states[i]) % 256
            self.states[i], self.states[j] = self.states[j], self.states[i]
            t = (self.states[i] + self.states[j]) % 256
            bin_x = bin(self.states[t])[2:]
            if len(bin_x) < 8:
                bin_x = '0' * (8 - len(bin_x)) + bin_x
            y += bin_x[-8:]
            while len(y) >= self.w and n_iter > 0:
                self.y_arr.append(int(y[:self.w], 2))
                y = y[self.w:]
                n_iter -= 1
