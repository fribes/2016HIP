CIPHER="CGEJDHAGBIBJAFEGBGBJAFEHEJDHAJAIEJBIEFBJAH\
EHDHAGAJEGCGCGDIAJAJAIEGBGBGEIBFDICGBIEIDF\
AFDIBFAFEFEHAJCIDIAJAJBJAGDIEHAFDJEHBGBGEF\
DIBGDFEIEJEGAFEJCGEJBIBIDICGAFBGEIEJDFDIDH\
AFEFDICFEHDFAIEHBGDIDGEIAGEHAHEHDHAGEIEJEG\
AFEFDIBIEHAGEFAFDFBJAJAJDJEJBIBFBFEJDHAFAI\
EJBIAGDIAFEIEJEGAJEFEJEGBGBFDJBIEHAFDIEHAF\
EHDHBGEJDJDIBICGBJAJDIBGDIAFAFDIBIAJAFEFDI\
DFBJAJAJDJEJBIBFEHAJAFDGAFBJDHAJDIEIAJBJDI\
EHEJCIAJDFEFDIAJBG"

EN_MAP= { "DI":"E",
"AF":"T",
"AJ":"A",
"EJ":"O",
"EH":"N",
"BI":"I",
"BG":"S",
"EF":"R",
"BJ":"H",
"DH":"D",
"EI":"L",
"DF":"U",
"EG":"C",
"CG":"M",
"AG":"F",
"BF":"Y",
"DJ":"W",
"AI":"G",
}

FR_MAP= { "DI":"E",
"AF":"A",
"AJ":"S",
"EJ":"T",
"EH":"I",
"BI":"R",
"BG":"N",
"EF":"U",
"BJ":"L",
"DH":"O",
"EI":"D",
"DF":"M",
"EG":"C",
"CG":"P",
"AG":"V",
"BF":"H",
"DJ":"G",
"AI":"F",
}


MAN_MAP= { "AF":"T",
"EF":"H",
"DI":"E",
"DF":"P",
"BJ":"A",
"AJ":"S",
"DJ":"W",
"EJ":"O",
"BI":"R",
"BF":"D",
"CI":"M",
"AG":"G",
"EH":"I",
"CG":"C",
"DH":"N",
"EG":"U",
"DH":"N",
"BG":"L",
"AI":"F",
"AH":"V",
"EI":"Y",
"CF":"Z",
"DG":"B"}

ENG_FREQS={
"cornell.edu" :"ETAOINSRHDLUCMFYWGPBVKXQJZ",
"stefan.trost":"ETAONISHRLDUCMWYFGPBVKJXQZ",
"lewand":      "ETAOINSHRDLCUMWFGYPBVKJXQZ"
}

def trans(map=EN_MAP, cipher=CIPHER):
	""" Do transposition """
	i=0
	for j in range(len(cipher)/2):
		try:
			print(map[cipher[i]+cipher[i+1]]),
		except KeyError:
			print('['+cipher[i:i+2]+']'),
		i +=2

trans(map=MAN_MAP)
