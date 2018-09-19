if __name__ == '__main__':
    def threeSumClosest(A, B):
        # return B if A is empty
        if len(A) == 0:
            return B
        #sort A
        A.sort()
        # c stores the sum of three numbers
        c = 0
        # d stores the return value
        d = 0
        #initialize minimum differece with maximum int value
        mind = 2147483648
        #i, j and k loop across the list A 
        for i in range(len(A)):
            j = i+1
            k = len(A)-1
            # we loop until j becomes equal to k
            while j < k:
                c = (A[i] + A[j] + A[k])
                diff = abs(c-B)
                #if the sum is equal to B return the sum
                if diff == 0:
                    return c
                #else if sum is not equal to B update minimum difference(mind) with diff
                #and update the return value with the current sum
                if diff < mind:
                    mind = diff
                    d = c
                if c <= B:
                    j += 1
                else:
                    k -= 1
        # print(c)
        return d
    A = list(map(int,input().split()))
    B = int(input())
    print(threeSumClosest(A, B))