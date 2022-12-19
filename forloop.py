lists = [int,float,'vikas','kumar',1,2,34,45,6,67,78,89,68,32];

for item in lists:
    if(str(item).isnumeric() and item >= 6):
        print(item);