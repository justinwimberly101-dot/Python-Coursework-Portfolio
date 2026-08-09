'''
Topic: Exception handling -- nested try/except blocks for dictionary lookups,
type-safe division, and timestamp validation
'''

##############################################
def get_info(d, info1, info2):
##############################################

    try:
        # Access nested dictionary values
        return d[info1][info2]
    except KeyError:
        # Handle missing keys
        return "No information is available in the database"

##############################################
def merge_lists(l1, l2):
##############################################

    result = []

    try:
        for i in range(len(l1)):
            try:
                # Attempt to concatenate corresponding elements
                combined = l1[i] + " " + l2[i]
                result.append(combined)
            except TypeError:
                # Skip invalid pairs (non-string concatenation)
                continue
    except IndexError:
        # Stop if one list is shorter
        return result

    return result

##############################################
def find_division(a, b):
##############################################
    try:
        a = int(a)
        b = int(b)
    except TypeError:
        return "Inputs must be numbers only"
    except ValueError:
        return "Invalid input"

    try:
        if a % b != 0:
            raise IndexError
        return a // b

    except ZeroDivisionError:
        return "Invalid input"
    except IndexError:
        return "a is not divisible by b"
##############################################
def check_timestamp(time):
##############################################

    try:
        # Ensure input is a string
        if not isinstance(time, str):
            raise TypeError

        try:
            # Split time into components
            parts = time.split(":")

            # Check correct format (3 parts)
            if len(parts) != 3:
                raise ValueError

            try:
                # Convert parts to integers
                h = int(parts[0])
                m = int(parts[1])
                s = int(parts[2])
            except ValueError:
                # Handle non-integer values
                return "Values must be integers"

            # Validate hour range
            if h < 0 or h > 23:
                return "Hour is out of range"

            # Validate minute range
            if m < 0 or m > 59:
                return "Minute is out of range"

            # Validate second range
            if s < 0 or s > 59:
                return "Second is out of range"

            # All checks passed
            return "The format is okay"

        except ValueError:
            # Handle incorrect format
            return "Incorrect format"

    except TypeError:
        # Handle non-string input
        return "Input must be a string value"
