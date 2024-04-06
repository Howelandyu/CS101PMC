# import re
# pattern = re.compile(r'go')
# match = pattern.match('go to there boy!')
# if match:
#     print(match.group( ))

# import re
# pattern = re.compile(r'there')
# match = pattern.search('go to there boy!')
# if match:
#     print(match.group( ))
# match = re.search(r'(\w+) (\w+)(?P<sign>.*)', 'go to get some points')
#
#
# print("m.string:", match.string)
# print("m.re:", match.re)
# print("m.pos:", match.pos)
# print("m.endpos:", match.endpos)
# print("m.lastindex:", match.lastindex)
# print("m.lastgroup:", match.lastgroup)
#
# print("m.group(3,4):", match.group(1, 2))
# print("m.groups():", match.groups())
# print("m.groupdict():", match.groupdict())
# print("m.start(1):", match.start(1))
# print("m.end(2):", match.end(2))
# print("m.span(2):", match.span(2))
# print(r"m.expand(r'\2 \1\3'):", match.expand(r'\2 \3\1' ))

# import re
#
# p = re.compile(r'(\w+) (\w+)')
# s = 'i say, hello world!'
#
# print(p.sub(r'\2 \1', s))
# def func(m):
#     return m.group(1).title() + ' ' + m.group(2).title()
# print(p.sub(func, s))






import re
pattern = re.compile(r'there')
match = pattern.search('go to there, are boys!')
def mat(match):
   return (match.group( ))
p = re.compile(r'(\w+) (\w+)')
file='he who is a   boy.'
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print(match.group()+'\t'+p.sub(r'\2 \1', file))

p = re.compile(r'\d+')
for numb in p.finditer('one1two2three3four4'):
    print (numb.group(),)

