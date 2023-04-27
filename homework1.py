# coin = int(input("Введите кол-во монеток, лежащих на столе: "))
# side = input("Введите последовательность сторон монеток, где 'r'-решка, а 'g'-герб: ")
# face = 0
# back = 0
# for i in range(coin):
#     if side[i] == 'r':
#         face += 1
#     elif side[i] == 'g':
#         back += 1
# if face > back:
#     print(back)
# elif face == back:
#     print(coin//2)
# else:
#     print(face)

print("Загадайте два числа от 0 до 1000")
sum = int(input("Введите сумму этих двух чисел: "))
product = int(input("Введите произведение этих двух чисел: "))
solution = False
while solution != True:
    for i in range(1, sum):
        firstNum = sum - i
        if firstNum * i == product:
            print(firstNum, i)
            solution = True







        
        





#  rightSide = true
#  wrongSide = true
#  for i in range coin[]:
#      while !rightSide:
#          rightSide = true