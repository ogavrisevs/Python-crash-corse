my_list = ['one','two','333','four','555']

for item in my_list: 
    print (item)

for item in range(95, 99): 
    print (item)

list_from_range = list(range(90, 99, 2))
print (f" min : {min(list_from_range)} , max : {max(list_from_range)} , list : list_from_range")

slice_234 = my_list[1:4]
print(slice_234)

slice_123 = my_list[:3]
print(slice_123)

slice_345 = my_list[2:]
print(slice_345)

slice_45 = my_list[-2:]
print(slice_45)

slice_12 = my_list[:-3]
print(slice_12)

copy_list = my_list[:]
del my_list[3]
print (f"type : {type(copy_list)} , contet : {copy_list}")