def count_partition(number , max):
    if number == 0:
        return 1
    elif number < 0:
        return 0
    elif max == 0:
        return 0
    else:
        return count_partition(number - max , max) + count_partition(number , max - 1)