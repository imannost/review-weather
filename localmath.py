def count_average(array):
    return round((sum(array) / len(array)), 1)


def count_median(array):
    sorted_array = sorted(array)
    size = len(array)
    index = (size - 1) // 2
    if size % 2:
        return sorted_array[index]
    else:
        return (sorted_array[index] + sorted_array[index + 1]) / 2.0


def count_min(array):
    min_value = array[0]
    for n in range(1, len(array)):
        if array[n] < min_value:
            min_value = array[n]
    return min_value


def count_max(array):
    max_value = array[0]
    for n in range(1, len(array)):
        if array[n] > max_value:
            max_value = array[n]
    return max_value
