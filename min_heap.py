heap = [10, 30, 20, 35, 50, 40, 45, 60, 75, 80, 95, 70, 98, 92]

heap_size = 14


def heap_insert(key: int):
    idx = heap_size

    while idx > 0 and key < heap[(idx - 1) / 2]:
        heap[idx] = heap[(idx - 1) / 2]
        idx = (idx - 1) / 2


def heap_delete():
    key = heap[0]

    heap[0] = heap[heap_size - 1]
    heap_size -= 1
    heapify(0)

    return key


def heapify(idx: int):
    parent = idx

    left = idx * 2 + 1
    right = idx * 2 + 2

    if left < heap_size and heap[left] < heap[parent]:
        parent = left

    if right < heap_size and heap[right] < heap[parent]:
        parent = right

    if parent != idx:
        swap(parent, idx)
        heapify(parent)


def swap(idx1: int, idx2: int):
    heap[idx1], heap[idx2] = heap[idx2], heap[idx1]
