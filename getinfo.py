#!/usr/bin/env python
#-*- conding:utf-8 -*-

import re




def getzoneinfo(plant,zone,confile='/md/publish/serverInfo.cfg',*params):
	Params_dict = {'plant':0,'plantid':1,'zone':2,'zoneid':3,'servername':4,'opentime':1,'port':12}
	ConfigFile = open(confile,'r')
	for Info in ConfigFile.readlines():
		expect = re.match(r'^#',Info)
		split = re.split('\s+',Info)
		if expect:
			pass
		elif split[0] == plant and split[2] == zone:
			#return Info
			#print Info
			'''if params is null,return all info line'''
			for parm in params:
				''' time split shouled optimize'''
				split_id = Params_dict[parm]
				if parm == 'opentime':
					split = re.split('\"',Info)
				else:
					pass
				return split[split_id]
				#print "%s" %(split[split_id]),
	ConfigFile.close()


'''test'''

#getzoneinfo('360','s1','/Users/hyperion/shell/serverInfo.cfg','zone','servername','port','opentime')

		




