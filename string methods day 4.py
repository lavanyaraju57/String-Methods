'''SWAPCASE'''

# p="pythON proGRAMming"
# print(p.swapcase())

# a=4 ; b=66
# print(a)
# del a,b
# print(a,b)

'''FORMAT'''

# print("Buy this for Rs.{d} or for Rs.{ed}".format(d=11,ed=50))

'''EXPANDTABS'''

# a='R\tS\tV'
# print(a.expandtabs(0))
# print(a.expandtabs(1))
# print(a.expandtabs(2))
# print(a.expandtabs(3))
# print(a.expandtabs(4))
# print(a.expandtabs(5))
# print(a.expandtabs(6))
# print(a.expandtabs(7))
# print(a.expandtabs(8))
# print(a.expandtabs())
# print(a.expandtabs(-1))

'''JOIN'''

# v='hello','python','core'
# n='python'
# print('-'.join(v))
# print('*'.join(n))
# print('*'.join("Hello"))

'''MAKETRANS & TRANSLATE'''

# r="helly hello"
# a=r.maketrans('l','u')
# print(a,type(a))
# print(r.translate(a))

'''SPLITLINES'''

# a="hello\nCore python\nprogramming"
# g=a.splitlines()
# # print(g)
# # print(g,type(g))
# print(g[0])
# print(g[1])
# print(g[2])

# k="Hello!\nWelcome to \nJoshInnovations"
# print(k.splitlines())
# print(k.splitlines(True))
# print(k.splitlines(False))

'''SPLIT'''

# h="HelloWelcome to JoshInnovations"
# w=h.split()
# print(w,type(w))
# print(h.split(" "))
# print(h.split(""))

# v="Hello Welcome to JoshInnovations"
# print(v.split())

# b="Hello:Welcome: To:Josh:Innovations"
# print(b.split(":"))

# n="Python#C#Java#R#Dart"
# print(n.split("#"))
# print(n.split("#",0))
# print(n.split("#",1))
# print(n.split("#",2))
# print(n.split("#",3))
# print(n.split("#",4))
# print(n.split("#",5))

'''ZFILL'''

# f="hello"
# print(f.zfill(10))
# print(f.zfill(20))

'''PARTITION'''

# j="hey! how are you doing?"
# print(j.partition("are"))

# t="hey! how are you doing?"
# r=t.partition("you")
# print(r)
# print(r[2])

'''rpartition'''

# m="We are Learing Python Programming , Python is badsic need"
# print(m.partition("Python"))
# print(m.rpartition("Python"))

'''ljust'''

# c="Python"
# print(c.ljust(8,'p'))

# x="Python"
# print(x.ljust(10,'R'))

'''rjust'''

# s="Python"
# print(s.rjust(10),'R')
# print(s.rjust(10,'R'))

# z="python"
# print(z.rjust(8),"programming basics")

'''isidentifier'''

# a='_hello'
# print(a.isidentifier())
# b='hello'
# print(b.isidentifier())
# c='Hello'
# print(c.isidentifier())
# d='_'
# print(d.isidentifier())
# e='_32'
# print(e.isidentifier())
# f='1abc'
# print(f.isidentifier())
# g='.1abc'
# print(g.isidentifier())
# h='1a bc'
# print(h.isidentifier())





