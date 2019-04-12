import platform

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))
    print('Printing this message with {0} and {1} coded this and wanted to print out {2:.4f}.'.format('Python', 'Bryan Rojas', 3.140000))

if __name__ == '__main__':
    main()