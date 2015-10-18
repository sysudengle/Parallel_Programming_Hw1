import os
import sys

for i in xrange(int(sys.argv[2])):
	os.system('./client localhost:%s &' % (sys.argv[1]))


while True:
	word = raw_inut('press z for ending\n')
	if word == 'z':
		os.system("kill `pidof ./client`")
		break
