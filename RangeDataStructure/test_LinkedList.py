import LinkedList

def test_AddToFrontOfEmptyList():
    list = LinkedList.LinkedList()
    list.insert_front(1)
    assert list.get_all_data() == [1]
    assert list.length == 1
    assert list.head == list.tail

def test_AddToBacktOfEmptyList():
    list = LinkedList.LinkedList()
    list.insert_back(1)
    assert list.get_all_data() == [1]
    assert list.length == 1
    assert list.head == list.tail

def test_AddMultipleToFrontOfList():
    list = LinkedList.LinkedList()
    len = 5
    expected = []
    for i in range(0, len):
        list.insert_front(i)
        expected.append(i)
    assert list.get_all_data() == expected[::-1]
    assert list.length == len
    assert list.head.data == 4
    assert list.tail.data == 0

def test_AddMultipleToEndOfList():
    list = LinkedList.LinkedList()
    len = 5
    expected = []
    for i in range(0, len):
        list.insert_back(i)
        expected.append(i)
    assert list.get_all_data() == expected
    assert list.length == len
    assert list.head.data == 0
    assert list.tail.data == 4

def test_DeleteHeadOfListWithOneElement():
    list = LinkedList.LinkedList()
    list = LinkedList.LinkedList()
    list.insert_back(1)
    assert list.get_all_data() == [1]
    assert list.length == 1
    assert list.head == list.tail
    list.delete(list.head)
    assert list.get_all_data() == []
    assert list.length == 0
    assert list.head == list.tail == None

def test_DeleteTailOfListWithOneElement():
    list = LinkedList.LinkedList()
    list = LinkedList.LinkedList()
    list.insert_back(1)
    assert list.get_all_data() == [1]
    assert list.length == 1
    assert list.head == list.tail
    list.delete(list.tail)
    assert list.get_all_data() == []
    assert list.length == 0
    assert list.head == list.tail == None

def test_DeleteTailOfListWithTwoElement():
    list = LinkedList.LinkedList()
    list = LinkedList.LinkedList()
    list.insert_back(1)
    list.insert_back(2)
    assert list.get_all_data() == [1, 2]
    assert list.length == 2
    list.delete(list.tail)
    assert list.get_all_data() == [1]
    assert list.length == 1
    assert list.head == list.tail

def test_DeleteHeadOfListWithTwoElement():
    list = LinkedList.LinkedList()
    list = LinkedList.LinkedList()
    list.insert_back(1)
    list.insert_back(2)
    assert list.get_all_data() == [1, 2]
    assert list.length == 2
    list.delete(list.head)
    assert list.get_all_data() == [2]
    assert list.length == 1
    assert list.head == list.tail

def test_DeleteMiddleElement():
    list = LinkedList.LinkedList()
    list = LinkedList.LinkedList()
    len = 3
    expected = []
    for i in range(0, len):
        list.insert_back(i)
        expected.append(i)

    assert list.get_all_data() == expected
    assert list.length == len
    list.delete(list.head.next)
    assert list.get_all_data() == [0,2]
    assert list.length == 2