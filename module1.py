# -----------------
# module1
# -----------------
def first():
	print('this is first function on module #1')

def second(s):
	print('it\'s a second module - {}'.format(s))

def third(sd):
	print('Hello everybody! - {}'.format(sd))

if __name__ == '__main__':
	first()
	second('yes')
	third('How are You?')
	
