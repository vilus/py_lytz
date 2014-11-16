#!/bin/env python

def _hidden_func():
	print(' From hidden func')

def usual_func():
	print(' From usual func')

some_str = 'Just string, not unicode'
print type(some_str)
