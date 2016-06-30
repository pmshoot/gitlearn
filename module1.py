# -----------------
# module1
# -----------------
def first():
	print('this is first function on module #1')

def second(s):
	print('it\'s a second module - {}'.format(s))

if __name__ == '__main__':
	first()
	second('yes')
