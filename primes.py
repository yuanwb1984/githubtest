# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:03:06 2016

@author: 06210
"""

import itertools
  
def primes(): 
    numbers = itertools.count(2) 
    while True: 
        p = numbers.__next__()
        numbers = itertools.filterfalse(lambda x, p=p: x%p, numbers) 
        yield p 
          
print(list(itertools.islice(primes(), 1000)))