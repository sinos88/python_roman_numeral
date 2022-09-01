'''
Takes a positive integer and returns a string containing
the roman numeral
'''


def solution(n):
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    output = ''
    position = 0
    # Countdown n for n >= list take away that number
    while n != 0:
        while position != 13:
            if n >= number[position]:
#               print(n)
                n -= number[position]
#                print(n)
                output += roman[position]
#               print(output)
                break
            position += 1
#            print(position)
    return output


final = int(input('number to roman numeral: '))
print(solution(final))

'''
The bottom shows various other solutions 
and also a failed solution that didn't 
work for me. 
'''
'''
FAILED SOLUTION
def solution(n):
    m = 'XYZ'
    roman_list = ['I', 'X', 'C', 'M', 'V', 'L', 'D']
    roman = ''
    # iterate and minus n until 0
    while n != 0:
        # Check if it starts at 9, 5. 4

        print(str(n))
        nstr = str(n)
        print(nstr[0])
        if (nstr[0]) == '9':
            print(len(nstr)-1)
            roman += roman_list[len(nstr)] + roman_list[len(nstr)-1]
            print(roman)
            n = n - (9 * (10 ** len(nstr)))

        if (nstr[0]) == '5':
            roman += roman_list[len(nstr)+3]
            print(roman)


        
        #len(str(n))

    # if list[1] == 9
    # if list[1] == 8
    return m


final = int(input('number to roman numeral: '))
print(solution(final))

'''
'''
units = " I II III IV V VI VII VIII IX".split(" ")
tens = " X XX XXX XL L LX LXX LXXX XC".split(" ")
hundreds = " C CC CCC CD D DC DCC DCCC CM".split(" ")
thousands = " M MM MMM".split(" ")

def solution(n):
    return thousands[n//1000] + hundreds[n%1000//100] + tens[n%100//10] + units[n%10]
'''
'''
def solution(n):
    dic = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
    roman = ''
    for a in reversed(sorted(dic.keys())):
        while (a <= n):
            n = n - a;
            roman = roman + dic[a];
    return roman
'''