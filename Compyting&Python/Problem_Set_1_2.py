s = 'azcbobobegghakl'

import re
count = len(re.findall('(?=bob)', s))
print('Number of times bob occurs is: ' + str(count))