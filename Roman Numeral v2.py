'''
A class with two objects, to convert Roman Numeral to number and vice versa
This is Version 2.0, added function to convert from number to a roman numeral
'''

class RomanNumerals:
    
    def to_roman(val):
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        output = ''
        position = 0
        # Countdown n for n >= list take away that number
        while val != 0:
            while position != 13:
                if val >= number[position]:
#                   print(n)
                    val -= number[position]
#                   print(n)
                    output += roman[position]
#                   print(output)
                    break
                position += 1
#               print(position)
        return output


    def from_roman(roman_num):
        #roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        #number = [1000, 500, 100, 50, 10, 5, 1]        
        roman_dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        total = 0
        prev = 0
        
        while roman_num:
            for rn in roman_dict.keys():
                romannum = roman_num[-1]
                if rn == roman_num[-1]:
                    romanvalue = roman_dict.get(rn)
                    if prev > romanvalue:
                        total -= romanvalue
                        #print(f'---minus{total} -----')
                    else:
                        total += romanvalue
                        #print(f'---plus{total} -----')
            prev = romanvalue
            roman_num = roman_num[:-1]
        return total

print(RomanNumerals.to_roman(2454) + '\n')
print(RomanNumerals.from_roman('MMCXIV'))



# Found a more elegant way to code this....  

'''
ROMANS = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'C': 100,
    'XC': 90,
    'L': 50,
    'X': 10,
    'V': 5,
    'IV': 4,
    'I': 1,
}
    
class RomanNumerals:
    
    def to_roman(n):
        s = ''
        for key, value in ROMANS.items():
            while n % value != n:
                n = n - value
                s += key
        return s
    
    def from_roman(r):
        s = 0
        for key, value in ROMANS.items():
            while r.startswith(key):
                r = r[len(key):]
                s += value
        return s
        '''
