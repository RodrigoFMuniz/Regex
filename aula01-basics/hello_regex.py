import re

texto = 'hello world!'

new_regex = re.compile(r'h...o.w....')

print(new_regex.findall(texto))
