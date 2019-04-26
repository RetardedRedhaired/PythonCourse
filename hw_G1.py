def saver(func):
    def wrapped(*args, **kwargs):
        t = func.__name__ + '.txt'
        f = open(t, 'w')
        result = func(*args, **kwargs)
        f.write(str(result))
        f.close
        return result
    return wrapped

@saver
def list_sum(a):
    return sum(a)

@saver
def list_max(a):
    return max(a)

print(list_sum([1, 2, 3]))
print(list_max([5, 6, 7]))
