def flat_generator(list_):
    for i in list_:
        my_iter = iter(i)
        for n in range(len(i)):
            yield next(my_iter)