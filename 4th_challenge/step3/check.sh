#!/bin/bash

#known="HIP{f3a306095ecc4dad3d0056ad7b0c135afd89e3127e2"
known="HIP{"
while true
do
	len=${#known}
	found="no"
	for j in `cat chars.txt`
	do
		for i in $j
		do
			echo $known$i | strace ./chall.bin 2>&1 | grep -A$((1+$len)) read\(0 | head -$((2+$len)) | tail -1 | grep -v "write(1, \"A\", 1A)" >/dev/null
			if [ $? == 0 ]
			then
				known=$known$i
				echo  $known
				found="yes"
				break	
			fi
		done
		if [ $found = "yes" ]
		then
			break
		fi
	done
done
