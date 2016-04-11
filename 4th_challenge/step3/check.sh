#!/bin/bash

known="HIP"
len=${#known}

for i in \ \! \# \@ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v x y z \=  
do
	echo $known$i | strace ./chall.bin 2>&1 | grep -A$((1+$len)) read\(0 | head -$((2+$len)) | tail -1 | grep -v "write(1, \"A\", 1A)"
	if [ $? == 0 ]
	then
		echo Found !!! $i
	fi
done
