import os


def get_path():
    return os.getcwd()


def main():
    print "path %s" % get_path()


if __name__ == '__main__':
    main()



