def sortedSquares(A):
    
    # 第一种
    # List = []
    # for i in A:
    #     List.append(i**2)
    # return sorted(List)

    # 第一种优化
    return sorted([x * x for x in A])

    # 第二种双指针
    # j = 0
    # N = len(A)
    # while j < N and A[j] < 0:
    #     j += 1
    # i = j - 1

    # ans = []

    # while j < N and i >= 0:
    #     if A[i]**2 > A[j]**2:
    #         ans.append(A[j]**2)
    #         j += 1
    #     else:
    #         ans.append(A[i]**2)
    #         i -= 1

    # while i >= 0:
    #     ans.append(A[i]**2)
    #     i -= 1

    # while j < N:
    #     ans.append(A[j]**2)
    #     j += 1

    # return ans


if __name__ == "__main__":
    List = sortedSquares([-4, -1, 0, 3, 10])
    print(List)