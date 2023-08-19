# # Return two distinct highest values in a list
# def two_highest(arg1):
#     return sorted(set(arg1), reverse=True)[:2]
#
#
# my_list = [15, 20, 20, 17]
# print(two_highest(my_list))

# # Return true if the 2nd string only has elements in 1st string
# def solution(text, ending):
#     return text.endswith(ending)
#
#
# start = "abc"
# end = "b"
# print(solution(start, end))

# # Duplicate encoder, print '(' if not duplicated, print ')' if duplicated
# def duplicate_encode(word):
#     # word = word.lower()
#     # encoded_str = ''
#     # for char in word:
#     #     if word.count(char) == 1:
#     #         encoded_str += '('
#     #     elif word.count(char) > 1:
#     #         encoded_str += ')'
#     # return encoded_str
#     return ''.join(['(' if word.lower().count(c) == 1 else ')' for c in word.lower()])
#
#
# test = "din"
# test2 = "recede"
# print(duplicate_encode('TTG) @'))

#
# # An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# def is_isogram(string):
#     # # My solution
#     # string = string.lower()
#     # for char in string:
#     #     if string.count(char) > 1:
#     #         return False
#     # return True
#
#     # Best practice
#     return len(string) == len(set(string.lower()))
#
#
# print(is_isogram("Dermatoglyphics"))
# # isIsogram "Dermatoglyphics" = true
# # isIsogram "moose" = false
# # isIsogram "aba" = false

# dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
# dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
# dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
# dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

def dig_pow(n, p):
    sum_list = []
    for num in str(n):
        sum_list.append(int(num) ** p)
        p += 1
    print(sum_list)
    if sum(sum_list) % n == 0:
        return round(sum(sum_list) / n)
    return -1


print(dig_pow(695, 2))
