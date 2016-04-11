
Extracted string ixeas://yddotyprujw.nzm/udue/nsaco2016/ef7118o5-p1au-49g0-84f7-3850h4n21210.miex

from original image.


No success with caeser cipher... tried Vignere online:
http://planetcalc.com/2468/

and found key BELLARD 

thanks to plain text supposed to start with https://hackinparis ...

Result URL is:
https://hackinparis.com/data/chall2016/db7118d5-e1ad-49d0-84e7-3850d4c21210.binu

last character is junk

The file obtained has BGP as magic number : it is a BGP image

a lib to decode it is available there: http://bellard.org/bpg/

it doesn't compile fully, but the decoder is available

libbpg-0.9.6/bpgdec  flag.bpg > flag.png


extract from original image with stegsolve:
blue LSB by row  : bcc0e8c4c8fad03e6840
green LSB by row : 9f0f1d09589918998f00
red LSB by row   : b3212141a971b1b1e3e0
