import math


class Fx(object):
    def __init__(self, n, vals):
        self.vals = vals
        self.n = n

    def get_fx(self, x):
        y = 0
        orders = [*range(0, self.n+1)][::-1]
        cofs = self.vals
        for cof, order in zip(cofs, orders):
            # print (cof, order)
            y += cof * math.pow(x, order)
        return y

    def get_fx_order(self, x):
        y = 0
        orders = [*range(0, self.n)][::-1]
        cofs = self.vals[:-1]
        for cof, order in zip(cofs, orders):
            # print (cof * (order+1), order)
            y += cof * (order+1) * math.pow(x, order)
        return y
    
    def get_root(self, x0, max_iter=20, tol=1e-4):
        p0 = x0 * 1.0
        for i in range(max_iter):
            # f的一阶导数不能为0，最普遍的说法是不能非正定
            #while (self.get_fx_order(p0) - 0) < tol:
            #    p0 += 0.1
            if abs(self.get_fx_order(p0) - 0) < tol:
                if abs(self.get_fx(p0) - 0) < tol:
                    return p0
                else:
                    p0 += 0.01
                    continue
            p = p0 - self.get_fx(p0) / self.get_fx_order(p0)
            # print (p)
            # 如果小于精度值则退出迭代
            if abs(p - p0) < tol:
                return round(p, 2)
            else:
                p0 = p
        return None


import sys
if __name__ == "__main__":
    # n A,B,C,D numbers
    if True:
        n = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        vals = [int(x) for x in line.split(' ')]
    else:
        n = 3
        vals = [1, 4, 2, 5]
        n = 2
        vals = [1, 2, 1]
    # print (n, vals)

    # n = 2
    # vals = [2, 0, 1]
    func = Fx(n, vals)

    solutions = []
    i = -5
    while i < 5:
        subsol = func.get_root(i)
        if subsol is not None:
            if len(solutions) == 0:
                solutions.append(subsol)
            else:
                # if abs(subsol-solutions[-1]) > 1e-2:
                #     solutions.append(subsol)
                keep = True
                for x in solutions:
                    if abs(x-subsol) <= 1e-2:
                        keep = False
                if keep:
                    solutions.append(subsol)
        i = i+0.002

    solutions = sorted(solutions)
    if len(solutions) == 0:
        print("No")
    else:
        out_str = " ".join([str("{:.2f}".format(x)) for x in solutions])
        print (out_str)
