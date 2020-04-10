import owotrans
import re

with open('Localizable.strings', encoding='utf-16') as f:
    mytext = f.readlines()

def do_owo(line):
    separator = '\" = \"'
    if re.search(separator, line) != None:
        parts = line.split(separator)
        assert len(parts) == 2, 'Invalid line found: %s' % line
        parts[1] = owotrans.owo(parts[1])
        owoized_line = separator.join(parts)
        return owoized_line
    else:
        return line

new_text = [do_owo(line) for line in mytext]
new_text_str = '\n'.join(new_text)

with open('Localizable.strings.new', 'w', encoding='utf-16') as f:
    f.write(new_text_str)

