'''
Given two integers n and k, return all possible combinations of k numbers
 chosen from the range [1, n].

You may return the answer in any order.

 
Input: n = 6 , k = 3
Output: [
            [1,2,3], [1,2,4], [1,2,5], [1,2,6], 
            [2,3,4], [2,3,5], [2,3,6],
            [3,1,5], [3,1,]
            ]
Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered 
to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

Constraints:

1 <= n <= 20
1 <= k <= n

function makeCombination(n, k, i = 1) {
    const result = [];
    while (i <= n - k + 1) {
        if (k === 1) result.push([i]);
        else result.push(
          ...makeCombination(
            n, k - 1, i + 1)
            .map(
              a => [i, ...a]
              )
            );
        i++;
    }
    return result;
}

makeCombination(5, 3).map(a => console.log(...a));


let ans = [],
  arr = [];

function makeCombination(n, k, low = 1) {
  if (k == 0) {
    ans.push(arr.slice());
//    console.log(...arr); commenting out the console log to demonstrate that the returned value is correct
    return;
  }

  for (let i = low; i <= n; i++) {
    arr.push(i);
    makeCombination(n, k - 1, i + 1);
    arr.pop();
  }
  return ans;
}

var n = 5;
var k = 3;

makeCombination(n, k).map(a => console.log(...a));


'''

def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    combinations = []
    a = 0
    b = 1
    while a < k and b < n:
        if a < k:
            a += 1
        else:
            a =
        a += 1
        for i in range(1,n):
        combinations.append([])
        # print(combinations)
        if len(combinations[i-1]) < k:
            combinations[i-1].append(i)
    return combinations


print(combine(4, 2))