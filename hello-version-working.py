import platform


def main():
    message()
    butt()


def message():
    print('This is python version {}'.format(platform.python_version()))

def butt():
    print('This is a comment from butt {}'.format(platform.python_version()))

if __name__ == '__main__': main()
