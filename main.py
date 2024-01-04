graph = {}
with open("graph.txt", "r") as f:
    for line in f:
        key, *value = line.split()
        graph[key] = value
print(graph)

arr=[]
for key in graph.keys():
    arr.append(graph.get(key))

graphMatrixKeys = list(graph.keys())

WayC = False
WayB = False
def Search(Key, checkedKeys,search):
    if Key in checkedKeys:
        return "0"
    if "-1" in arr[graphMatrixKeys.index(Key)]:
        indexMinusOne = []
        for i in range(len(arr[graphMatrixKeys.index(Key)])):
            if arr[graphMatrixKeys.index(Key)][i] == "-1":
                indexMinusOne.append(i)
        vershinaMinusOne = []
        for i in range(len(arr)):
            for index in indexMinusOne:
                if arr[i][index] == "1":
                    vershinaMinusOne.append(i)
        vershinaKeys = []
        for elem in vershinaMinusOne:
            vershinaKeys.append(graphMatrixKeys[elem])
        if search not in vershinaKeys:
            checkedKeys.append(Key)
            for elem in vershinaKeys:
                if elem in graphMatrixKeys:
                    Search(elem, checkedKeys,search)
        else:
            if search == "C":
                global WayC
                WayC = True
                return "0"
            else:
                global WayB
                WayB = True
                return "0"
Search("A",[],"C")
Search("C",[],"B")


if WayB and WayC:
    print("Можно проехать")
else:
    print("Нельзя проехать")
