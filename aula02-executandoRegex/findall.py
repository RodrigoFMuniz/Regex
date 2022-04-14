import re

texto = 'Hello World Again he! hello hp'

regex_1 = re.compile(r'[a-z]')
# retorna somente o grupo de chars que começar com h
# retorna uma lista com quaisquer combinações que começem com h + 4 dados qq
regex_2 = re.compile(r'H....')
regex_3 = re.compile(r'.....')  # retorna vários grupos de 5 chars em uma lista
# retorna uma lista com quaisquer combinações que começem com h + um dado qq
regex_4 = re.compile(r'h.')

print(regex_1.findall(texto))
print(regex_2.findall(texto))
print(regex_3.findall(texto))
print(regex_4.findall(texto))
