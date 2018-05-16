import os
import log


def set_log(log_txt):
    return log_txt


@log.log(log='')
def get_path():

    return os.getcwd()


def main():
    print "path %s" % get_path()


if __name__ == '__main__':
    main()



