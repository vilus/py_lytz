#!/bin/env python

import sys


class General(Exception): pass

class Spec1(General): pass

class Spec2(General): pass

class Spec3(General):
	# param for check raise only as instance
	def __init__(self, request):
		# for attribute self.args
		Exception.__init__(self, request)


if __name__ == '__main__':
	exc_list = [
		Exception,
		General(1, '2'),
		Spec1,
		Spec2,
		Spec3(3),
		KeyboardInterrupt,
		SystemExit,
		GeneratorExit,
	]
	for exc in exc_list:
		try:
			raise exc
		except Spec1:
			print 'Spec1'
		except Spec2:
			print 'Spec2'
		except Spec3 as e:
			print 'Spec3, args %s' % str(e.args)
		except General as e:
			# attr args from BaseException
			print 'General, args %s' % str(e.args)
		except Exception:
			print 'Exception: %s' % sys.exc_info()[0]
		except:
			print sys.exc_info()[0]
		else:
			print '!!!!! Should not reached'
		finally:
			print '------ Always execute, end \n'
