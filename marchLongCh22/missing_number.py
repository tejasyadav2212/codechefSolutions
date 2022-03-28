'''Alice (uniformly and independently) randomly picks two integers a,b from the range [1,104], and writes down the values of a+b, a−b, a⋅b and ⌊ab⌋ (integer division) in some random order. Unfortunately, she forgot the values of a and b. You need to help her to find out if there exists two integers a,b such that 1≤a,b≤104 and a+b, a−b, a⋅b, ⌊ab⌋

are the numbers she has written down.

If a solution exists, it is guaranteed to be unique.
Input Format

    The first line of input contains a single integer T

, denoting the number of testcases. The description of T
testcases follows.
Each testcase consists of a single line of input, containing four space-separated integers A,B,C,D
— the values written down by Alice. It is guaranteed that at most one of the four numbers A,B,C,D

    will be negative.

Output Format

    For each testcase, output in a single line, separated by a space, the two numbers Alice has chosen in order (i.e, if the solution is a=1

and b=2, print 1 2 and not 2 1). If there does not exist any such choice of integers, print −1

    twice, separated by a space, instead.

Constraints

    1≤T≤105

−109≤A,B,C,D≤109
At most one of A,B,C,D

    is negative.

Subtasks

Subtask #1 (100 points): Original constraints
Sample Input 1

2
-1 72 0 17
1 4 5 6

Sample Output 1

8 9
-1 -1

Explanation

Test case 1
: With a=8,b=9 we obtain 8+9=17,8−9=−1,8⋅9=72,⌊89⌋=0 which are exactly the 4

numbers written down by Alice.

Test case 2
: It can be shown that no choice of integers a,b can produce the given 4 numbers.'''

t = int(input())
for i in range(0, t):
    l = list(map(int, input().split(' ')))
    l.sort()
    p = max(l)
    c=0
    l1=[]
    
    for j in range(1 , p+1):
        # finding factors of max i.e multiplication
        
        if(p%j==0):
            l1.append((j,p//j))  #p//j the other factor
            
    for j in l1:
        #traversing the factors list
        l2=[]
        l2.append(j[0]*j[1])
        l2.append(j[0]//j[1])
        l2.append(j[0]-j[1])
        l2.append(j[0]+j[1])
        l2.sort()
        if(l==l2):
            print(j[0], j[1])
            c+=1
            break
    if(c==0):
        print(-1, -1)
            
