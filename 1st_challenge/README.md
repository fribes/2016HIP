
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


From Lionel:


cd /tmp/
wget 'http://bellard.org/bpg/libbpg-0.9.6.tar.gz' && tar -xvzf libbpg-0.9.6.tar.gz 
cd libbpg-0.9.6/
wget 'ftp://ftp.simplesystems.org/pub/png/src/libpng15/libpng-1.5.26.tar.gz' && tar -xvzf libpng-1.5.26.tar.gz 
cd libpng-1.5.26/
./configure --prefix=`pwd`/compiled
make all install
cd ..
patch << EOF
--- bpgdec.c 2016-03-22 08:57:11.934472933 +0100
+++ bpgdec.c 2016-03-22 08:58:41.834473723 +0100
@@ -249,6 +249,7 @@
                 tag_name = extension_tag_str[0];
             printf("  tag=%d (%s) length=%d\n",
                    md->tag, tag_name, md->buf_len);
+            for (buf_len=0; buf_len<md->buf_len; buf_len++) printf("0x%08x: %02x\n", buf_len, md->buf[buf_len]);
         }
         bpg_decoder_free_extension_data(first_md);
     }
EOF
sed -i -e 's@^CFLAGS+=-I.*@& -I./libpng-1.5.26/compiled/include@' -e 's@^LDFLAGS=-g.*@& -L./libpng-1.5.26/compiled/lib@' Makefile
make
LD_LIBRARY_PATH=./libpng-1.5.26/compiled/lib/ ./bpgdec -i ./db7118d5-e1ad-49d0-84e7-3850d4c21210.bin|sed -n -e 's/^0x[^:]*:[[:blank:]]*\([^[:blank:]]*\)[[:blank:]]*$/0x\1,/p'|xargs echo|sed -e '1iimport struct,sys' -e '1s/^.*$/A=[&]/' -e '1asys.stdout.write(struct.pack("B"*len(A), *A))'|python > ./payload.pyc
