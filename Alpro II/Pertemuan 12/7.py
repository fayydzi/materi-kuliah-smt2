def segitiga(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(segitiga(3, 4, 5))