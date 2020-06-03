from progress_bar import print_progress_bar


class Generator:
    def __init__(self,
        c, k, w, p_arr,
        x_start_arr, m_arr, j_arr,
        q, j
    ):
        self.c = c
        self.k = k
        self.w = w
        self.p_arr = p_arr
        self.x_start_arr = x_start_arr
        self.m_arr = [int(m) for m in m_arr]
        self.j_arr = [[int(item) - 1 for item in ar] for ar in j_arr]
        self.q = int(q)
        self.j = [[int(j) for j in str(item)] for item in j]

        print_progress_bar(0, self.k, prefix='Progress step 1:', suffix='Complete', length=50)
        self.lfsr_generated_list = []
        for i in range(self.k):
            self.lfsr_generated_list.append(self.generate_lfsr_list(int(self.c * self.w / self.p_arr[i] + 1), self.p_arr[i], self.m_arr[i], self.j_arr[i], self.x_start_arr[i]))
            print_progress_bar(i + 1, self.k, prefix='Progress step 1:', suffix='Complete', length=50)

        print_progress_bar(0, self.c, prefix='Progress step 2:', suffix='Complete', length=50)
        self.y_arr = []
        for c_iter in range(self.c):
            result = []
            for w_iter in range(self.w):
                new_x = 0
                bits = [item[self.w * c_iter + w_iter] for item in self.lfsr_generated_list]
                for q_iter in range(self.q):
                    need_bits = [1 if self.j[q_iter][idx] == 0 else value for idx, value in enumerate(bits)]
                    qq = need_bits[0]
                    for bit in need_bits[1:]:
                        qq = qq & bit
                    new_x = new_x ^ qq
                result.append(new_x)
            self.y_arr.append(int(''.join([str(it) for it in result]), 2))
            print_progress_bar(c_iter + 1, self.k, prefix='Progress step 2:', suffix='Complete', length=50)

    def generate_lfsr_list(self, n, p, m, j, start):
        x = []
        temp_first_x = self.to_bin(start, p)
        x += temp_first_x
        for n_iter in range(n):
            for p_iter in range(p):
                new_x = 0
                for m_iter in range(m):
                    new_x += x[n_iter * p + p_iter + j[m_iter]]
                    new_x %= 2
                x.append(new_x)
        return x[len(temp_first_x):]

    def to_bin(self, value, size):
        ans = []
        while value > 1:
            ans.append(value % 2)
            value //= 2
        ans.append(value % 2)
        while len(ans) < size:
            ans.append(0)

        return ans[::-1]

    def to_dec(self, x):
        ans = 0
        st = 1
        for item in x[::-1]:
            if item == 1:
                ans += 1
            st *= 2
        return ans

    def get_sequence(self):
        return self.y_arr
