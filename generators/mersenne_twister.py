class Generator:
    def __init__(self,
        n,
        p,
        w,
        r,
        q,
        a,
        u,
        s,
        t,
        l,
        b,
        c,
        x_arr,
    ):
        self.n = n
        self.p = p
        self.w = w
        self.r = r
        self.q = q
        self.a = a
        self.u = u
        self.s = s
        self.t = t
        self.l = l
        self.b = b
        self.c = c
        self.x_arr = x_arr
        self.n = n
        self.w = w

        self.z_arr = []

        self.generate_sequence()

    def get_sequence(self):
        return self.z_arr

    def generate_sequence(self):
        for i in range(self.n):
            a = bin(self.x_arr[i])[2:]
            if len(a) < self.w:
                a = '0' * (self.w - len(a)) + a
            b = bin(self.x_arr[i + 1])[2:]
            if len(b) < self.w:
                b = '0' * (self.w - len(b)) + b
            a1 = a[::-1][self.r:self.w][::-1]
            b1 = b[::-1][:self.r][::-1]
            x1 = int(a1 + b1, 2)

            x = self.x_arr[i + self.q] ^\
                (x1 >> 1) ^\
                (self.a * (x1 % 2))
            x = x % pow(2, self.w)
            self.x_arr.append(x)

            y = (x ^ (x >> self.u)) % pow(2, self.w)
            y = y ^ ((y << self.s) & self.b)
            y = y ^ ((y << self.t) & self.c)
            z = (y ^ (y >> self.l)) % pow(2, self.w)
            self.z_arr.append(z)
