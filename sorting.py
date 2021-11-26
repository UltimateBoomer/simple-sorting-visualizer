import numpy as np
import time
import random

from numpy.random.mtrand import shuffle

class sorting:
    def __init__(self, size, write_delay=1.0):
        self.size = size
        self.array = np.arange(start=1, stop=size+1, step=1)
        self.anno = np.zeros(size)
        self.write_delay = write_delay
        
        self.reset()
    
    def reset(self):
        self.is_sorting = False
        self.waiting = False

    def shuffle(self, amount=1.0, seed=None):
        self.clear_anno()
        if seed != None:
            random.seed(seed)
        else:
            random.seed()
        for i in range(self.size - 1, 0, -1):
            n = random.randint(0, i)
            if amount == 1.0 or random.random() < amount:
                self.swap(i, n)
        self.clear_anno()

    def reverse(self):
        self.clear_anno()
        for i in range(self.size // 2):
            self.swap(i, self.size - i - 1)
        self.clear_anno()
    
    def compare(self, a, b, clear = True):
        aa, ab = self.array[a], self.array[b]
        if clear:
            self.clear_anno()
        self.anno[a] = self.anno[b] = 3
        time.sleep(self.write_delay)
        return 1 if aa > ab else 0 if aa == ab else -1

    def swap(self, a, b, clear = True):
        self.array[a], self.array[b] = self.array[b], self.array[a]
        if clear:
            self.clear_anno()
        self.anno[a] = self.anno[b] = 2
        time.sleep(self.write_delay)

    def read(self, i, clear = True):
        time.sleep(self.write_delay)
        if clear:
            self.clear_anno()
        self.anno[i] = 1
        return self.array[i]
    
    def write(self, i, n, clear = True):
        time.sleep(self.write_delay)
        if clear:
            self.clear_anno()
        self.anno[i] = 2
        self.array[i] = n
    
    def clear_anno(self):
        self.anno = np.zeros(self.size)

    def check_sorted(self):
        self.clear_anno()
        self.anno[0] = 1
        for i in range(1, self.size):
            if not self.compare(i, i - 1) > -1:
                return False

        self.anno[0:self.size] = 1
        return True

    def bubble_sort(self):
        for i in range(self.size):
            for j in range(self.size - i - 1):
                if self.is_sorting == False:
                    return
                if self.compare(j, j + 1) == 1:
                    self.swap(j, j + 1)

        self.check_sorted()
        self.is_sorting = False

    def insertion_sort(self):
        for i in range(1, self.size):
            j = i - 1
            while j >= 0 and self.compare(j + 1, j) == -1:
                self.swap(j, j + 1)
                j -= 1

        self.check_sorted()
        self.is_sorting = False

    def shaker_sort(self):
        for i in range(self.size // 2):
            for j in range(i, self.size - i - 1):
                if self.compare(j, j + 1) == 1:
                    self.swap(j, j + 1)

            for j in range(self.size - i - 2, i - 1, -1):
                if self.compare(j, j + 1) == 1:
                    self.swap(j, j + 1)

        self.check_sorted()
        self.is_sorting = False

    def shaker_sort(self):
        for i in range(self.size // 2):
            for j in range(i, self.size - i - 1):
                if self.compare(j, j + 1) == 1:
                    self.swap(j, j + 1)

            for j in range(self.size - i - 2, i - 1, -1):
                if self.compare(j, j + 1) == 1:
                    self.swap(j, j + 1)

        self.check_sorted()
        self.is_sorting = False

    def selection_sort(self):
        for i in range(self.size - 1, -1, -1):
            max = 0
            for j in range(i + 1):
                if self.compare(max, j) == -1:
                    max = j
            if max == i:
                continue
            self.swap(max, i)

        self.check_sorted()
        self.is_sorting = False

    def bogo_sort(self):
        random.seed()
        while not self.check_sorted():
            for i in range(self.size - 1, 0, -1):
                n = random.randint(0, i)
                self.swap(i, n)

        self.is_sorting = False

    def sandwich_sort(self):
        for i in range(self.size // 2):
            max = i
            min = i
            for j in range(i, self.size - i):
                if self.compare(max, j) == -1:
                    max = j
                if self.compare(min, j) == 1:
                    min = j
            if min == max:
                break
            if min == i and max == self.size - i - 1:
                continue
            
            self.swap(min, i)
            
            if max == i:
                max = min

            self.swap(max, self.size - i - 1)
            
        self.check_sorted()
        self.is_sorting = False

    def shell_sort(self):
        i = 1
        while i < self.size // 3:
            i = 3 * i + 1
        
        while i > 0:
            for j in range(i, self.size):
                n = j
                while n >= i and self.compare(n - i, n) == 1:
                    self.swap(n - i, n)
                    n = n - i

            i = (i - 1) // 3

        self.check_sorted()
        self.is_sorting = False

    def merge_sort(self):
        self.check_sorted()
        self.is_sorting = False

    def _merge_sort(self, a, b):
        if a > b:
            return
        m = (a + b) // 2
        self._merge_sort(a, m)
        self._merge_sort(m + 1, b)
        self._merge(a, m, b)
    
    def _merge(self, a, m, b):
        pass
            

