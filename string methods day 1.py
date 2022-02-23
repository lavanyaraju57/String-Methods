"""strings:
 strings is immutable, modificatons cannot be made."""

# print(dir(str))

'''CAPITALIZE'''

# name='hEllo PyThon'
# print(name.capitalize())

# name="hElloPython"
# print(name.capitalize())

'''CASEFOLD'''

# name="hEllo pyThon"
# print(name.casefold())
# print(name.lower())

'''CENTER'''

# name="hello pythony"
# print(name.center())
# print(name.center(50,'*'))
# print(name.center(100))

'''ENCODE'''

# name="hello python"
# n=name.encode()
# print(n)


'''isupper'''

# name="hEllo pyThon"
# print(name.isupper())

# b="CHOCOLATE"
# print(b.isupper())

'''islower'''

# m='world t20'
# print(m.islower())

'''title'''

# t='hEllo pyThon'
# print(t.title())

'''istitle'''

# c='Hello Python'
# print(c.istitle())

'''ENDSWITH'''

# n='hEllo pyThon'
# print(n.endswith())
# print(n.endswith(''))
# print(n.endswith(' '))
# print(n.endswith('n'))

'''STARTSWITH'''

# n='hEllo pyThon'
# print(n.startswith())
# print(n.startswith(''))
# print(n.startswith(' '))
# print(n.startswith('h'))

# m=" hello python"
# print(m.startswith(''))
# print(m.startswith(' '))
# print(m.startswith('h'))

'''isspace'''

# v=''
# g='   '
# print(v.isspace())
# print(g.isspace())

'''index'''

# q="hello pyotholno"
# print(q.index('l'))
# print(q.index("p"))
# print(q.index('l',4))
# print(q.index('o',5))
# print(q.index('1'))

'''rindex'''

# r="hello python programming"
# # print(r.index('b'))#value error
# print(r.rindex('n'))
# # print(len(r))
# print(r.rindex('g'))

