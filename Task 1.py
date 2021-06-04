s = input('Please enter the text: ')
l = {i:s.count(i) for i in s}
sort = sorted(list(l.values()))
print('MYSTRING') if (sort[0]==sort[-1] or (sort[0]==sort[-2] and sort[0]==sort[-1]-1)) else print('Not MYSTRING')

# In normal syntax:
#if sort[0]==sort[-1] or sort[0]==sort[-2] and sort[0]==sort[-1]-1:
#    print('MYSTRING')
#else:
#    print('Not MYSTRING')