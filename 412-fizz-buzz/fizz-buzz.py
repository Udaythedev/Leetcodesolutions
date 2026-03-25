class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        FBL= []
        for i in range(1,n+1):
            if i%3==0 and i%5==0 :
                FBL.append("FizzBuzz")
            elif i%3==0 :
                FBL.append("Fizz")
            elif i%5==0 :
                FBL.append("Buzz")
            else:
                FBL.append(str(i))
        return FBL