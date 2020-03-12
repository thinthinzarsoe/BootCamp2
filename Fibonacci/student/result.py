import student
import mary

x = student.a["code"]
y = student.b["code"]
z = student.a["student"]
print(x, ' ', y, ' ', z,)

x = student.a["age"]
y = student.a["father"]
z = student.b["mother"]
p = student.b["student"]
print(x, ' ', y, ' ', z, ' ', p)

for i in range(len(mary.a)):
	print(i, mary.a[i])