def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    tuple_i = tuple_a + (0, 0)
    tuple_j = tuple_b + (0, 0)
    new_tuple = (tuple_i[0] + tuple_j[0], tuple_i[1] + tuple_j[1])
    return new_tuple
