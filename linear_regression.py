import numpy

def main():
    (N, X, Y) = read_data()
    print(N)
    print(X)
    print(Y)

def read_data():
    # 1
    N = input()
    X = numpy.array([])
    Y = numpy.array([])
    for t in range(int(N)):
        temp = input().split(" ")
        X = numpy.concatenate((X, [temp[0]]))
        Y = numpy.concatenate((Y, [temp[1]]))
    
    # 2

    return (N, X, Y)

if __name__ == "__main__":
    main()