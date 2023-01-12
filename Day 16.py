
# Python Collections module

from collections import Counter
# cnt=Counter()
# list=[1,2,3,4,1,2,6,7,3,8,1]
# Counter(list)
# Counter({1:3,2:4})
# cnt=Counter(list)
# print(cnt[1])

# Element function

# cnt=Counter({1:3,2:4})
# print(list(cnt.elements()))
#
# # Most Common function
#
# list=[1,2,3,4,1,2,6,7,3,8,1]
# cnt= Counter(list)
# print(cnt.most_common())
#
# # The Subtract function
#
# cnt=Counter({1:3,2:4})
# deduct={1:1,2:2}
# cnt.subtract(deduct)
# print(cnt)
#
# # The defaultdict
#
# from collections import defaultdict
#
# # Create a defaultdict
# nums=defaultdict(int)
# nums['one']=1
# nums['two']=2
# print(nums['three'])
#
# count=defaultdict(int)
# names_list="Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
# for names in names_list:
#     count[names]+=1
# print(count)

# The OrderedDict

# from collections import OrderedDict
# od=OrderedDict()
# od['a']=1
# od['b']=2
# od['c']=3
# print(od)

# for key,value in od.items():
#     print(key,value)

# list=["a","c","c","a","b","a","a","b","c"]
# cnt=Counter(list)
# od=OrderedDict(cnt.most_common())
# for key,value in od.items():
#     print(key,value)

# The deque
# Importing the deque

# from collections import deque
# list=["a","b","c"]
# deq=deque(list)
# print(deq)

# Inserting elements to deque
# deq.append("d")
# deq.appendleft("e")
# print(deq)

# Removing elements from the deque

# deq.pop()
# deq.popleft()
# print(deq)

# Clearing the deque
# print(deq)
# print(deq.clear())

# Counting elements in a deque
# print(deq.count("a"))

# The ChainMap
# from collections import ChainMap

# Create a ChainMap

# dict1={'a':1,'b':2}
# dict2={'c':3,'b':4}
# chain_map=ChainMap(dict1,dict2)
# print(chain_map.maps)
#
# print(chain_map['a'])
#
# dict2['c']=5
# print(chain_map.maps)

# Getting Keys and values from chainmap

# dict1={'a':1,'b':2}
# dict2={'c':3,'b':4}
# chain_map=ChainMap(dict1,dict2)
# print(list(chain_map.keys()))
# print(list(chain_map.values()))

# Adding new Dictionary to ChainMap

# dict3={'e':5,'f':6}
# new_chain_map=chain_map.new_child(dict3)
# print(new_chain_map)

# The namedtuple()

# from collections import namedtuple
# Student=namedtuple('Student','fname,lname,age')
# s1=Student('John','Clarke','13')
# print(s1.fname)

# Creating named tuple Using List

# s2=Student._make(['Adam','joe','18'])
# print(s2)

# Creating a New instance Using Existing Instance

# s2=s1._asdict()
# print(s2)

# Changing field values with _replace() Function

# s2=s1._replace(age='14')
# print(s1)
# print(s2)
