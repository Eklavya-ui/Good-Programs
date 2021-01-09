class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sum = 0
        if num1[0] == '-' and num2[0] == '-':
            num1 = num1[1:]
            num2 = num2[1:]
            for i in range(len(num2)-1,-1,-1):
                for j in range(len(num1)-1,-1,-1): 
                    sum += ((ord(num2[i]) - 48)*10**(len(num2)-(i+1)))*((ord(num1[j]) - 48)*10**(len(num1)-(j+1)))
            return str(sum)
        elif num1[0].isdigit() and num2[0].isdigit():
            for i in range(len(num2)-1,-1,-1):
                for j in range(len(num1)-1,-1,-1): 
                    sum += ((ord(num2[i]) - 48)*10**(len(num2)-(i+1)))*((ord(num1[j]) - 48)*10**(len(num1)-(j+1)))
            return str(sum)
        elif num1[0] == '-':
            num1 = num1[1:]
            for i in range(len(num2)-1,-1,-1):
                for j in range(len(num1)-1,-1,-1): 
                    sum += ((ord(num2[i]) - 48)*10**(len(num2)-(i+1)))*((ord(num1[j]) - 48)*10**(len(num1)-(j+1)))
            return str(-1*sum)
            
        else:
            num2 = num2[1:]
            for i in range(len(num2)-1,-1,-1):
                for j in range(len(num1)-1,-1,-1): 
                    sum += ((ord(num2[i]) - 48)*10**(len(num2)-(i+1)))*((ord(num1[j]) - 48)*10**(len(num1)-(j+1)))
            return str(-1*sum)
