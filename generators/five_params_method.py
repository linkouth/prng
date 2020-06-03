class Generator:
    def __init__(self, n, p, w, q1, q2, q3, y_start):
        self.n = n
        self.p = p
        self.w = w
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.y_start = y_start
        y_start_bin = f"{y_start:0{p}b}"
        self.x_arr = [int(x) for x in y_start_bin]
        self.y_arr = []
        self.generate_sequence()

    def get_sequence(self):
        return self.y_arr

    def generate_next_x(self):
        for s_iter in range(self.w):
            step = len(self.x_arr) - self.p
            new_x = \
                self.x_arr[step + self.q1] ^\
                self.x_arr[step + self.q2] ^\
                self.x_arr[step + self.q3] ^\
                self.x_arr[step]
            self.x_arr.append(new_x)

    def generate_sequence(self):
        for n_iter in range(self.n):
            self.generate_next_x()
            line = self.x_arr[-self.w:]
            tmp = ''.join(str(x) for x in line)
            new_y = int(tmp, 2)
            self.y_arr.append(new_y)
