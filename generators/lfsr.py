from progress_bar import print_progress_bar


class Generator:
    def __init__(self, n, p, s, m, j_arr, y_start):
        self.n = n
        self.p = p
        self.s = s
        self.m = m
        self.a_arr = [0 for _ in range(p)]
        for j in j_arr:
            self.a_arr[j - 1] = 1
        self.y_start = y_start
        y_start_bin = f"{y_start:0{p}b}"
        self.x_arr = [int(x) for x in y_start_bin]
        self.y_arr = []
        self.generate_sequence()

    def get_sequence(self):
        return self.y_arr

    def generate_next_x(self):
        for s_iter in range(self.s):
            prev_p_x = self.x_arr[-self.p:]
            new_x = self.a_arr[0] & prev_p_x[0]
            for p_iter in range(1, self.p):
                new_x ^= self.a_arr[p_iter] & prev_p_x[p_iter]
            self.x_arr.append(new_x)

    def generate_sequence(self):
        print_progress_bar(0, self.n, prefix='Progress:', suffix='Complete', length=50)
        for n_iter in range(self.n):
            self.generate_next_x()
            line = self.x_arr[-self.s:]
            tmp = ''.join(str(x) for x in line)
            new_y = int(tmp, 2)
            self.y_arr.append(new_y)
            print_progress_bar(n_iter + 1, self.n, prefix='Progress:', suffix='Complete', length=50)
