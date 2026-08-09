'''
Topic: Default parameters and recursion -- manual list stats, tiered bonus
calculation, string padding/truncation, and recursive functions
'''

##############################################
def drop_smallest(lst, drop=2):
##############################################
    temp = []

    # copy elements so we don't mess up original list
    for i in range(len(lst)):
        temp.append(lst[i])

    # remove the smallest value 'drop' times
    for i in range(drop):
        smallest = temp[0]

        # find smallest value manually
        for j in range(len(temp)):
            if temp[j] < smallest:
                smallest = temp[j]

        # remove first occurrence of that smallest value
        for k in range(len(temp)):
            if temp[k] == smallest:
                del temp[k]
                break

    total = 0

    # calculate sum of remaining values
    for i in range(len(temp)):
        total = total + temp[i]

    # return average rounded to 2 decimals
    return round(total / len(temp), 2)


##############################################
def calculate_bonus(salary, performance=3, experience=1):
##############################################
    percent = 5  # base bonus

    # add bonus based on performance rating
    if performance == 5:
        percent = percent + 10
    elif performance == 4:
        percent = percent + 7
    elif performance == 3:
        percent = percent + 5
    elif performance == 2:
        percent = percent + 2
    elif performance == 1:
        percent = percent + 0

    # add experience bonus (1% per year)
    percent = percent + experience

    # calculate final bonus amount
    return salary * (percent / 100)


##############################################
def truncate(lst, max_len=5, suffix='.'):
##############################################
    result = []

    for i in range(len(lst)):
        word = lst[i]

        # cut word if it's too long
        if len(word) > max_len:
            result.append(word[:max_len])

        # pad word if it's too short
        elif len(word) < max_len:
            new_word = word
            needed = max_len - len(word)

            for j in range(needed):
                new_word = new_word + suffix

            result.append(new_word)

        # leave word unchanged if correct length
        else:
            result.append(word)

    return result


##############################################
def replaceLetter(word, char, new_char):
##############################################
    # base case: empty string
    if word == "":
        return ""

    # replace first character if it matches
    if word[0] == char:
        return new_char + replaceLetter(word[1:], char, new_char)
    else:
        return word[0] + replaceLetter(word[1:], char, new_char)


##############################################
def helper_sum(number):
##############################################
    # base case for digit sum
    if number == 0:
        return 0

    # add last digit and recurse
    return number % 10 + helper_sum(number // 10)


##############################################
def sum_digits(number):
##############################################
    # stop when number is a single digit
    if number < 10:
        return number

    # sum digits once
    total = helper_sum(number)

    # repeat until result is one digit
    return sum_digits(total)
