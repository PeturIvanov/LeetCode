class Solution(object):
    def merge(self, nums1, m, nums2, n):
        zero_inx = m

        for num in nums2:
            for i in range(m + n):
                if num <= nums1[i]:
                    nums1.insert(i, num)
                    zero_inx += 1
                    nums1.pop()
                    break

                elif i == zero_inx:
                    nums1[i] = num
                    zero_inx += 1
                    break

        return nums1

solution = Solution()
print(solution.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3))



# def merge_two_sorted_arrays(A, m, B, n) -> None:
#     a, b, write_index = m-1, n-1, m + n - 1
#
#     while b >= 0:
#         if a >= 0 and A[a] > B[b]:
#             A[write_index] = A[a]
#             a -= 1
#         else:
#             A[write_index] = B[b]
#             b -= 1
#
#         write_index -= 1
#
#     return A
#
# print(merge_two_sorted_arrays([1,2,3,0,0,0], 3, [2, 5, 6], 3))