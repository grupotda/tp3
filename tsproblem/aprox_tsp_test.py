from aprox_tsp import aprox_tsp

if __name__ == "__main__":
    # Estas son solo para ver que funciona, hay que hacer otras
    fri26 = aprox_tsp("matrices/fri26.m")
    print "\nfri26"
    for edge in fri26.iter_edges():
        print edge
    gr17 = aprox_tsp("matrices/gr17.m")
    print "\ngr17"
    for edge in gr17.iter_edges():
        print edge
    p01 = aprox_tsp("matrices/p01.m")
    print "\np01"
    for edge in p01.iter_edges():
        print edge
