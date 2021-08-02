#password generator by mr.love yadav

import random

uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase='abcdefghijklmnopqrstuvwxyz'
number='1234567890'
punctuation='!~@#$%^&*()_:;?><.,|]['

length=16

all=uppercase+lowercase+number+punctuation

generate="".join(random.sample(all,length))
print(generate)