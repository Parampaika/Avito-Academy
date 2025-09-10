import re
from english_stopwords import regexps_to_change

with open('./hamlet.txt') as f:
    hamlet = f.read()

for (regexp, to_change) in regexps_to_change:
    print(regexp)
    hamlet = re.sub(
        regexp, to_change, hamlet, flags=re.IGNORECASE
    )

with open('./hamlet_no_stopwords.txt', 'w') as f:
    f.write(hamlet.strip())
