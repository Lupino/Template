#!/usr/bin/python
# -*- coding: UTF-8 -*-

def toUni(line,dec):
	line=line.decode(dec)
	# \BOOKMARK [2][-]{subsection.3.1}{发现英语的重要性}{section.3}
	idx = line.find("}{")
	start = line[:idx+2]
	line = line[idx+2:]
	idx = line.find("}{")
	end = line[idx:]
	uniCN = line[:idx]
	#line=line.split('{')
	code=r'\376\377'
	for i in uniCN:
		u=ord(i)
		lu=u%256
		hu=(u>>8)%256
		code+=r'\%03o\%03o'%(hu,lu)
	return start + code + end

def main(infile,outfile,dec='UTF8'):
	with open(infile,'r') as f:
		for line in f:
			line=toUni(line,dec)
			with open(outfile,'a') as of:
				of.write(line)
if __name__=="__main__":
	import sys,os
	argc=len(sys.argv)
	if argc==1:
		print"Usage:{0} <infile>[ <decode>[ <outfile>]]".format(sys.argv[0])
		exit(-1)
	if not sys.argv[1].endswith('.out'):
		sys.argv[1]+='.out'
	if argc<4:
		outfile=sys.argv[1]
		infile=outfile+'.bak'
		os.system('mv {0} {1}'.format(outfile,infile))
		dec='UTF8'
		if argc==3:
			dec=sys.argv[2]
		main(infile,outfile,dec)
		exit()
	main(sys.argv[1],sys.argv[3],sys.argv[2])
