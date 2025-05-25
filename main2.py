import inspect
def who_am_i(obj):
    print((type(obj)))
    print((dir(obj)))
    print(type(obj).__module__ == 'builtins')

who_am_i(123)
who_am_i("fds")