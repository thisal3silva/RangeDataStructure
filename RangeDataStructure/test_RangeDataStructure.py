import RangeDataStructure

def test_deleteOfEmptyList():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.delete(0,0) == True

def test_addToEmptyList():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.add(0,2) == True
    assert newRange.get_all() == [[0,2]]

def test_addToEndOfRange():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.add(1,2) == True
    assert newRange.add(3,5) == True
    assert newRange.get_all() == [[1,2], [3,5]]

def test_addToFrontOfRange():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.add(3,4) == True
    assert newRange.add(0,2) == True
    assert newRange.get_all() == [[0,2], [3,4]]

def test_addRangeWithoutMerge():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.add(1,2) == True
    assert newRange.add(5,6) == True
    assert newRange.add(3,4) == True
    assert newRange.get_all() == [[1,2], [3,4], [5,6]]

def test_addRangeWithMerge():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.add(1,4) == True
    assert newRange.add(3,5) == True
    assert newRange.get_all() == [[1,5]]

def test_addRangeWithinExistingRange():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.add(1,6) == True
    assert newRange.add(3,5) == True
    assert newRange.get_all() == [[1,6]]

def test_deleteRange():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.add(1,6) == True
    assert newRange.delete(-1,10) == True
    assert newRange.get_all() == []

def test_deleteWithinRange():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.add(0,9) == True
    assert newRange.delete(1,2) == True
    assert newRange.get_all() == [[0,1],[2,9]]

def test_deleteEndOfRange():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.add(1,6) == True
    assert newRange.delete(4,10) == True
    assert newRange.get_all() == [[1,4]]

def test_deleteOutOfRange():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.add(1,6) == True
    assert newRange.delete(-3,-1) == True
    assert newRange.get_all() == [[1,6]]

def test_deleteBeginningOfRange():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.add(1,6) == True
    assert newRange.add(7,8) == True
    assert newRange.add(10,12) == True
    assert newRange.delete(-3,3) == True
    assert newRange.get_all() == [[3,6],[7,8],[10,12]]

def test_getFromEmpty():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.get(0,5) == []

def test_getFromOutOfRange():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.add(1,3) == True
    assert newRange.add(5,7) == True
    assert newRange.get(4,5) == []

def test_getFromWithinRange():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.add(1,3) == True
    assert newRange.add(5,6) == True
    assert newRange.get(4,6) == [[5,6]]

def test_getFromOverlappingRange():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.add(1,3) == True
    assert newRange.add(5,6) == True
    assert newRange.get(2,9) == [[1,3],[5,6]]

def test_addInvalidRange():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.add(3,1) == False
    assert newRange.add('F',1) == False
    assert newRange.add(1,'F') == False

def test_deleteInvalidRange():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.delete(3,1) == False
    assert newRange.delete('F',1) == False
    assert newRange.delete(1,'F') == False

def test_getInvalidRange():
    newRange = RangeDataStructure.RangeCollection()
    assert newRange.get(3,1) == []
    assert newRange.get('F',1) == []
    assert newRange.get(1,'F') == []

def test_highVolumeAdditionToEnd():
    newRange = RangeDataStructure.RangeCollection()
    expected = []
    volume = 1000
    for i in range(0, volume, 2):
        newRange.add(i, i+1)
        expected.append([i,i+1])
    assert expected == newRange.get_all()

def test_highVolumeAdditionToFront():
    newRange = RangeDataStructure.RangeCollection()
    expected = []
    volume = 1000
    for i in range(1000, 0, -2):
        newRange.add(i, i+1)
        expected.append([i,i+1])
    assert expected[::-1] == newRange.get_all()

def test_highVolumeAdditionToEndWithOverlap():
    newRange = RangeDataStructure.RangeCollection()
    volume = 1000
    for i in range(0, volume, 1):
        newRange.add(i, i+1)
    assert [[0,1000]] == newRange.get_all()

def test_highVolumeAdditionToFrontWithOverlap():
    newRange = RangeDataStructure.RangeCollection()
    volume = 1000
    for i in range(1000, 0, -1):
        newRange.add(i-1, i)
    assert [[0,1000]] == newRange.get_all()