s = "MCMXCIV"
output = 1994

def romanToInt(self, s):

# use dictionary to keep track of letters and their values   
    lettersDict = { 'M' : 1000,
                    'D' : 500,
                    'C' : 100,
                    'L' : 50,
                    'X' : 10,
                    'V' : 5,
                    'I' : 1
                    }

# get the value of last element
    total = lettersDict[s[len(s)-1]]

# iterate through the chars in string, skipping last char.
# When next number is smaller or equal to current number, 
# sum them. When next number is larger than current number, 
# sum them and minus twice of current number.
    for i in range(len(s)-1, 0, -1):
        current = lettersDict[s[i]]
        prev = lettersDict[s[i-1]]
        total += prev if prev >= current else -prev
    return total

print(romanToInt(0, s))