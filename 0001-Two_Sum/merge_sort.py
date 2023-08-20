def merge(arr1, arr2):
    i = 0
    j = 0

    out = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            out.append(arr1[i])
            i += 1
        else:
            out.append(arr2[j])
            j += 1

    if i >= len(arr1):
        out += arr2[j:]
    if j >= len(arr2):
        out += arr1[i:]

    return out


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    return merge(merge_sort(arr[: len(arr) // 2]), merge_sort(arr[len(arr) // 2: ]))


print(merge_sort([5, 2, 7, 3, 9, 1]))