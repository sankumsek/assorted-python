#Final Project
infile = open('fares.txt')
location = {}
tuple = {}
money = {}
for line in infile:
    data = line.strip().split('\t')
    origin = data[0]
    end = data[1]
    cost = int(data[2])
    location(origin) = 1
    location(end) = 1
    money[(origin, end)] = cash
for j in (money.keys()):
    x = j
    for i in (money.keys()):
        y = i
        m = (a,b)
        if m in money:
            icost = (int(money[m]))
            value = 50
            for v in (location.keys()):
                z = v
                a1 = (x, z)
                a2 = (z, y)
                if a1 in money and a2 in money:
                    tcost = int(money[a1]) + int(money[a2])
                    fcost = icost - tcost
                    if value >= fcost:
                        value = fcost
                        k = tcost
                        s = z
            if value != 50:
                print('(0:3s)-(1:3s): (2:3d) direct; $(3:3d) via (4:3s); save(5:3d)'.format(x, y, icost, k, s))
