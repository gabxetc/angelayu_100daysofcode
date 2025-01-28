test_scores = [88, 75, 92, 67, 81, 90, 78, 84, 95, 72, 86, 93, 69, 80, 89, 77, 91, 85, 87, 83, 94, 74, 76, 68, 82]

# max = 95

''' What I did '''

# index_num = 0
# max_num = 0
# min_list = []

# for scores in test_scores:

#     scores_index_num = test_scores[index_num]

#     if scores >= scores_index_num and scores_index_num not in min_list:
#         max_num = scores
#     else:
#         index_num += 1
#         min_list.append(scores_index_num)

# print(max_num)

''' What's right '''

max_num = 0

for scores in test_scores:
    if scores > max_num:
        max_num = scores
    else:
        pass

print(max_num)