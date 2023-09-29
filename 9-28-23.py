import math
def arrayFinder(list, input):
    #plan
    #binary search for index of rotation point, split the array in half at the rotation point, binary search each one because both are sorted.
    #should be 3*logn or O(logn) running time
    #assume all unique

    #binary search
    rotationPoint = findRotationPoint(list, 0, len(list))
    leftSideSearch = binarySearch(list, 0, rotationPoint, input)
    rightSideSearch = binarySearch(list, rotationPoint, len(list), input)
    
    if leftSideSearch:
        return leftSideSearch
    elif rightSideSearch:
        return rightSideSearch
    else:
        return None

def findRotationPoint(list, left, right):
    middle = math.floor((right - left)/2) + left
    left_1 = left
    right_1 = middle
    left_2 = middle
    right_2 = right

    if list[left] < list[right-1]:
        return left
    
    if list[left_1] > list[right_1-1]:
       return findRotationPoint(list, left_1, right_1) 
    elif list[left_2] > list[right_2-1]:
        return findRotationPoint(list, left_2, right_2)
    else:
        return middle

def binarySearch(list, left, right, target):
    if right - left == 1:
        if list[left] == target:
            return left
        else:
            return None

    middle = math.floor((right - left)/2) + left
    left_1 = left
    right_1 = middle
    left_2 = middle
    right_2 = right


    if list[middle] > target:
        return binarySearch(list, left_1, right_1, target)
    elif list[middle] < target:
        return binarySearch(list, left_2, right_2, target)
    else:
        return middle






#test



def test_findRotationPoint():
    test_l = [4,5 , 1, 2, 3]
    res = findRotationPoint(test_l, 0, len(test_l))
    expected_res = 2
    test_check(expected_res, res, "Testing halves both in order.")

    test_l = [3, 4, 5, 1, 2]
    res = findRotationPoint(test_l, 0, len(test_l))
    expected_res = 3
    test_check(expected_res, res, "Testing right half contains the point.")

    test_l = [5, 1, 2, 3, 4]
    res = findRotationPoint(test_l, 0, len(test_l))
    expected_res = 1
    test_check(expected_res, res, "Testing left half contains the point.")

    test_l = [2, 3, 4, 5, 6, 1]
    res = findRotationPoint(test_l, 0, len(test_l))
    expected_res = 5
    test_check(expected_res, res, "Testing right half contains the point.")

def test_binarySearch():
    l = [1,2, 3, 4]
    res = binarySearch(l, 0, len(l), 1)
    test_check(0, res, "Testing binary search")



def test_ArrayFinder():
    test_list = [13, 18, 25, 2, 8, 10] 
    test_input = 8
    res = arrayFinder(test_list, test_input)
    test_check(4, res, "Testing array finder.")

    test_list = [13,14, 15, 16 ,18, 25, 2, 8, 10, 11, 12] 
    test_input = 8
    res = arrayFinder(test_list, test_input)
    test_check(7, res, "Testing array finder.")
    

def test_check(expected, result, testname):
    if result  == expected:
        print('✅ SUCCESS - ' + testname)
    else:
        print('❌ FAILURE - ' + testname)
        print('Output: ' + str(result))

test_ArrayFinder()
test_findRotationPoint()
test_binarySearch()
#testing