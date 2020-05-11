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
        n_iter = 0
        while n_iter < self.n:
            i = (i + 1) % 256
            j = (j + self.states[i]) % 256
            self.states[i], self.states[j] = self.states[j], self.states[i]
            t = (self.states[i] + self.states[j]) % 256
            self.x_arr += [int(x) for x in bin(self.states[t])[2:]]
            if n_iter * self.w + self.w <= len(self.x_arr):
                y = ''
                for w_iter in range(self.w):
                    y += str(self.x_arr[self.w * n_iter + w_iter])
                self.y_arr.append(int(y, 2))
                # tmp = ''.join(str(x) for x in self.x_arr[self.w * n_iter:n_iter * self.w + self.w])
                n_iter += 1
            else:
                continue
