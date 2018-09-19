if __name__ == '__main__':
	from collections import Counter
	def anagrams(A):
	    c = len(A)/2
	    #b stores list of anagrams
	    b = []
	    #loop through A till len(A)/2
	    for i in A[:int(c)]:
	        #loop j through A
	        for j in A:
	            # if i and j are anagrams add the index list to b
	            if i != j and Counter(i) == Counter(j):
	                b.append([A.index(i)+1,A.index(j)+1])
	            # else:
	                # b.append([A.index(i)])
	    return b
	A = input().split()
	print(anagrams(A))