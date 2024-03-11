# task1

# import math

# cemHasil = [3, 5, 10, 26, 11, 16]

# print(sum(cemHasil))

# print(math.prod(cemHasil))

##############################

# a = [5, 10, 15]

# total = 0
# multiply = 1
# for i in a:
#     total += i
#     multiply *= i


# print(total)
# print(multiply)







# task2

# myList = [16, 11, 26]

# myList.reverse()

# print(myList)



# task3 

# a = ["sal", "nece", "qar"]
# b = ["am", "sen", "dash"]



# c = [x + y for x,y in zip(a, b)]
# print(c)




# task4 

# thisList = [["bmw", "mercedes", "vw"], ["toyota", "nissan", "honda"],["yamaha", "kawasaki", "suzuki"]]

# a = thisList[2]
# a.insert(2, "ducati")
# print(thisList)




# task5 


# listem = ["alma", "heyva", "nar"]

# print(listem.index("heyva"))

# listem.insert(1, "banan")
# print(listem)





# task6 

# edediOrta = [5, 9, 11, 15]


# print(sum(edediOrta) / len(edediOrta))






# task7 

# a = int(input("Birinci reqem: "))
# b = int(input("Ikinci reqem: "))
# say = 0

# for i in range(a, b+1):
#     if i %2 == 0:
#         print("Cut ededler: ", i)
#         say += 1
#     else:
#         print("tek ededler: ", i)
# print(say)







# task8 

# tekrarList = [26, 11, 16, 26, 24, 11]

# print(set(tekrarList))






# task9 



# from itertools import combinations

# list123 = [1, 2, 3]

# print(sum([list(map(list, combinations(list123, i))) for i in range(len(list123) + 1)], []))








