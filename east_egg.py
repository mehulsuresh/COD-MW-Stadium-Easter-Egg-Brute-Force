# list = ["7","h","h","0","n","n","4","n"]
# list = ["c","n","n","5","n","0","3","h"]
# list = ["2","h","1","c","h","n","8","n"]
list =[]
numbers = [0,1,2,3,4,5,6,7,8,9]
nums=[]
def china_room(numbers,list,cnt=0):
    for i in numbers:
        temp_lst_a = [lst if lst!="h" else str(i) for lst in list]

        for j in numbers:
            if j != i:
                print([lst if lst!="n" else str(j) for lst in temp_lst_a])
                cnt+=1
    print(cnt)

def house_room(numbers,nums,list,cnt=0):
    for i in nums:
        temp_lst_a = [lst if lst!="h" else str(i) for lst in list]
        for j in numbers:
           for k in numbers:
               if k!=j:
                   temp_lst_b = [lst if lst!="c" else str(j) for lst in temp_lst_a]
                   print([lst if lst!="n" else str(k) for lst in temp_lst_b])
                   cnt+=1
    print(cnt)
def nose_room(numbers,nums,list,cnt=0):
    for i in nums:
        temp_lst_a = [lst if lst!="n" else str(i) for lst in list]
        for j in numbers:
           for k in numbers:
               if k!=j:
                   temp_lst_b = [lst if lst!="c" else str(j) for lst in temp_lst_a]
                   print([lst if lst!="h" else str(k) for lst in temp_lst_b])
                   cnt+=1
    print(cnt)
print("Enter the values as a digit or c or h or n")
for i in range(8):
    list.append(input(f"value {i}:"))
for i in list:
  if i.isnumeric():
      nums.append(int(i))
for i in nums:
    numbers.remove(i)
if "c" not in list:
    print("China Room")
    china_room(numbers,list)
if list.count("h") == 1:
    print("House Room")
    house_room(numbers,nums,list)
if list.count("h") == 2 and list.count("c") == 1:
    print("Nose Room")
    nose_room(numbers,nums,list)
