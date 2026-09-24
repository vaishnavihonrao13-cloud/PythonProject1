class code:
    def __init__(self,n):
        self.n=n
    def __add__(self, other):
       return code(self.n+other.n)
    def __sub__(self,other):
        return code(self.n-other.n)
    def __mul__(self,other):
        return code(self.n*other.n)
    def __truediv__(self,other):
        return code(self.n/other.n)

c1=code(10)
c2=code(11)
c3=code(0)
c3=c1+c2
c4=c1-c2
c5=c1*c2
c6=c1/c2

print(c3.n)
print(c4.n)
print(c5.n)
print(c6.n)
#class time:
#   def __init__(self,hr,min):
#       self.hr=hr
#       self.min=min
#   def __add__(self,other):
#       t=time(0,0)
#       t.hr=self.hr+other.hr
#       t.min=self.min+other.min
#        if t.min>=60:
#            t.min=t.min-60
 #           t.hr+1
  #      return t
   # def __str__(self):
    #    return f"{self.hr}:{self.min}"
#t1=time(3,55)
#t2=time(12,22)
#t3=t1+t2
#print(t1)
#print(t2)
#print(t3)