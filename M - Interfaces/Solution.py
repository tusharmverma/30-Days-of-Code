from abc import ABCMeta, abstractmethod


class AdvancedArithmetic(object, metaclass=ABCMeta):
    @abstractmethod
    def divisorSum(self, n):
        pass


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        result = 0
        for i in range(1,n+1):
            if n % i == 0:
                result += i
        
        return result


n = int(input())

myCalculator = Calculator()
total = myCalculator.divisorSum(n)
print("I implemented: " + str(AdvancedArithmetic))
print(total)
