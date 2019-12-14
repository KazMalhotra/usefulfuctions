import re
#camelCase
def camel(s):
  s = re.sub(r"(_|-)+", " ", s).title().replace(" ", "")
  return s[0].lower() + s[1:]
