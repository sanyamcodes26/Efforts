'''
Given an unsorted array A of size N of non-negative integers, find a
continuous sub-array which adds to a given number S.
Input:
The first line of input contains an integer T denoting the number of
test cases. Then T test cases follow. Each test case consists of two
lines. The first line of each test case is N and S, where N is the size
of array and S is the sum. The second line of each test case
contains N space separated integers denoting the array elements.
Output:
For each test case, in a new line, print the starting and ending
positions(1 indexing) of first such occurring sub array from the
left if sum equals to sub array, else print -1.
Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010
Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5
Explanation :
Test case 1: sum of elements from 2nd position to 4th position is 12
Test case 2: sum of elements from 1st position to 5th position is 15
'''


class Subarray_With_Given_Sum:

    def __init__(self, array):
        self.array = array
        self.disp()

    def disp(self):
        for i in self.array:
            print("[{}]".format(i), end=" ")
        print()
        return

    def run(self, total):
        i, temp2, j = 0, 0, 0
        while i < len(self.array):
            j = i
            temp2 = 0
            if temp2 < total and j < len(self.array)-1:
                temp2 += int(self.array[j])
                j += 1
            elif temp2 == total:
                return [i+1, j+1]
            else:
                i += 1
        return -1


if __name__ == "__main__":
    print(">>\tINPUT")
    test_case = int(input())
    if test_case <= 100:
        while test_case > 0:
            a, b = input().split()
            lista = list(input().split(" "))
            print(">>\tOUTPUT")
            obj = Subarray_With_Given_Sum(lista)
            ans = obj.run(int(b))
            if ans != -1:
                for i in ans:
                    print(i, end=" ")
            else:
                print(-1)
            test_case -= 1
