#
# # Dictionary comprehension in python
#
# square_dict=dict()
# for num in range(1,11):
#     square_dict[num]=num*num
# print(square_dict)
#
# # Using dictionary comprehension
# square_dict={num:num*num for num in range(1,11)}
# print(square_dict)
#
# # How to use dictionary comprehension
#
# old_price={'milk':1.02,'coffee':2.5,'bread':2.5}
# dollar_to_pound=0.76
# new_price={item:value*dollar_to_pound for(item,value) in old_price.items()}
# print(new_price)
#
# original_dict={'jack':38,'michael':48,'guido':57,'john':33}
# even_dict={k:v for (k,v) in original_dict.items() if v%2==0}
# print(even_dict)
#
# original_dict={'jack':38,'michael':48,'guido':57,'john':33}
# new_dict={k:v for (k,v) in original_dict.items() if v%2!=0 if v<40}
# print(new_dict)
#
# original_dict={'jack':38,'michael':48,'guido':57,'john':33}
# new_dict_1={k: ('old' if v>40 else 'young') for k,v in original_dict.items()}
# print(new_dict_1)
#
# # Nested dictionary comprehension
#
# dictionary={k1:{k2:k1*k2 for k2 in range(1,6)} for k1 in range(2,5)}
# print(dictionary)
#
# # dictionary=dict()
# for k1 in range(11,16):
#     dictionary[k1]={k2:k1*k2 for k2 in range(1,6)}
# print(dictionary)


# B. List Comprehension

# Iterating through a string using for loop
# h_letters=[]
# for letter in 'human':
#     h_letters.append(letter)
# print(h_letters)
#
# # Using List comprehension
# h_letters=[letter for letter in 'human']
# print(h_letters)
#
# # List Comprehension Vs Lambda functions
#
# letters=list(map(lambda x:x,'human'))
# print(letters)
#
# # Conditionals in list comprehension
# numbers_list=[x for x in range(20) if x%2==0]
# print(numbers_list)
#
# # Nested if with list comprehension
# num_list=[y for y in range(100) if y%2==0 if y%5==0]
# print(num_list)
#
# # if ...else with list comprehension
# obj=['Even' if i%2==0 else 'odd' for i in range(10)]
# print(obj)
#
# # Transpose of matrix using nested loops
# transposed=[]
# matrix=[[1,2,3,4],[4,5,6,8]]
# for i in range(len(matrix[0])):
#     transposed_row=[]
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
# print(transposed)
#
# # Transpose of a matrix using list comprehension
# matrix=[[1,2],[3,4],[5,6],[7,8]]
# transpose=[[row[i] for row in matrix] for i in range(2)]
# print(transpose)
