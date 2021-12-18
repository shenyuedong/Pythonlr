import re

r=r"[^a-z]*([y]o|[h']?ello|ok|hey|(good[ ])?(morn[gin']{0,3}|"\
  r"afternoon|even[gin']{0,3}))[\s,;:]{1,3}([a-z]{1,20})"

re_greeting=re.compile(r,flags=re.IGNORECASE)
print(re_greeting.match('Hello Rosa'))
print(re_greeting.match('Hello Rosa').groups())
print(re_greeting.match("Good Manning Rosa"))
print(re_greeting.match('Good evening Rosa Parks').groups())
print(re_greeting.match("Good Morn'n Rosa"))
print(re_greeting.match("yo Rosa"))


my_names=set(['rosa','rose','chatty','chatbot','bot','chatterbot'])
curt_names=set(['hal','you','u'])
greeter_name=''
match=re_greeting.match(input())
print(match.groups()[-1])
if match:
    at_name=match.groups()[-1]
    if at_name in curt_names:
        print("Good one.")
    elif at_name.lower() in my_names:
        print("Hi {}, How are you?".format(greeter_name))
