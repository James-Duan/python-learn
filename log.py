import functools


def log(log):
    def wrapper(func):
        @functools.wraps(func)
        def wrapper_son(*args, **kw):
            print "start execution %s" % func.__name__
            print "the log is : %s" % log
            return func(*args, **kw)
        return wrapper_son
    return wrapper
