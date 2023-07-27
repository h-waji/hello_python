print('hello')
print("hello")
print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don\'t know\"")

print('hello.\nHow are you?')
print(r'C:\nendoroid\nendoroid')

print("##########")
print("""\
Miku
Rin
Len\
""")
print("##########")

print('Hi.' * 3 + 'Miku.')

print('Vo' + 'caloid')
prefix = 'Vo'
print(prefix + 'caloid')

s = ('aaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbb')
print(s)

word = 'vocaloid'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print(word[:2])
print(word[2:])
# word[0] = 'b'    Error
word = 'b' + word[1:]
print(word)

n = len(word)
print(n)

s = 'My name is Miku. Hi Miku.'
print(s)
is_start = s.startswith('My')
print(is_start)

print(s.find('Miku'))
print(s.rfind('Miku'))
print(s.count('Miku'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Miku', 'Obama'))
