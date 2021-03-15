# import operator
#
# def accumulate(iterable, func = operator.add, *, initial=None):
#     'Return running totals'
#     # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
#     # accumulate([1,2,3,4,5], initial=100) --> 100 101 103 106 110 115
#     # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
#     it = iter(iterable)
#     total = initial
#     if initial is None:
#         try:
#             total = next(it)
#         except StopIteration:
#             return
#     yield total
#     for element in it:
#         total = func(total, element)
#         yield total
#
#
#
# if __name__ == '__main__':
#     data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
#     list(accumulate(data, operator.mul))
#     print (list)

# class first_n(object):
#
#     def __init__(self, n):
#         self.n = n
#         self.num = 0
#
#     def __iter__(self):
#         return self
#
#     # Python 3 compatibility
#     def __next__(self):
#         return self.next()
#
#     def next(self):
#         if self.num < self.n:
#             cur, self.num = self.num, self.num + 1
#             return cur
#         raise StopIteration()

#
# def first_n(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
#
#
# if __name__ == '__main__':
#     sum_of_first_n = sum(first_n(6))
#     print(sum_of_first_n)
#
# def filter_odd(x):
#     return x % 2
#
# for x in range(10):
#     if filter_odd(x):
#         print(x)
#     else:
#         print (0)


from itertools import *
for i in permutations("ABC"):
    print(i)

