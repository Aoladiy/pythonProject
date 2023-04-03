# a = [i for i in range(1, 8)]
# used = []
# result = []
# for i in range(len(a)):
#     for j in range(len(a)):
#         t = {a[i], a[-1 - j]}
#         if t not in used:
#             used.append(t)
#         else:
#             continue
#         if (a[i] ** 2 + a[-1-j] ** 2) <= 49:
#             print(f"a = {a[i]} b = {a[-1-j]} y = {(a[i] ** 2 + a[-1-j] ** 2) ** 0.5}")
#             result.append({a[i], a[-1-j], (a[i] ** 2 + a[-1-j] ** 2) ** 0.5})
while True:
    a = int(input("a = "))
    b = int(input("b = "))
    print((a ** 2 + b ** 2) ** 0.5)
