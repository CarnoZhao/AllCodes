from collections import defaultdict
import vcf
import matplotlib.pyplot as plt
import seaborn as sns

def get_variant_relation(recs, f1, f2):
	rel = defaultdict(int)
	for rec in recs:
		if not rec.is_snp:
			continue
		try:
			v1 = f1(rec)
			v2 = f2(rec)
			if v1 is None or v2 is None:
				continue
			rel[(v1, v2)] += 1
		except:
			pass
	return rel

accepted_eff = ['INTERGENIC', 'INTRON', \
	'NON_SYNONYMOUS_CODING', 'SYNONYMOUS_CODING']

def eff_to_int(rec):
	try:
		for annot in rec.INFO['EFF']:
			master_type = annot.split('(')[0]
			return accepted_eff.index(master_type)
	except ValueError:
		return len(accepted_eff)

eff_mq0s = {}
for vcf_name in ['standard.vcf.gz', 'centro.vcf.gz']:
	recs = vcf.Reader(filename = vcf_name)
	eff_mq0s[vcf_name] = get_variant_relation(recs, \
		lambda r: eff_to_int(r), lambda r: int(r.INFO['DP']))

fig, ax = plt.subplots(figsize = (16, 9))
vcf_name = 'standard.vcf.gz'
bp_vals = [[] for x in range(len(accepted_eff) + 1)]
for k, cnt in eff_mq0s[vcf_name].items():
	my_eff, mq0 = k
	bp_vals[my_eff].extend([mq0] * cnt)

sns.boxplot(data = bp_vals, sym = '', ax = ax)
ax.set_xticklabels(accepted_eff + ['OTHER'])
ax.set_ylabel('DP (Variant)')
fig.suptitle('Distribution of variant DP per SNP type', \
	fontsize = 'xx-large')
plt.show()
plt.savefig('P57.png')