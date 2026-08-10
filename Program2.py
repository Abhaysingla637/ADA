class Sort:
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        result = []
        i = j = 0

        # Merge two sorted halves
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[-1]
        left = []
        right = []

        # Divide elements around the pivot
        for x in arr[:-1]:
            if x <= pivot:
                left.append(x)
            else:
                right.append(x)

        return self.quick_sort(left) + [pivot] + self.quick_sort(right)


# Main
arr = [38, 27, 43, 3, 9, 82, 10]

s = Sort()

print("Original array:", arr)
print("Merge Sort:", s.merge_sort(arr))
print("Quick Sort:", s.quick_sort(arr))