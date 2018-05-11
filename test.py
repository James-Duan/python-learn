import os
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print '%s %s:' % (func, func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def get_path():
    return os.getcwd()


def main():
    print "path %s" % get_path()


if __name__ == '__main__':
    main()



