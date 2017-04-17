""" Label functions: check each value and label with VALID/INVALID/NULL """

def check_three_digit(str):
    """ 
        Check values in column 7 and 9 (three digit) and label them with NULL/INVALID/VALID 
        
        NULL: value contains empty string or 'NULL'
        INVALID: length of the value is not 3 or the value is not numeric
        VALID: a three digit number
    """

    str = str.strip()
    if str == '' or str == 'NULL':
        return 'NULL'
    elif len(str) != 3:
        return 'INVALID'
    else:
        return ('VALID' if str.isdigit() else 'INVALID')

def check_indicator(str):
    """ 
        Check values in column 11 (indicator) and label them with NULL/INVALID/VALID

        NULL: value contains empty string or 'NULL'
        INVALID: the string is not one of "COMPLETED" and "ATTEMPTED" (case insensitive)
        VALID: one of "COMPLETED" and "ATTEMPTED"
    """

    str = str.strip()
    if str == '' or str == 'NULL':
        return 'NULL'
    
    str = str.upper() # Convert to upper case
    if str == 'COMPLETED' or str == 'ATTEMPTED':
        return 'VALID'
    else:
        return 'INVALID'

def check_offense_level(str):
    """ 
        Check values in column 12 (offense level) and label them with NULL/INVALID/VALID

        NULL: value contains empty string or 'NULL'
        INVALID: the string is not one of "felony", "misdemeanor", and "violation" (case insensitive)
        VALID: one of "felony", "misdemeanor", and "violation"
    """

    str = str.strip()
    if str == '' or str == 'NULL':
        return 'NULL'
    
    str = str.upper() # Convert to upper case
    if str == 'FELONY' or str == 'MISDEMEANOR' or str == 'VIOLATION':
        return 'VALID'
    else:
        return 'INVALID'

def checknull(str):
    return ('VALID' if str != '' else 'NULL')
