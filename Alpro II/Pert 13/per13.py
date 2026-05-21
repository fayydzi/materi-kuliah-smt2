#nomor 1
t = ( 1, 2, 3, "Dorrr")
print(t)

#NOmor 2
t = ("a", "b", "c")
print(t[0])
print(t[1])

#Nomor 3
t = (1, 2, 3)
# t[0] = 10  # ini akan error

#Nomor 4
tuple1 = (1, 2, 3)
tuple2 = (4, 5)

print(len(tuple1))
print(tuple1 + tuple2)
print(tuple1 * 2)
print(2 in tuple1)
print(10 not in tuple1)

#Nomor 5
a = 10
b = 20

a, b = b, a
print(a, b)

#Nommor 6
data = {"nama": "mingyu", "nilai": 100}
print(data)

#Nomor 7
data = {"nama": "mingyu", "nilai": 100}
print(data["nilai"])

#Nomor 8
data = {"a": 10, "b": 20, "c": 30}
print(data.keys())

#Nomor 9
data = {"a": 10, "b": 20, "c": 30}
print(data.values())

#Nomor 10
data = {"x": 1, "y": 2}
print(data.items())

#Nomor 11
data = {"nama": "faii"}
data.update({"kelas": "A"})
print(data)

#Nomor 12
data = {"a": 1, "b": 2, "c": 3}
data.popitem()
print(data)

#Nomor 13
data = {"nama": "Budi"}
data["nama"] = "Andi"
data["umur"] = 19

print(data)

#Nomor 14
try:
    angka = int("salah")
except:
    print("Input tidak valid")

#Nomor 15
try:
    x = int("10a")
    y = 5 / 0
except ValueError:
    print("Terjadi kesalahan konversi")
except ZeroDivisionError:
    print("Tidak bisa dibagi nol")
