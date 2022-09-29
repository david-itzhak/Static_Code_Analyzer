import re


sentence = 'Do I like cats? Yes!!'
template = 'Do I like cats\\? Yes!!'
tem = re.match(template, sentence)

template = '¯\\t_'
print(re.match(template, '¯\_(ツ)_/¯'))  # no match
print(re.match(template, '¯\t_'))  # match
print('¯\t_')