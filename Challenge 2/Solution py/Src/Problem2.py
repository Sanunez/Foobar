n = "1211"
b = 10
k = len(n)
count = 1
pattern = []
string = n

def reps(n, b):
    def numtobase(n, b):
        num = []
        fin = []
        f = n
        while f != 0:
            num.append(f % b)
            f = f / b
        fin = num
        fin.reverse()
        return fin

    ascending = [int(i) for i in n]
    descending = [int(i) for i in n]

    ascending.sort()
    descending.sort()
    descending.reverse()

    x = 0
    y = 0

    for i in range(0, len(ascending)):
        y += ascending.pop() * (b ** i)
        x += descending.pop() * (b ** i)

    z = numtobase((x - y), b)
    while (len(z) < k):
        z.insert(0, 0)
    basestr = ''.join(str(e) for e in z)
    return basestr

while string not in pattern:
    pattern.append(string)
    string = reps(string, b)
pattern.append(string)
numOcc = (len(pattern)-1 - pattern.index(pattern.pop()))
print pattern, numOcc