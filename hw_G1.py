def saver(func):
    def wrapped(*args, **kwargs):
        t = func.__name__ + '.txt'
        result = func(*args, **kwargs)
        with open(t, 'w') as f:
            f.write(str(result))
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
