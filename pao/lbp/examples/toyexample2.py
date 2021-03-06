#
# Toy Example 2 from 
#
# "A projection-based reformulation and decomposition algorithm for global optimization 
#  of a class of mixed integer bilevel linear programs" by Dajun Yue, Jiyao Gao, Bo Zeng, Fengqi You
#
from pao.lbp import *


def create():
    M = LinearBilevelProblem()

    U = M.add_upper(nxZ=1)
    U.x.lower_bounds = [0]

    L = U.add_lower(nxZ=1)
    L.x.lower_bounds = [0]

    U.minimize = True
    U.c[U] = [-1]
    U.c[L] = [-2]

    U.A[U] = [[-2], [1]]
    U.A[L] = [[3], [1]]
    U.b = [12,14]

    L.minimize = False
    L.c[L] = [1]

    L.A[U] = [[-3], [3]]
    L.A[L] = [[1], [1]]
    L.b = [-3,30]

    return M


if __name__ == "__main__":          #pragma: no cover
    M = create()
    opt = SolverFactory('pao.lbp.PCCG')
    opt.solve(M)
    M.print()
