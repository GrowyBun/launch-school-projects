def century(year):
    century = year // 100 + 1
    if year % 100 == 0:
        century -= 1
        
    last_two = century % 100
    last = century % 10
    if century > 10:
        match last_two:
            case 11|12|13:
                return str(century) + 'th'
            
    match last:
        case 1:
            return str(century) + 'st'
        case 2:
            return str(century) + 'nd'
        case 3:
            return str(century) + 'rd'
        case _:
            return str(century) + 'th'
    return century

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
