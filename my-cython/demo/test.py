# Import the extension module hello.
import timeit


def test_import():
    import cy_optimized

    # Call the print_result method
    cy_optimized.print_result(23.0)
    print()


def test_for_loop_speed():
    cy = timeit.timeit('cy_optimized.test_for_loop(5000)',
                       setup='import cy_optimized', number=10)
    py = timeit.timeit('naive.test_for_loop(5000)',
                       setup='import naive', number=10)
    print(cy, py)
    print(f'Cython is {py/cy}x faster\n')


def test_numpy_best(repeat, number):
    setup = '''
import numpy as np
import cy_optimized
import naive

ff = np.array([[1, 1, 1]], dtype=np.int)
gg = np.array([[1],[2],[1]], dtype=np.int)
'''

    cy1 = timeit.Timer(
        'f = ff[:]; g = gg[:]; cy_optimized.naive_convolve1(f, g)', setup=setup)
    cy2 = timeit.Timer(
        'f = ff[:]; g = gg[:]; cy_optimized.naive_convolve2(f, g)', setup=setup)
    cy3 = timeit.Timer(
        'f = ff[:]; g = gg[:]; cy_optimized.naive_convolve3(f, g)', setup=setup)
    py = timeit.Timer(
        'f = ff[:]; g = gg[:]; naive.naive_convolve(f, g)', setup=setup)

    r_py = py.repeat(repeat, number)
    best_py, worse_py = min(r_py), max(r_py)

    r_cy1 = cy1.repeat(repeat, number)
    best_cy1, worse_cy1 = min(r_cy1), max(r_cy1)

    r_cy2 = cy2.repeat(repeat, number)
    best_cy2, worse_cy2 = min(r_cy2), max(r_cy2)

    r_cy3 = cy3.repeat(repeat, number)
    best_cy3, worse_cy3 = min(r_cy3), max(r_cy3)

    print(f"Python: {number} loops, best of {repeat}: {best_py:.3g} seconds per loop, \
            worse of {repeat}: {worse_py:.3g} seconds per loop\n")

    print(f"Cython 1: {number} loops, best of {repeat}: {best_cy1:.3g} seconds per loop, \
            worse of {repeat}: {worse_cy1:.3g} seconds per loop\n")

    print(f"Cython 2: {number} loops, best of {repeat}: {best_cy2:.3g} seconds per loop, \
            worse of {repeat}: {worse_cy2:.3g} seconds per loop\n")

    print(f"Cython 3: {number} loops, best of {repeat}: {best_cy3:.3g} seconds per loop, \
            worse of {repeat}: {worse_cy3:.3g} seconds per loop\n")


def test_generic_multithread():
    import numpy as np
    import cy_optimized

    array_1 = np.random.uniform(0, 1000, size=(30, 20)).astype(np.intc)
    array_2 = np.random.uniform(0, 1000, size=(30, 20)).astype(np.intc)
    a = 4
    b = 3
    c = 9
    print(cy_optimized.compute(array_1, array_2, a, b, c).dtype)  # int32
    print(cy_optimized.compute(array_1.astype(np.double),
                               array_2.astype(np.double), a, b, c).dtype)  # float64


def main():
    test_import()
    test_for_loop_speed()
    # repeat 10 times, 1000 times through the loop
    test_numpy_best(20, 5000)
    test_generic_multithread()


if __name__ == '__main__':
    main()
