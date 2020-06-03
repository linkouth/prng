import argparse
from enum import Enum
from collections import namedtuple

from generators import lc, add, lfsr, bbs, five_params_method, rc4, mersenne_twister, nlc_lfsr, rsa


def handle_lc(input_data):
    n = input_data.n
    a, c, m, x0 = input_data.i[0], input_data.i[1], input_data.i[2], input_data.i[3]
    lc_generator = lc.Generator(n=n, a=a, c=c, m=m, x0=x0)
    return lc_generator.get_sequence()


def handle_add(input_data):
    s = (len(input_data.i) - 2) // 2
    a_arr = input_data.i[:s]
    c = int(input_data.i[s])
    m = int(input_data.i[s + 1])
    x_arr = input_data.i[-s:]
    add_generator = add.Generator(n=input_data.n, s=s, c=c, m=m, a_arr=a_arr, x_arr=x_arr)
    return add_generator.get_sequence()


def handle_lfsr(input_data):
    n = input_data.n
    p, a, y_start, s = \
        int(input_data.i[0]), int(input_data.i[1]), int(input_data.i[2]), int(input_data.i[3])

    j = []
    for idx, item in enumerate(f"{a:0{p}b}"):
        if int(item) == 1:
            j.append(idx + 1)
    m = len(j)

    lfsr_generator = lfsr.Generator(n=n, p=p, s=s, m=m, j_arr=j, y_start=y_start)
    return lfsr_generator.get_sequence()


def handle_five_params(input_data):
    n = input_data.n
    p, w, q1, q2, q3, y_start = \
        input_data.i[0], input_data.i[4], input_data.i[1], \
        input_data.i[2], input_data.i[3], input_data.i[5]
    five_params_generator = five_params_method.Generator(n=n, p=p, w=w, q1=q1, q2=q2, q3=q3, y_start=y_start)
    return five_params_generator.get_sequence()


def handle_rsa(input_data):
    c = int(input_data.n)
    n, e, x_start, w, l = \
        int(input_data.i[0]), int(input_data.i[1]), int(input_data.i[4]), \
        int(input_data.i[2]), int(input_data.i[3])

    rsa_generator = rsa.Generator(c=c, n=n, e=e, x_start=x_start, w=w, l=l)
    return rsa_generator.get_sequence()


def handle_bbs(input_data):
    c = int(input_data.n)
    n, x_start, l = int(input_data.i[0]), int(input_data.i[2]), int(input_data.i[1])

    bbs_generator = bbs.Generator(c=c, n=n, x_start=x_start, l=l)
    return bbs_generator.get_sequence()


def handle_rc4(input_data):
    n = int(input_data.n)
    w = int(input_data.i[-1])
    keys = [int(k) for k in input_data.i[:-1]]

    rc4_generator = rc4.Generator(n=n, w=w, keys=keys)
    return rc4_generator.get_sequence()


def handle_nlc_lfsr(input_data):
    c = input_data.n
    k = int(input_data.i[0])
    w = int(input_data.i[1])

    buffer = input_data.i[2:2 + 3 * k]
    p_arr = []
    x_start_arr = []
    m_arr = []
    j_arr = []
    idx = 0
    while idx < 3 * k:
        p, a, x = int(buffer[idx]), int(buffer[idx + 1]), int(buffer[idx + 2])
        p_arr.append(p)
        x_start_arr.append(x)

        j = []
        for key, item in enumerate(f"{a:0{p}b}"[::-1]):
            if int(item) == 1:
                j.append(key + 1)
        m = len(j)
        j_arr.append(j)
        m_arr.append(m)

        idx += 3

    j = [f"{value:0{k}b}" for value in input_data.i[2 + 3 * k:]]
    q = len(j)

    nlc_lfsr_generator = nlc_lfsr.Generator(
        c=c, k=k, w=w, p_arr=p_arr,
        x_start_arr=x_start_arr, m_arr=m_arr, j_arr=j_arr, q=q, j=j
    )
    return nlc_lfsr_generator.get_sequence()


def handle_mersenne_twister(input_data):
    n = int(input_data.n)
    p, w, r, q, a, u, s, t, l, b, c = [item for item in input_data.i[:11]]
    x_arr = [int(x) for x in input_data.i[-p:]]

    mersenne_generator = mersenne_twister.Generator(
        n=n, p=p, w=w, r=r,
        q=q, a=a, u=u, s=s,
        t=t, l=l, b=b, c=c,
        x_arr=x_arr
    )
    return mersenne_generator.get_sequence()


class Dists(Enum):
    LC = 'lc'
    ADD = 'add'
    FP = '5p'
    LFSR = 'lfsr'
    NLFSR = 'nlfsr'
    MT = 'mt'
    RC4 = 'rc4'
    RSA = 'rsa'
    BBS = 'bbs'


def parse_data(args):
    if args.n is None:
        n = 10000
    else:
        n = int(args.n)

    i = []
    for num_as_str in args.i.split(','):
        num_as_str = num_as_str.strip()
        if len(num_as_str) > 2 and num_as_str[:2] == '0b':
            i.append(int(num_as_str[2:], 2))
        elif len(num_as_str) > 2 and num_as_str[:2] == '0x':
            i.append(int(num_as_str[2:], 16))
        else:
            i.append(int(num_as_str))

    Data = namedtuple('Data', ['n', 'm', 'i'])

    return Data(n=n, m=args.m, i=i)


def output_data(arr, path):
    if path is None:
        for a in arr:
            print(f"{a}")
    else:
        with open(path, 'w') as output:
            for a in arr:
                output.write(f'{a}\n')


def main():
    parser = argparse.ArgumentParser(description='Pseudo-random number generators')
    parser.add_argument('-f', help='Path to file with output sequence')
    parser.add_argument('-g', type=str, help='Type of the generator')
    parser.add_argument('-i', help='The initialize vector')
    parser.add_argument('-n', help='The number of generated samples')
    parser.add_argument('-m', help='Take by module m')

    args = parser.parse_args()
    gen_type = str(args.g).lower()

    input_data = parse_data(args)

    if gen_type == Dists.LC.value:
        seq = handle_lc(input_data)
        output_data(seq, args.f)
    elif gen_type == Dists.ADD.value:
        seq = handle_add(input_data)
        output_data(seq, args.f)
    elif gen_type == Dists.FP.value:
        seq = handle_five_params(input_data)
        output_data(seq, args.f)
    elif gen_type == Dists.LFSR.value:
        seq = handle_lfsr(input_data)
        output_data(seq, args.f)
    elif gen_type == Dists.NLFSR.value:
        seq = handle_nlc_lfsr(input_data)
        output_data(seq, args.f)
    elif gen_type == Dists.MT.value:
        seq = handle_mersenne_twister(input_data)
        output_data(seq, args.f)
    elif gen_type == Dists.RC4.value:
        seq = handle_rc4(input_data)
        output_data(seq, args.f)
    elif gen_type == Dists.RSA.value:
        seq = handle_rsa(input_data)
        output_data(seq, args.f)
    elif gen_type == Dists.BBS.value:
        seq = handle_bbs(input_data)
        output_data(seq, args.f)
    else:
        print(f"Generator {gen_type} does not exist")


if __name__ == '__main__':
    main()
