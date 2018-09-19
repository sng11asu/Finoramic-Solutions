if __name__ == '__main__':
	def braces(A):
	    stack = []
	    #loop through A
	    for i in A:
	        #if a closing brace is encountered loop till an opening brace is encountered
	        if i == ')':
	            count = 0
	            #pop values until a opening brace is encountered and count
	            while stack[-1] != '(':
	                stack.pop()
	                count += 1
	            #if tere are less than two operators or operands between opening and closing braces return 1
	            if count <= 1:
	                return 1
	            #else pop the opening brace and see if more operators or operands exist
	            else:
	                stack.pop()
	        #push to stack all operators and operands until a closing brace is encountered
	        else:
	            stack.append(i)
	    return 0

	a = input()
	a = list(a)
	if braces(a) == True:
	    print("Yes")
	else:
	    print("No")