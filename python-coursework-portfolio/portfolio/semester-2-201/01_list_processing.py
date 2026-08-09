'''
Topic: List processing -- filtering, matching, and merging parallel lists
(a small membership/attendance tracking system)
'''

##############################################
def check_enrollment_time(desired_month, season):
##############################################
    months = []
    found = False

    if season == "Spring":
        months = ["March", "April", "May"]
    elif season == "Summer":
        months = ["June", "July", "August"]
    elif season == "Fall":
        months = ["September", "October", "November"]
    elif season == "Winter":
        months = ["December", "January", "February"]

    for month in months:
        if desired_month == month:
            found = True

    return found

##############################################
def upcoming_enrollment(prospective_members, desired_month, season):
##############################################
    result = []
    for i in range(len(prospective_members)):
        if check_enrollment_time(desired_month[i], season):
            result.append(prospective_members[i])
    return result

##############################################
def membership_cancellation(member_list, cancelled_member_ids):
##############################################
    result = []
    for member in member_list:
        remove = False
        for cancelled in cancelled_member_ids:
            if member == cancelled:
                remove = True
        if remove == False:
            result.append(member)
    return result

##############################################
def calculate_membership_fees(member_lst, attendance_lst, base_fee, per_attendance_fee, threshold, discount_percent):
##############################################
    result = []
    for i in range(len(member_lst)):
        total = base_fee + (attendance_lst[i] * per_attendance_fee)
        if total >= threshold and discount_percent > 0:
            total = total - (total * (discount_percent / 100))
        total = round(total, 2)
        result.append(member_lst[i])
        result.append(total)
    return result

##############################################
def report_attendance(member_lst1, member_lst2):
##############################################
    result = []
    for i in range(0, len(member_lst1), 2):
        member = member_lst1[i]
        total = member_lst1[i + 1]
        for j in range(0, len(member_lst2), 2):
            if member == member_lst2[j]:
                total = total + member_lst2[j + 1]
        result.append(member)
        result.append(total)

    for j in range(0, len(member_lst2), 2):
        member = member_lst2[j]
        found = False
        for i in range(0, len(member_lst1), 2):
            if member == member_lst1[i]:
                found = True
        if found == False:
            result.append(member)
            result.append(member_lst2[j + 1])

    return result
