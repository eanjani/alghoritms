

def quickSort(dataset,):
    print("data: ", dataset)
    if len(dataset)<=1:
        return dataset
    else:
        medium = int(len(dataset)/2)
        pivot = dataset[medium]
        print("pivot: ", pivot)
        lower = [x for x in dataset if x < pivot]
        print("lower: ",lower)
        higher = [y for y in dataset if y > pivot]
        print("higher", higher)
        return quickSort(lower)+[pivot]+quickSort(higher)


data = [2,5,3,7,1,9,8,4,6] #data to sort
result = quickSort(data)
print(result)
