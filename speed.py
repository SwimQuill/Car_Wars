speed = {'zero': 0, 'five': 5, 'ten': 10, 'fifteen': 15, 'twenty': 20, 'twenty-five': 25, 'thirty': 30,
         'thirty-five': 35, 'forty': 40, 'forty-five': 45, 'fifty': 50}


def foo(d):
    d['1'] = 'ONE'


print speed['zero']  # prints 'one' original value
foo(speed)
print speed['1']  # prints 'ONE' ie, modification reflects in original value
