A = [1, 2, 3, 5]
K = 3

#A = [1,2,3,5,7,13,17,23,31,41,47,53,61,67,73,79,83,97,103,107,109,131,149,151,163,167,173,179,191,211,223,227,229,239,241,251,263,271,293,313,317,331,347,349,353,359,367,389,397,401,431,433,439,443,449,457,461,463,479,487,491,509,521,569,571,577,587,601,619,641,647,659,683,691,701,709,719,727,733,739,743,751,757,761,773,787,797,811,821,823,827,839,853,857,863,929,937,941,947,953,967,991,1021,1031,1033,1051,1061,1087,1091,1093,1103,1117,1129,1151,1153,1187,1201,1217,1229,1237,1283,1289,1291,1297,1301,1303,1307,1319,1321,1327,1361,1373,1399,1423,1429,1439,1447,1451,1453,1459,1471,1481,1483,1487,1489,1493,1499,1543,1549,1553,1559,1579,1583,1597,1601,1607,1613,1621,1627,1637,1657,1663,1693,1697,1699,1747,1777,1787,1789,1801,1811,1831,1847,1867,1871,1879,1913,1931,1933,1949,1951,1973,1993,1997,2011,2017,2027,2029,2039,2063,2069,2081,2087,2089,2099,2111,2113,2129,2131,2137,2141,2143,2153,2161,2179,2213,2243,2269,2281,2287,2293,2297,2339,2351,2357,2371,2377,2389,2393,2417,2441,2447,2467,2477,2503,2531,2539,2549,2551,2557,2617,2633,2657,2659,2663,2687,2689,2693,2713,2731,2749,2767,2791,2803,2833,2837,2843,2851,2861,2879,2887,2903,2909,2939,2953,2969,2971,2999,3001,3041,3079,3083,3089,3121,3163,3169,3187,3203,3217,3221,3229,3253,3259,3299,3301,3307,3319,3329,3331,3343,3347,3361,3389,3413,3463,3467,3469,3499,3511,3517,3533,3541,3559,3571,3581,3583,3593,3607,3613,3617,3623,3631,3643,3677,3691,3697,3701,3733,3767,3833,3847,3851,3881,3907,3911,3919,3929,3931,3947,3989,4001,4003,4013,4019,4021,4049,4051,4057,4073,4079,4093,4099,4127,4133,4153,4157,4159,4177,4211,4217,4219,4241,4243,4253,4261,4271,4273,4297,4327,4337,4339,4363,4373,4391,4409,4447,4451,4457,4463,4481,4513,4523,4561,4567,4583,4591,4603,4621,4637,4643,4649,4663,4691,4721,4751,4787,4799,4801,4813,4817,4831,4861,4877,4909,4931,4937,4943,4957,4967,4969,4993,5003,5009,5021,5023,5051,5077,5101,5113,5119,5153,5167,5171,5179,5189,5231,5273,5279,5281,5303,5309,5323,5347,5387,5399,5407,5413,5417,5419,5431,5437,5441,5443,5449,5471,5477,5479,5483,5501,5503,5507,5519,5521,5527,5531,5557,5563,5569,5573,5591,5623,5639,5647,5651,5659,5669,5693,5741,5743,5749,5783,5801,5813,5827,5843,5849,5861,5867,5879,5903,5923,5927,5939,5953,5987,6011,6037,6047,6073,6079,6089,6091,6101,6113,6121,6131,6133,6143,6151,6173,6197,6199,6203,6211,6221,6229,6247,6257,6263,6269,6271,6287,6299,6301,6317,6329,6337,6343,6359,6367,6373,6389,6397,6421,6449,6451,6469,6473,6491,6529,6551,6553,6563,6577,6607,6619,6637,6659,6679,6689,6701,6709,6763,6779,6791,6793,6803,6829,6833,6841,6857,6863,6869,6871,6883,6917,6949,6959,6961,6971,6977,6983,6991,7001,7019,7027,7043,7069,7079,7109,7121,7159,7177,7211,7229,7237,7243,7247,7253,7283,7297,7307,7331,7333,7351,7369,7393,7411,7433,7451,7457,7459,7477,7481,7487,7517,7523,7537,7547,7561,7577,7583,7591,7603,7621,7649,7669,7691,7703,7717,7741,7753,7757,7759,7789,7823,7829,7841,7853,7867,7873,7883,7901,7919,7927,7933,7949,7951,7963,8009,8011,8017,8053,8081,8087,8089,8093,8111,8123,8179,8209,8231,8233,8237,8263,8269,8273,8287,8311,8317,8329,8363,8369,8377,8389,8419,8423,8443,8447,8461,8467,8521,8537,8543,8563,8581,8599,8609,8627,8629,8641,8647,8663,8669,8677,8689,8699,8731,8737,8741,8747,8753,8761,8803,8807,8839,8863,8867,8923,8963,8971,8999,9007,9011,9013,9029,9041,9043,9067,9133,9161,9181,9187,9199,9203,9209,9221,9239,9241,9257,9281,9293,9323,9341,9343,9349,9391,9419,9421,9431,9433,9437,9461,9463,9473,9479,9491,9497,9511,9533,9539,9547,9551,9587,9601,9623,9629,9631,9649,9689,9697,9719,9733,9739,9749,9769,9787,9791,9803,9811,9817,9857,9859,9883,9901,9907,9923,9931,9941,9967,9973,10007,10039,10061,10067,10069,10079,10091,10093,10099,10133,10141,10159,10163,10177,10193,10211,10253,10259,10271,10273,10289,10301,10313,10331,10333,10337,10343,10369,10391,10399,10427,10429,10433,10459,10499,10501,10529,10531,10559,10589,10597,10601,10607,10627,10639,10657,10687,10691,10709,10723,10729,10733,10753,10771,10781,10847,10853,10859,10883,10889,10891,10903,10939,10949,10957,10993,11003,11027,11047,11059,11069,11083,11117,11119,11131,11149,11159,11161,11171,11173,11177,11197,11213,11243,11261,11273,11279,11287,11311,11329,11351,11353,11369,11383,11393,11423,11437,11447,11483,11489,11497,11527,11549,11551,11587,11593,11617,11621,11633,11657,11677,11681,11699,11701,11717,11719,11731,11777,11779,11783,11789,11801,11813,11821,11827,11831,11833,11839,11867,11887,11897,11903,11909,11927,11939,11953,11971,11987,12011,12041,12043,12073,12097,12101,12109,12113,12149,12157,12197,12211,12251,12253,12269,12277,12289,12301,12343,12347,12379,12401,12409,12413,12421,12433,12437,12473,12479,12487,12491,12497,12503,12511,12527,12541,12547,12553,12569,12583,12589,12601,12611,12613,12619,12641,12647,12653,12659,12671,12721,12739,12743,12757,12763,12799,12823,12841,12889,12907,12923,12953,12959,12979,12983,13033,13037,13049,13063,13093,13127,13151,13159,13171,13183,13187,13217,13219,13229,13241,13249,13259,13291,13313,13327,13337,13339,13367,13381,13397,13411,13417,13421,13457,13463,13469,13477,13499,13513,13523,13537,13553,13567,13591,13627,13649,13679,13681,13687,13691,13693,13711,13721,13723,13757,13763,13781,13789,13799,13831,13841,13859,13873,13963,13967,13999,14009,14029,14033,14051,14057,14087,14143,14149,14153,14159,14177,14221,14243,14249,14293,14321,14327,14347,14401,14419,14423,14431,14437,14449,14461,14503,14533,14537,14543,14549,14551,14557,14563,14591,14593,14621,14629,14639,14653,14657,14683,14699,14717,14731,14741,14747,14753,14759,14767,14779,14797,14813,14821,14843,14869,14879,14891,14897,14923,14929,14947,14951,14969,14983,15013,15061,15073,15083,15101,15107,15121,15137,15139,15149,15161,15187,15193,15199,15227,15233,15263,15271,15277,15287,15289,15299,15313,15319,15329,15331,15349,15359,15361,15401,15413,15427,15439,15443,15451,15461,15467,15473,15511,15527,15541,15559,15581,15583,15601,15607,15619,15643,15679,15683,15727,15731,15733,15737,15749,15767,15773,15791,15797,15803,15809,15817,15823,15859,15881,15887,15889,15907,15923,15937,15959,15971,15991,16033,16057,16061,16067,16103,16111,16127,16141,16183,16189,16217,16229,16231,16253,16267,16301,16333,16363,16369,16381,16411,16427,16433,16451,16477,16481,16487,16493,16519,16529,16547,16553,16603,16607,16619,16631,16633,16651,16661,16693,16729,16763,16787,16811,16829,16831,16843,16871,16903,16921,16927,16931,16937,16943,16979,16981,16987,16993,17011,17021,17033,17041,17053,17077,17093,17099,17107,17123,17159,17167,17189,17191,17203,17231,17239,17257,17291,17317,17327,17333,17387,17393,17401,17417,17431,17443,17449,17467,17471,17489,17497,17509,17519,17551,17569,17579,17581,17599,17609,17657,17659,17669,17707,17713,17729,17737,17747,17783,17789,17791,17807,17851,17881,17891,17903,17911,17921,17923,17939,17959,17977,17981,17989,18043,18047,18049,18059,18061,18089,18119,18121,18127,18133,18169,18181,18199,18211,18217,18251,18253,18269,18287,18289,18313,18329,18341,18367,18371,18457,18481,18517,18521,18523,18539,18541,18553,18587,18593,18617,18637,18661,18671,18691,18719,18743,18749,18757,18773,18787,18793,18797,18859,18869,18899,18911,18913,18919,18973,18979,19031,19037,19051,19073,19081,19121,19139,19157,19163,19183,19213,19237,19259,19301,19309,19319,19333,19373,19379,19381,19387,19403,19417,19423,19427,19429,19433,19457,19469,19471,19477,19483,19489,19501,19507,19541,19571,19577,19583,19603,19609,19661,19681,19687,19697,19717,19739,19751,19753,19759,19763,19813,19843,19853,19867,19913,19919,19927,19937,19949,19973,19979,19991,19993,20011,20021,20023,20047,20051,20089,20101,20107,20113,20143,20147,20173,20177,20201,20219,20231,20233,20249,20269,20323,20341,20347,20357,20359,20369,20393,20399,20411,20431,20443,20479,20483,20509,20521,20543,20549,20551,20563,20593,20639,20641,20681,20749,20753,20759,20771,20773,20789,20807,20809,20849,20857,20879,20887,20897,20899,20921,20929,20947,20959,20963,20981,21001,21011,21017,21023,21031,21061,21089,21107,21121,21139,21143,21157,21163,21187,21191,21211,21221,21227,21247,21277,21283,21313,21317,21347,21379,21383,21391,21397,21407,21419,21467,21481,21493,21517,21521,21529,21559,21563,21569,21577,21587,21599,21611,21613,21617,21649,21673,21713,21727,21737,21739,21751,21773,21787,21799,21817,21871,21937,21977,21991,21997,22003,22013,22039,22063,22073,22079,22093,22109,22123,22129,22147,22229,22247,22259,22273,22277,22279,22283,22291,22343,22349,22367,22369,22381,22391,22409,22453,22483,22501,22511,22531,22541,22549,22571,22573,22613,22619,22621,22639,22643,22651,22697,22699,22721,22727,22741,22783,22807,22811,22853,22859,22861,22877,22921,22937,22943,22963,23003,23017,23027,23053,23059,23071,23087,23099,23117,23131,23159,23167,23173,23189,23197,23201,23203,23209,23227,23251,23269,23279,23291,23293,23297,23311,23327,23357,23369,23399,23431,23447,23473,23509,23549,23563,23581,23593,23599,23609,23623,23633,23663,23677,23687,23741,23743,23747,23753,23761,23767,23773,23801,23813,23819,23827,23831,23833,23857,23869,23873,23879,23887,23917,23929,23981,24001,24029,24043,24049,24071,24077,24083,24091,24103,24107,24121,24133,24137,24151,24169,24181,24197,24203,24223,24229,24247,24251,24281,24329,24337,24359,24371,24373,24379,24413,24421,24473,24481,24509,24517,24527,24533,24547,24551,24631,24671,24677,24697,24709,24767,24781,24793,24809,24847,24851,24907,24917,24919,24923,24943,24971,24979,24989,25013,25031,25073,25097,25111,25121,25127,25147,25153,25163,25169,25171,25183,25189,25219,25229,25237,25247,25301,25321,25343,25349,25357,25367,25391,25409,25411,25423,25439,25447,25457,25469,25523,25541,25561,25577,25583,25589,25603,25621,25633,25643,25657,25667,25673,25679,25703,25741,25747,25759,25763,25771,25799,25819,25841,25873,25889,25913,25919,25939,25943,25951,25969,25999,26017,26021,26041,26053,26083,26099,26107,26119,26141,26161,26171,26177,26189,26203,26209,26227,26237,26267,26293,26297,26309,26321,26347,26387,26399,26407,26431,26449,26459,26479,26497,26513,26539,26561,26573,26591,26597,26627,26633,26669,26681,26683,26687,26699,26701,26711,26729,26731,26737,26759,26777,26783,26813,26833,26839,26849,26881,26891,26903,26927,26953,26959,26987,26993,27031,27043,27061,27067,27077,27091,27103,27109,27127,27143,27191,27197,27211,27259,27271,27277,27281,27299,27329,27361,27367,27397,27407,27409,27427,27431,27437,27449,27457,27479,27539,27581,27611,27647,27653,27689,27691,27697,27701,27733,27739,27743,27751,27763,27767,27773,27779,27791,27793,27799,27809,27823,27827,27851,27883,27893,27901,27941,27947,27953,27961,27983,28001,28019,28031,28069,28081,28097,28099,28111,28123,28151,28181,28201,28211,28229,28277,28279,28283,28289,28307,28309,28349,28393,28411,28433,28439,28447,28463,28477,28513,28517,28537,28541,28549,28559,28579,28597,28607,28619,28621,28657,28661,28663,28669,28687,28703,28711,28723,28729,28751,28759,28771,28789,28793,28807,28843,28859,28867,28933,28949,28961,29021,29023,29027,29033,29059,29123,29129,29131,29137,29147,29153,29173,29179,29191,29207,29209,29221,29251,29269,29297,29303,29311,29327,29333,29339,29347,29363,29389,29401,29411,29423,29429,29437,29453,29473,29483,29501,29569,29573,29581,29599,29611,29663,29669,29671,29717,29741,29753,29761,29789,29819,29833,29863,29867,29879,29881,29917,29921,29927,29959,29983]
#K = 453785

A = [1,3769,4283,4937,5197,5563,6053,7487,7589,8819,9041,12953,15287,15937,16087,19139,20747,23879,24623,29327]
K = 125

def FUNC1(A):
	pile = [(x, max(A)) for x in A[:-1]]
	pileresult = [x[0] / x[1] for x in pile]
	used = pile[:]
	i = 0
	while i < K:
		minidx = pileresult.index(min(pileresult))
		m = pile[minidx]
		son, mom = m
		idxson, idxmom = A.index(son), A.index(mom)
		newson, newmom = A[idxson + 1], A[idxmom - 1]
		next1, next2, nex = None, None, None
		if (newson, mom) not in used and newson < mom:
			next1 = (newson, mom)
		if (son, newmom) not in used and son < newmom and idxmom != 0:
			next2 = (son, newmom)
		if next1 and next2:
			nex = next1 if newson * newmom < son * mom else next2
		elif next1 or next2:
			nex = next1 if next1 else next2
		if nex:
			pile = [nex] + pile
			pileresult = [nex[0] / nex[1]] + pileresult
			used.append(nex)
		if not (next1 or next2):
			pile.remove(m)
			pileresult.remove(m[0] / m[1])
			used.remove(m)
			i += 1
	#return m
	print(m)

def FUNC2(A):
	lenth = len(A)
	pile = [(i, lenth - 1) for i in range(lenth - 1)]
	pileresult = [A[x[0]] / A[x[1]] for x in pile]
	used = pile[:]
	i = 0
	while i < K:
		minidx = pileresult.index(min(pileresult))
		m = pile[minidx]
		idxson, idxmom = m
		son, mom = A[idxson], A[idxmom]
		idxnewson, idxnewmom = idxson + 1, idxmom - 1
		newson, newmom = A[idxnewson], A[idxnewmom]
		next1, next2, nex = None, None, None
		if (idxnewson, idxmom) not in used and newson < mom:
			next1 = (idxnewson, idxmom)
		if (idxson, idxnewmom) not in used and son < newmom and idxmom != 0:
			next2 = (idxson, idxnewmom)
		if next1 and next2:
			(nex, is_next1) = (next1, True) if newson * newmom - son * mom < 0 else (next2, False)
		elif next1 or next2:
			(nex, is_next1) = (next1, True) if next1 else (next2, False)
		if nex:
			pile.append(nex)
			pileresult += [newson / mom] if is_next1 else [son / newmom]
			used.append(nex)
		if not (next1 or next2):
			pile.remove(m)
			pileresult.remove(son / mom)
			used.remove(m)
			i += 1
	#return [A[m[0]], A[m[1]]]
	print([A[m[0]], A[m[1]]])

def FUNC3(A):
	pile = [(x, max(A)) for x in A[:-1]]
	pileresult = [x[0] / x[1] for x in pile]
	used = pile[:]
	i = 0
	while i < K:
		minidx = pileresult.index(min(pileresult))
		m = pile[minidx]
		son, mom = m
		idxson, idxmom = A.index(son), A.index(mom)
		newson, newmom = A[idxson + 1], A[idxmom - 1]
		if (newson, mom) not in used and newson < mom:
			next1 = (newson, mom)
			pile.append(next1)
			pileresult.append(newson / mom)
			used.append(next1)
		if (son, newmom) not in used and son < newmom:
			next2 = (son, newmom)
			pile.append(next2)
			pileresult.append(son / newmom)
			used.append(next2)
		pile.remove(m)
		pileresult.remove(son / mom)
		used.remove(m)
		i += 1
	#return m
	print(m)

def FUNC4(A):
	lenth = len(A)
	pile = [(i, lenth - 1) for i in range(lenth - 1)]
	pileresult = [A[x[0]] / A[x[1]] for x in pile]
	for i in range(K):
		minidx = pileresult.index(min(pileresult))
		m = pile[minidx]
		idxson, idxmom = m
		idxnewson, idxnewmom = idxson + 1, idxmom - 1
		son, mom = A[idxson], A[idxmom]
		newson, newmom = A[idxnewson], A[idxnewmom]
		if (idxnewson, idxmom) not in pile and newson < mom:
			pile.append((idxnewson, idxmom))
			pileresult.append(newson / mom)
		if (idxson, idxnewmom) not in pile and son < newmom and idxmom != 0:
			pile.append((idxson, idxnewmom))
			pileresult.append(son / newmom)
		pile.remove(m)
		pileresult.remove(son / mom)
		print(len(pile))
	#return [A[m[0]], A[m[1]]]
	print([A[m[0]], A[m[1]]])

FUNC4(A)