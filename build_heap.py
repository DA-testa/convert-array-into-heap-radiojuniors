# python3


def build_heap(data, n):
    swaps = []
    for h in range(2):
        for i in reversed(range(n)):
            while i>0:
                if i%2==0:
                    if data[i] <= data[i//2-1]:
                        data[i],data[i//2-1] = data[i//2-1], data[i]
                        swaps.append((i//2-1,i))
                        i=i//2-1
                    if data[i] > data[i//2-1]:
                        break
                else:
                    if data[i] <= data[i//2]:
                        data[i],data[i//2] = data[i//2], data[i]
                        swaps.append((i//2,i))
                        i=i//2
                    if data[i] > data[i//2]:
                        break
    return swaps


def main():
    inp = input()
    inp = inp[0]
    if (inp.upper() == "F"):
        inp = input()
        f = open("./tests/" + inp, "r")
        n = int(f.readline())
        data = list(map(int, f.readline().split()))
    else:
        n = int(input())
        data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data, n)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
