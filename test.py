import os


def add(a, b):
    return a + b


def get_path():
    return os.getcwd()


def main():
    print "path %s" % get_path()
    print "2+3=%s" % add(2, 3)


if __name__ == '__main__':
    main()



