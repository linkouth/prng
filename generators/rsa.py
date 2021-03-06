class Generator:
    def __init__(self, c, n, e, x_start, w, l):
        self.c = c
        self.n = n
        self.e = e
        self.x_start = x_start
        self.w = w
        self.l = l
        self.y_arr = []
        self.generate_sequence()

    def get_sequence(self):
        return self.y_arr

    def generate_sequence(self):
        s = ''
        c_iter = 0
        while c_iter < self.c:
            self.x_start = pow(self.x_start, self.e, self.n)
            a_arr = bin(self.x_start)[2:]
            if len(a_arr) < self.w:
                a_arr = '0' * (self.w - len(a_arr)) + a_arr
            s += a_arr[-self.w:]
            while len(s) >= self.l:
                self.y_arr.append(int(s[:self.l], 2))
                s = s[self.l:]
                c_iter += 1
