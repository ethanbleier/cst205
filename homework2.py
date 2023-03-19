import statistics
color_list_example = [109460, 1, 1, 2, 4181, 3, 5, 8, 13, 17711, 21, 34, 55, 6765, 89, 144, 233, 377, 610, 987, 1597]
def my_median(color_list_example):
# Calculates median value of list of values and prints median value
    return statistics.median(color_list_example.sort())

print(statistics.median(color_list_example.sort()))