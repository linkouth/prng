import lfsr, five_params_method, rsa, bbs, rc4, mersenne_twister


def handle_lfsr():
    n, p, s = map(lambda item: int(item), input().strip().split(' '))
    tmp = input().strip().split(' ')
    m, j = int(tmp[0]), [int(x) for x in tmp[1:]]
    y_start = int(input().strip())
    lfsr_generator = lfsr.Generator(n=n, p=p, s=s, m=m, j_arr=j, y_start=y_start)
    print(lfsr_generator.get_sequence())


def handle_five_params():
    n, p, w, q1, q2, q3, y_start = map(lambda item: int(item), input().strip().split(' '))
    five_params_generator = five_params_method.Generator(n=n, p=p, w=w, q1=q1, q2=q2, q3=q3, y_start=y_start)
    print(five_params_generator.get_sequence())


def handle_rsa():
    c, n, e, x_start, w, l = map(int, input().split())
    rsa_generator = rsa.Generator(c=c, n=n, e=e, x_start=x_start, w=w, l=l)
    print(rsa_generator.get_sequence())


def handle_bbs():
    c, n, x_start, l = map(int, input().split())
    bbs_generator = bbs.Generator(c=c, n=n, x_start=x_start, l=l)
    print(bbs_generator.get_sequence())


def handle_rc4():
    n, w = map(int, input().split())
    keys = []
    for i in range(16):
        tmp_input = input().strip()
        while '  ' in tmp_input:
            tmp_input = tmp_input.replace('  ', ' ')
        keys = keys + list(map(int, tmp_input.split(' ')))
    rc4_generator = rc4.Generator(n=n, w=w, keys=keys)
    print(rc4_generator.get_sequence())


def handle_mersenne_twister():
    n = int(input().strip())
    p = int(input().strip())
    w = int(input().strip())
    r = int(input().strip())
    q = int(input().strip())
    a = int(input().strip())
    u = int(input().strip())
    s = int(input().strip())
    t = int(input().strip())
    l = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())
    x_arr = [int(x) for x in input().strip().split(' ')]

    mersenne_generator = mersenne_twister.Generator(
        n = n,
        p = p,
        w = w,
        r = r,
        q = q,
        a = a,
        u = u,
        s = s,
        t = t,
        l = l,
        b = b,
        c = c,
        x_arr = x_arr
    )
    print(mersenne_generator.get_sequence())



def main():
    handle_mersenne_twister()
    # handle_rc4()
    # handle_bbs()
    # handle_rsa()
    # handle_five_params()
    # handle_lfsr()


if __name__ == '__main__':
    main()
