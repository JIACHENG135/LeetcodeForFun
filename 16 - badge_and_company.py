def badge1(entry_list):
    count = {}
    exitWithoutBadge = set()
    enterWithoutBadge = set()

    for entry in entry_list:
        name = entry[0]
        action = entry[1]
        prev = count.get(name, None)
        if action == "enter":
            if prev is not None and prev != 0:
                exitWithoutBadge.add(name)
            prev = 1
        else:
            if prev is None or prev == 0:
                enterWithoutBadge.add(name)
            prev = 0
        count[name] = prev

    for person in count:
        if count[person] > 0:
            exitWithoutBadge.add(person)

    print("enter without badge:", enterWithoutBadge)        
    print("exit without badge:", exitWithoutBadge)        

def badge1_(entry_list):
    exit_set = set()
    enter_set = set()
    count = {}

    for entry in entry_list:
        id = entry[0]
        action = entry[1]
        prev = count.get(id, None)
        if action == "enter":
            if prev is not None and prev != 0:
                exit_set.add(id)
            prev = 1
        elif action == "exit":
            if prev is None or prev == 0:
                enter_set.add(id)
            prev = 0
        count[id] = prev
    
    for k,v in count.items():
        if v > 0:
            exit_set.add(k)
    
    print(enter_set)
    print(exit_set)


test1 = [
    ["Martha", "exit"],
    ["Paul", "enter"],
    ["Martha", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "enter"],
    ["Paul", "enter"],
    ["Curtis", "enter"],
    ["Paul", "exit"],
    ["Martha", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "exit"]
]

badge1(test1)
badge1_(test1)

test2 = [
    ["Paul", 1355],
    ["Jennifer", 1910],
    ["John", 830],
    ["Paul", 1315],
    ["John", 835],
    ["Paul", 1405],
    ["Paul", 1630],
    ["John", 855],
    ["John", 915],
    ["John", 930],
    ["Jennifer", 1335],
    ["Jennifer", 730],
    ["John", 1630]
]

def badge2(badge_records):
    person_record = {}
    for record in badge_records:
        name = record[0]
        time = record[1]
        if name not in person_record:
            person_record[name] = []
        person_record[name].append(time)
    
    res = {}
    for person in person_record:
        times = person_record[person]
        times.sort()

        for i in range(len(times)):
            count = oneHourContain(times, i)
            if count >= 3:
                tmp = []
                for j in range(i, i + count):
                    tmp.append(times[j])
                res[person] = tmp
                break

    print(res)

def oneHourContain(times, startIdx):
    endVal = times[startIdx] + 100
    i = startIdx
    count = 0
    while i < len(times) and times[i] <= endVal:
        count += 1
        i += 1

    return count

badge2(test2)