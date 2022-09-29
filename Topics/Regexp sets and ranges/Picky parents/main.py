import re


print('Suitable!' if re.match('[B-N][aeiouy].*', input()) else '')