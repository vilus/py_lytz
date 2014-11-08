#!/bin/env python


class TraceBlock:
	def msg(self, val):
		print 'message: %s' % val

	def __enter__(self):
		print '__enter__'
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		if exc_type:
			print 'raised exc %s' % exc_type
			return False
		print 'exited normally'


if __name__ == '__main__':
	with TraceBlock() as tb:
		tb.msg('Hi norm')
		print 'without raise'

	with TraceBlock() as tb:
		tb.msg('Hi exc')
		raise TypeError
                print 'not reached'



