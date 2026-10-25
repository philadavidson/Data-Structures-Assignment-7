class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        while index > 0:
            # Find the current patient's parent
            parent_index = (index - 1) // 2
            current_patient = self.data[index] 
            parent_patient = self.data[parent_index]

            # A lower urgency score moves toward the root
            if current_patient.urgency < parent_patient.urgency:
                # Swap the patient with their parent 
                temp = self.data[index]
                self.data[index] = self.data[parent_index]
                self.data[parent_index] = temp

                # Continue checking from the parent's position
                index = parent_index
            else: 
                break
        
    def heapify_down(self, index):
        # Find both child positions 
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index 

        # Compare the left child with the current smallest score
        if (left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency):
            smallest = left

        # Compare the right child with the smallest score found so far
        if (right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency):
            smallest = right

        # Move down only if a child has a lower urgency score
        if smallest != index:
            temp = self.data[index]
            self.data[index] = self.data[smallest]
            self.data[smallest] = temp
        
            # Continue checking from the patient's new position
            self.heapify_down(smallest)


    def insert(self, patient):
        self.data.append(patient) 
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("\nCurrent Patients")
        for patient in self.data:
            print(f"-{patient.name} (Urgency: {patient.urgency})")

    def peek(self):
        # An empty heap has no next patient
        if not self.data:
            return None

        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None

        # Save the highest-priority patient to return
        patient = self.data[0]

        # Remove the last patient from the list
        last_patient = self.data.pop()

        # If patients remain, move the last patient to the root
        if self.data:
            self.data[0] = last_patient
            self.heapify_down(0)

        return patient

# Demonstrate queue operations
heap = MinHeap()
heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))

heap.print_heap()

# Remove and display the highest priority patient
served = heap.remove_min()
if served is not None:
    print("Serving:", served.name)
else:
    print("No patients waiting.")

print("\nAfter serving a patient:")
heap.print_heap()

# Edge case tests
# One patient, removing them should leave an empty heap
heap = MinHeap()
heap.insert(Patient("Jordan", 3))

assert heap.peek().name == "Jordan"
assert len(heap.data) == 1  # Peek should not remove anything
assert heap.remove_min().name == "Jordan"
assert heap.peek() is None
assert heap.remove_min() is None

# Insert in reverse priority order
heap = MinHeap()
heap.insert(Patient("Avery", 10))
heap.insert(Patient("Jordan", 5))
heap.insert(Patient("Taylor", 1))

assert heap.remove_min().urgency == 1
assert heap.remove_min().urgency == 5
assert heap.remove_min().urgency == 10

# Equal urgency scores
heap = MinHeap()
heap.insert(Patient("Jordan", 2))
heap.insert(Patient("Taylor", 2))

first = heap.remove_min()
second = heap.remove_min()

assert first.urgency == 2
assert second.urgency == 2
assert {first.name, second.name} == {"Jordan", "Taylor"}
assert heap.peek() is None

# Several levels with insertion after removal
heap = MinHeap()
for urgency in [8, 3, 10, 1, 6, 2, 7]:
    heap.insert(Patient(f"Patient {urgency}", urgency))

assert heap.remove_min().urgency == 1
assert heap.remove_min().urgency == 2

heap.insert(Patient("New urgent patient", 1))

for expected in [1, 3, 6, 7, 8, 10]:
    assert heap.remove_min().urgency == expected

assert heap.peek() is None

print("\nAll edge-case tests passed!")


# Design Memo

# Trees are appropriate for doctor structure, or any employee reporting structure, since it preserves management relationships and 
# lets software traverse an entire reporting branch. This is decidedly different from a queue, like the emergency_queue.py, which 
# maintains enough order to keep the most urgent patient at the root. Trees, on the other hand, might have several elements below 
# each node. With our binary tree, each node had at most two children.

# Preorder (root, left, right): Processing a parent before its children. Software could display a manager before listing who reports to them.
# Inorder (left, root, right): Useful when retrieving sorted information from a binary search tree. Out doctor_tree.py is arranged by reporting relationships, so this 
# traversal does not automatically produce alphabetical order.
# Postorder (left, right, root): Useful for processing children before parent. Could be used to delete folder contents before deleting 
# the folder, or calculating totals of a departments before combining them into a store wide total.

# Heaps are a type of binary tree that allow you to implement a priority queue. Emergency intakes and task lists are great examples of where heaps 
# are implemented. Each patient has an urgency score, and the heap keeps the patient with the lowest score at the root. As patients arrive or are served, 
# heap operations restore this ordering efficiently without sorting the entire list. This allows newly arriving urgent cases to move ahead of less urgent patients.

