'''
[+]Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.

[+]Examples
"1999" --> "20th"
"2011" --> "21st"
"2154" --> "22nd"
"2259" --> "23rd"
"1124" --> "12th"
"2000" --> "20th"
'''

#solution:
def what_century(year):
    if int(year) % 100 == 0:
        century = int(year)//100
    else:
        century = int((int(year) // 100)) +1
    if century in range(10,20):
        return str(century) + "th"
    else:
        if str(century)[len(str(century))-1] == "1":
            return str(century) + "st"
        elif str(century)[len(str(century))-1] == "2":
            return str(century) + "nd"
        elif str(century)[len(str(century))-1] == "3":
            return str(century) + "rd"
        else:
            return str(century) + "th"
