#!/bin/env python
# -*- coding: UTF-8 -*-


from modules import *

if '_hidden_func' in globals():
	print 'oO'
else:
	print 'ok'

if 'usual_func' in globals():
	print 'ok'
else:
	print 'oO'

str_lit = 'Some string'
print type(str_lit)
