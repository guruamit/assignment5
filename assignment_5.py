
class py_solution:
   def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x,-n)
        num = self.pow(x,n//2)
        if n%2 ==0:
            return num*num
        return num*num*x

print(py_solution().pow(10, 2))
