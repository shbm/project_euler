def main():
    alphabets = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    f = open('./p022_names.txt', 'r')
    n = f.read()
    names = sorted(n.split(','))
    score = 0
    for i, name in enumerate(names):
        i += 1
        sum = 0
        for j in name[1:-1]:
            sum += alphabets[j]
        score = i*sum + score
    print score


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
