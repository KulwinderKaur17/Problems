class MathematicalTools:


    def __init__(self) -> None:
        pass

    def find_prime(self,num):
        prime=True
        for i in range(2,num):
            if num%i==0:
                prime = False
                break
        if prime==False:
            print('not a prime', num)
            pass
        else:
            print('prime number is:', num)


    def find_factors(self,num):
        factors=[]
        for i in range(2,num):
            if num%i==0:
                factors.append(i)
        return factors

    