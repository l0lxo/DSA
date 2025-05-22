# Palindrome Check Using Stack and Queue (HackerRank Day 18 Inspired)

from collections import deque

class PalindromeChecker:
    def __init__(self):
        self.stack = []         # Stack: LIFO
        self.queue = deque()    # Queue: FIFO

    def push_character(self, ch):
        self.stack.append(ch)

    def enqueue_character(self, ch):
        self.queue.append(ch)

    def pop_character(self):
        return self.stack.pop()

    def dequeue_character(self):
        return self.queue.popleft()

# Main logic
if __name__ == "__main__":
    s = input().strip()

    checker = PalindromeChecker()

    # Load characters into stack and queue
    for char in s:
        checker.push_character(char)
        checker.enqueue_character(char)

    is_palindrome = True
    for i in range(len(s) // 2):
        if checker.pop_character() != checker.dequeue_character():
            is_palindrome = False
            break

    # Output result
    if is_palindrome:
        print(f"The word, {s}, is a palindrome.")
    else:
        print(f"The word, {s}, is not a palindrome.")

#Sample input: racecar
#Output: The word, racecar, is a palindrome.
#Sample input: potato
#Output: The word, potato, is not a palindrome.
