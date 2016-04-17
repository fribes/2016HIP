
dd if=dump.pdf of=header.bin bs=1 count=$((0x..))

gdb ./header.bin

info file 
br *<entry point>
layout asm
run
stepi

Found hardcoded password: Fkop4!opLm9

$ java -jar stegsolve.jar 
$ gocr -i solved.bmp -o pass.txt



http://guidetodatamining.com/ngramAnalyzer/analyze.php
https://www3.nd.edu/~busiforc/handouts/cryptography/cryptography%20hints.html
http://www.cryptograms.org/letter-frequencies.php#Quadrigrams
http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/

bruteforce
https://crackstation.net/buy-crackstation-wordlist-password-cracking-dictionary.htm
