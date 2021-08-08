# Meet Anna, she likes to travel with as many clean pair of socks for her trips abroad.
# Anna's socks are divided into two drawers: clean and dirty socks. Anna has an unusual
# washing machine that can only wash a sock at a time and clean at most K socks
# described by noOfWashes.
# Anna wants to pick socks for laundering in such a way that after washing she will have
# a maximal number of clean, same-coloured pair of socks. It is possible that some socks
# cannot be paired with any other sock, because Anna may have lost socks over the
# years.
# Anna has exactly N clean and M dirty socks, which are described in the
# arrays cleanPile and dirtyPile respectively. The colours of the socks are represented
# as integers with equal numbers representing identical colours.
# For example, if Anna's washing machine can clean at most 2 socks.
# noOfWashes: number = 2;
# cleanPile: number[] = [1, 2, 1, 1];
# dirtyPile: number[] = [1, 4, 3, 2, 4];
# Then, the maximum number of pairs of socks Anna can take on her trip is 3.
# In the same scenario, if Anna's machine isn't working, i.e noOfWashes is 0. The maximum
# number of socks she can take on her trips is 1.
# Also, if Anna's machine can wash as many socks as she wants, the maximum number
# of pair of socks, for this scenario she can take on her trip is 4.
# Note that clean socks do not need to be washed again.
# Write a function that given the noOfWashes, cleanPile, and dirtyPile returns the
# maximum number of pair of socks that Anna can take on the trip with the given
# conditions.
# Assume that
# noOfWashes is an integer within the range 0...50 cleanPile and dirtyPile is an integer
# array within the range 1...50, they cannot be empty, and contain at most 50 elements.

def countpairs(clean, dirty, noOfWashes):
    # variable declarations
    cleanunpaired = []  # list to hold unpaired socks in the clean socks list
    setclean = set(clean)
    pairs = 0
    # count pairs in the clean socks list
    for num in setclean:
        if clean.count(num) >= 2:
            if clean.count(num) % 2 == 0:
                pairs += clean.count(num) / 2
            else:
                cleanunpaired.append(num)
                pairs += (clean.count(num) - 1) / 2
        elif clean.count(num) < 2:
            cleanunpaired.append(num)
    # check if number of washes is below 1
    if noOfWashes < 1:
        print(f"maximum pairs of socks is {pairs}")
    # check if number of washes is greater than or equal to the number of dirty socks in dirty socks list
    elif noOfWashes >= len(dirty):
        combarr = dirty + cleanunpaired
        setcombarr = set(combarr)
        for num in setcombarr:
            if combarr.count(num) >= 2:
                if combarr.count(num) % 2 == 0:
                    pairs += combarr.count(num) / 2
                else:
                    pairs += (combarr.count(num) - 1) / 2
        print(f"maximum pairs of socks is {pairs}")
    # pair remaining unpaired clean socks with identical sock in the dirty list
    else:
        count = 0
        for num in dirty:
            for i in cleanunpaired:
                if num == i:
                    count += 1
                    dirty.remove(num)
            if count == noOfWashes:
                break
        if (noOfWashes - count) > 1:
            rem = noOfWashes - count
            setdirty = set(dirty)
            for num in setdirty:
                if dirty.count(num) >= 2:
                    if dirty.count(num) >= rem:
                        if rem % 2 == 0:
                            pairs += rem / 2
                        else:
                            pairs += (rem - 1) / 2
                        break
                    else:
                        if dirty.count(num) % 2 == 0:
                            pairs += dirty.count(num) / 2
                        else:
                            pairs += (dirty.count(num) - 1) / 2
            print(f"maximum pairs of socks is {pairs + count}")
        else:
            print(f"maximum pairs of socks is {pairs + count}")


# Run function to test it
clean = [1, 1, 1, 1, 2]
dirty = [1, 4, 3, 2, 4, 2]
noOfWashes = 3
countpairs(clean, dirty, noOfWashes)
