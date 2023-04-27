coin = int(input("Введите кол-во монеток, лежащих на столе: "))
side = input("Введите последовательность сторон монеток, где 'r'-решка, а 'g'-герб: ")
face = 0
back = 0
for i in range(coin):
    if side[i] == 'r':
        face += 1
    elif side[i] == 'g':
        back += 1
if face > back:
    print(back)
elif face == back:
    print(coin//2)
else:
    print(face)


# rightSide = None
# wrongSide = None
# if side > otherSide:
#     for i in otherSide:
        
        





#  rightSide = true
#  wrongSide = true
#  for i in range coin[]:
#      while !rightSide:
#          rightSide = true