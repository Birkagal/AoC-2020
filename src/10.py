''' 
Part One - What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
Part Two - What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?
'''


def insert_adapters_into_list(data):
    adapters = []
    for adapter in data:
        adapters.append(int(adapter))
    adapters.sort()
    adapters.append(int(data[-1])+3)
    return adapters


def partOne(content):
    adapters = insert_adapters_into_list(content)
    one_diff = []
    two_diff = []
    tree_diff = []
    current_jolts = 0
    for adapter in adapters:
        if adapter - 1 == current_jolts:
            one_diff.append(adapter)
        elif adapter - 2 == current_jolts:
            two_diff.append(adapter)
        elif adapter - 3 == current_jolts:
            tree_diff.append(adapter)
        current_jolts = adapter
    tree_diff.append(adapters[-1]+3)
    return len(one_diff) * len(tree_diff)


def partTwo(data):
    data = insert_adapters_into_list(data)

    arr = [int(line) for line in data]
    arr.sort()
    arr.append(arr[-1]+3)

    memo = {0: 1}
    for r in arr:
        memo[r] = memo.get(r-3, 0) \
            + memo.get(r-2, 0) \
            + memo.get(r-1, 0)
    return memo[arr[-1]]


def run_the_array(adapters, current_jolts, path, index):
    total = 0
    for adapter in adapters:
        if adapter - 1 == current_jolts:
            path.append(adapter)
            total += run_the_array(adapters[index:], adapter, path, index)
        elif adapter - 2 == current_jolts:
            path.append(adapter)
            total += run_the_array(adapters[index:], adapter, path, index)
        elif adapter - 3 == current_jolts:
            path.append(adapter)
            total += run_the_array(adapters[index:], adapter, path, index)
        current_jolts = adapter
        index += 1
