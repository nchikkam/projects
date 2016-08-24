words = raw_input().split(' ')
M = int(raw_input())

words_dict = {word:0 for word in words}
hotel_dict = {}

for i in range(M):
    hotel_id = int(raw_input())
    review = raw_input()

    if not hotel_id in hotel_dict:
        hotel_dict[hotel_id] = 0

    for word in words_dict:
        if word in review:
            hotel_dict[hotel_id] += 1

print sorted(hotel_dict, key=lambda k: hotel_dict[k], reverse=True)
"""
Sample Example:
a b c ==> keywords
2     --> no of reviews
1     -> review for hotel#1
a d        -> review comments for hotel#1
2     -> review for hotel#2
c          -> review comments for hotel#2

as per the reviews containing keywords, the sorted order is 2, 1
"""