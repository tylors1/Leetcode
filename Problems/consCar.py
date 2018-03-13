def cons(a, b):
    return lambda f : f(a, b)

def car(f):
	return f(lambda a, b: a)

def cdr(f):
	return f(lambda a, b: b)



a = 5
b = 6

print car(cons(a,b))

# https://stackoverflow.com/questions/21769348/use-of-lambda-for-cons-car-cdr-definition-in-sicp
# https://stackoverflow.com/questions/8073882/lisp-cons-in-python