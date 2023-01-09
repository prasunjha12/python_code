def getMatch(birthdays):
    
    if len(birthdays) == len(set(birthdays)):
        return None  
 
    
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA  