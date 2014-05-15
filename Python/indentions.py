def square_eggs(x):
    return x**2

square_spam = lambda x: x**2

y = [1,2,3,4,5]
spam  = []
eggs = []
for i in y:
    spam.append(square_spam(i))
    eggs.append(square_eggs(i))
    print i,i**2

print "spam == eggs?", spam==eggs
