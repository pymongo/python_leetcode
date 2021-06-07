def test():
    # both a and b aree on global HashMap<String, Any>
    print(a)


if __name__ == '__main__':
    a = 1
    while a >= 1:
        b = 2
        break
    test()
    print(b)
