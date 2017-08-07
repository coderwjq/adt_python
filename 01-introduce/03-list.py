from timeit import Timer


def test_append():
    li = []
    for i in range(10000):
        li.append(i)


def test_insert():
    li = []
    for i in range(10000):
        li.insert(0, i)


timer_append = Timer("test_append()", "from __main__ import test_append")
print("append", timer_append.timeit(1000))

timer_insert = Timer("test_insert()", "from __main__ import test_insert")
print("insert(0)", timer_insert.timeit(1000))
