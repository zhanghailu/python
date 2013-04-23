#!/user/bin/env python
#-*- conding: utf-8 -*-

import sys
import datetime

#now = datetime.datetime.now()
#Date = now.strftime('%Y-%m-%d %H:%M:%S')
#print Date

change_d = '2013-04-26 00:00:00'
init_d = datetime.datetime.strptime(change_d,'%Y-%m-%d %H:%M:%S')
init_version = 85






def count_Along(open_day_str):
	#open_day = datetime.datetime.strptime(open_day_str,'%Y-%m-%d %H:%M:%S')
	open_day = datetime.datetime.strptime(open_day_str,'%Y-%m-%d')
	Along = open_day - init_d
	return Along




def select_version(Days):
	if Days > 0:
		print 'After now version,%d days' %(Days)
		add_ver = Days / 7
		version = init_version + add_ver
		return version
	else:
		Days = - Days
		print 'Before now version,%d days' %(Days)
		reduce_ver = Days / 7
		version = init_version - reduce_ver
		return version


if __name__ == '__main__':
	open_day_str = '2013-04-19'
	Along = count_Along(open_day_str)
	version = select_version(Along.days)
	print "v%d" %(version)