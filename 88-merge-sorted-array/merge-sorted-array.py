class Solution:
    def merge(self, nums1, m, nums2, n):
        x, y = (m - 1, n - 1,)  # To get to the last value befrore 0 of x and for y it's the end index

        for z in range(m + n - 1, -1, -1):  # basicly z is the last index of nums1, -1(becaus we have to check till 0) and -1 because it's a decreasing loop

            if x < 0:
                nums1[z] = nums2[y]
                y -= 1

            elif y < 0:
                break

            elif nums1[x] < nums2[y]:
                nums1[z] = nums2[y]
                y -= 1

            else:
                nums1[z] = nums1[x]
                x -= 1
