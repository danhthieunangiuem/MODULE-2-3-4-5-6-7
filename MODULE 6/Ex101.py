import time

def shape1():
    shape = [
        "       *    ",
        "       * *   ",
        "       * * *  ",
        " * * * * * * * ",
        " * * *     ",
        " * *",
        " *",
    ]
    for line in shape:
        print(line)

def shape2():
    shape = [
        "       *    ",
        "       * *   ",
        "       *   * ",
        " * * * * * * * ",
        " *   *    ",
        " * *",
        " *",
    ]
    for line in shape:
        print(line)

def shape3():
    shape = [
        "      * * * *  ",
        "      * * *    ",
        "      * *      ",
        "      *        ",
        "    * *   ",
        "  * * *",
        "* * * *",
    ]
    for line in shape:
        print(line)

def shape4():
    shape = [
        "      * * * *  ",
        "      *   *    ",
        "      * *      ",
        "      *        ",
        "    * *   ",
        "  *   *",
        "* * * *",
    ]
    for line in shape:
        print(line)

def main():
    shape1()
    time.sleep(5)
    print("\n" * 2)
    shape2()
    time.sleep(5)
    print("\n" * 2)
    shape3()
    time.sleep(5)
    print("\n" * 2)
    shape4()

if __name__ == "__main__":
    main()