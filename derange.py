# Python 3 only

def derange(iterable):
    """
    Convert a sequence of integers to a minimal sequence of `range` objects
    that generate all the elements of the input sequence (ignoring duplicates
    and reordering)

    >>> derange([3,4,5,6,7,10,11,12,15,16,17,19,20,21,22,23,24,42,43,44,45,46])
    [range(3, 8), range(10, 13), range(15, 18), range(19, 25), range(42, 47)]

    >>> derange([2016, 2015, 2016])
    [range(2015, 2017)]

    >>> derange([42])
    [range(42, 43)]

    >>> derange([])
    []
    """
    ranges = []
    for x in iterable:
        if not ranges:
            ranges = [range(x, x+1)]
        elif x < ranges[0].start - 1:
            ranges.insert(0, range(x, x+1))
        elif x > ranges[-1].stop:
            ranges.append(range(x, x+1))
        else:
            low, high = 0, len(ranges)
            while low < high:
                mid = (low + high) // 2
                if x in ranges[mid]:
                    break
                elif x == ranges[mid].start - 1:
                    if mid > 0 and ranges[mid-1].stop == x:
                        ranges[mid-1:mid+1] \
                            = [range(ranges[mid-1].start, ranges[mid].stop)]
                    else:
                        ranges[mid] = range(x, ranges[mid].stop)
                elif x == ranges[mid].stop:
                    if mid+1 < len(ranges) and ranges[mid+1].start == x+1:
                        ranges[mid:mid+2] \
                            = [range(ranges[mid].start, ranges[mid+1].stop)]
                    else:
                        ranges[mid] = range(ranges[mid].start, x+1)
                elif x < ranges[mid].start:
                    high = mid
                else:
                    assert x > ranges[mid].stop
                    low = mid + 1
            else:
                ranges.insert(low, range(x, x+1))
    return ranges

def deinterval(adjacent, iterable):
    """
    Generalization of `derange` for arbitrary types.

    Returns a list of pairs defining a closed interval (so the upper bound is
    included in each range)

    :param callable adjacent: called with two elements of ``iterable`` at a
        time to test whether they are "adjacent"/"consecutive"
    """
    raise NotImplementedError

def derange_sorted(iterable):  # for sorted (ascending) inputs
    ranges = []
    for x in iterable:
        if not ranges:
            ranges = [range(x, x+1)]
        elif x == ranges[-1].stop:
            ranges[-1] = range(ranges[-1].start, x+1)
        elif x > ranges[-1].stop:
            ranges.append(range(x, x+1))
    return ranges

def deinterval_sorted(adjacent, iterable):  # for sorted (ascending) inputs
    raise NotImplementedError
