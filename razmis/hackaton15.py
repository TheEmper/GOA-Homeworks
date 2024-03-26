n = 15

plates = [1, 5, 4, 4, 3, 3, 5, 3, 4]

xinkali = 0

plates.sort(reverse=True)

needed_plates =  [1]

for i in plates:
    xinkali += i
    if xinkali >= n:
        break
    else:
        needed_plates.append(1)

if  xinkali >= n:
    print(len(needed_plates))
else:
    print("False")