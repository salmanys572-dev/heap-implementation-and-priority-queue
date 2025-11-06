

import heapq
import time

# ------------------ TASK CLASS ------------------ #
class Task:
    """Represents a task with priority, arrival time, and deadline."""
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        # For max-heap, reverse comparison
        return self.priority > other.priority

    def __repr__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority})"


# ------------------ PRIORITY QUEUE USING HEAP ------------------ #
class PriorityQueue:
    """Implements a priority queue using a max-heap."""
    def __init__(self):
        self.heap = []

    def insert(self, task):
        """Insert a new task (O(log n))."""
        heapq.heappush(self.heap, task)

    def extract_max(self):
        """Remove and return the task with the highest priority (O(log n))."""
        if not self.is_empty():
            return heapq.heappop(self.heap)
        return None

    def increase_priority(self, task_id, new_priority):
        """Increase priority of a given task (O(n) for search + O(log n) reheapify)."""
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                self.heap[i].priority = new_priority
                heapq.heapify(self.heap)
                return
        print("Task not found.")

    def is_empty(self):
        """Return True if heap is empty."""
        return len(self.heap) == 0

    def __repr__(self):
        return f"PriorityQueue({self.heap})"


# ------------------ TASK SCHEDULER SIMULATION ------------------ #
def simulate_scheduler():
    """Demonstrates priority queue usage for task scheduling."""
    print("\n--- Priority Queue Task Scheduler ---")
    pq = PriorityQueue()

    tasks = [
        Task("T1", 3, 0, 5),
        Task("T2", 5, 1, 3),
        Task("T3", 2, 2, 6),
        Task("T4", 4, 3, 4),
    ]

    for t in tasks:
        pq.insert(t)
        print("Inserted:", t)

    print("\nQueue State:", pq)

    print("\nExtracting tasks by priority:")
    while not pq.is_empty():
        print("Processing:", pq.extract_max())

    print("\nIncreasing priority of T3 to 6:")
    pq.insert(Task("T3", 2, 2, 6))
    pq.increase_priority("T3", 6)
    print(pq)


if __name__ == "__main__":
    simulate_scheduler()



