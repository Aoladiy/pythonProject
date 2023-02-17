from multiprocessing import Process, Pool
import numpy as np
import time

start_time = time.time()

# import Matrix_prepare
global res
matrix1 = np.loadtxt("m1.csv", delimiter=",", dtype=np.int32)
matrix2 = np.loadtxt("m2.csv", delimiter=",", dtype=np.int32)


def element(index, a=matrix1, b=matrix2):
    i, j = index
    res = 0
    N = len(a[0]) or len(b)
    for k in range(N):
        res += a[i][k] * b[k][j]
    # print(f"i={i}, j={j} => {res}")

    return res


def main():
    if len(matrix1[0]) == len(matrix2):
        N: int = len(matrix1[0])

        with Pool(4) as p:
            a = [(i, j) for i in range(N) for j in range(N)]
            d = np.array(p.map(func=element, iterable=a), dtype=np.int32).reshape(N, N)
            np.savetxt("m3.csv", X=d, delimiter=",", fmt="% 10.d")
            print(d)


if __name__ == '__main__':
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
