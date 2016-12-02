from aprox_tsp import aprox_tsp
import timeit

if __name__ == "__main__":
    # Estas son solo para ver que funciona, hay que hacer otras
    start_time = timeit.default_timer()
    p01 = aprox_tsp("matrices/p01.m")
    res = timeit.default_timer() - start_time
    print "15 nodes:", res, "seconds"

    start_time = timeit.default_timer()
    gr17 = aprox_tsp("matrices/gr17.m")
    res = timeit.default_timer() - start_time
    print "17 nodes:", res, "seconds"

    start_time = timeit.default_timer()
    fri26 = aprox_tsp("matrices/fri26.m")
    res = timeit.default_timer() - start_time
    print "26 nodes", res, "seconds"





