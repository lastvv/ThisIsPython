#Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('x y z Первое выражение; второе выражение')
for x in range(2):
    for y in range(2):
        for z in range(2):
            result = not x and not y and not z
            result2 = not(x or y or z)
            print(x,y,z,'  ',result,'    ',result2)
if result == result2:
    print('равенство истинно')
else:
    print('равенство ложно')
            