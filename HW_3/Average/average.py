def average(lst):

    if not lst: raise ValueError('List is empty')

    return sum(lst) / len(lst)