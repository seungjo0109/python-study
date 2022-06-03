
# example 1
# student_heights = input("Input a list of student heights ").split()

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# total_height = 0

# for height in student_heights:
#     total_height += height
# print(total_height)

# example 2
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])

# highest_score = 0
# for score in student_scores:
#     if highest_score < score:
#         highest_score = score
# print(highest_score)

# example 3
# sum_even = 0
# for n in range(2, 101, 2):
#     sum_even += n
# print(sum_even)

# example 4
for n in range(1,101):
    if n%3 == 0 and n%5 == 0:
        print("FizzBuzz")
    elif n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else:
        print(n)