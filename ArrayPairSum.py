def pair_sum(arr,k):
    cache = {}
    pairs = []

    for num in arr:
        pairing = k - num
        if (pairing in cache) and (cache[pairing] == True):
            pairs.append((min(num, pairing), max(num, pairing)))            
            cache[num] = False
            cache[pairing] = False            
        else:
           cache[num] = True
    
    return None if len(pairs)==0 else pairs

def num_pair_sum(arr,k):
    return len(pair_sum(arr, k))

from nose.tools import assert_equal

assert_equal(num_pair_sum([1,3,2,2,2,3, 5, -1, 0, 4],4),4)
assert_equal(num_pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
assert_equal(num_pair_sum([1,2,3,1],3),1)
assert_equal(num_pair_sum([1,3,2,2],4),2)
print("PASS") 