simple_list  = ['one', 'two', 'three']
print (simple_list)
print (f"first in list : {simple_list[0]} , last in list : {simple_list[-1]}")


simple_list[1]= '2222'
print(f"modiefied list : {simple_list}")

simple_list.append('4444')
print(f"append list list : {simple_list}")

empty_list = []
print (f"type of obj : {type(empty_list)}")
empty_list.append('one')
print (f"add elemnt to list : {empty_list}")
empty_list.insert(0,'zero')
print (f"add elemnt to list in pos = 0 : {empty_list}")

del simple_list[1]
print(f"remove from list : {simple_list}")

pop_item = simple_list.pop()
print(f"did pop last item : {pop_item} from list : {simple_list}")

pop_item = simple_list.pop(-1)
print(f"did pop first item : {pop_item} from list : {simple_list}")

simple_list.remove('one')
print(f"did remove item by name from list : {simple_list}")

number_list = [111, 300, 222, 122, 133]
sorted_list = number_list
sorted_list.sort()
revers_list = number_list
revers_list.sort(reverse=True)
print(f"sorted list : {number_list} in reverse : {revers_list}")


print(f"
      temp sorted list : {sorted(number_list)} orginal list : {number_list}")
