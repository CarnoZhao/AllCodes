from collections import defaultdict
import vcf
import seaborn as sns
import matplotlib.pyplot as plt

vcf_names = ['centro.vcf.gz', 'standard.vcf.gz']

def get_sample_relation(recs, f1, f2):
    rel = defaultdict(int)
    for rec in recs:
        if not rec.is_snp:
            continue
        for sample in rec.samples:
            try:
                v1 = f1(sample)
                v2 = f2(sample)
                if v1 is None or v2 is None:
                    continue
                rel[(v1, v2)] += 1
            except:
                pass
    return rel

rels = {}
for vcf_name in vcf_names:
    recs = vcf.Reader(filename = vcf_name)
    rels[vcf_name] = get_sample_relation(recs, \
        lambda s: 1 if s.is_het else 0, lambda s: int(s['DP']))

def plot_hz_rel(dps, ax, ax2, name, rel):
    frac_hz = []
    cnt_dp = []
    for dp in dps:
        hz = 0.0
        cnt = 0
        for khz, kdp in rel.keys():
            if kdp != dp:
                continue
            cnt += rel[(khz, dp)]
            if khz == 1:
                hz += rel[(khz, dp)]
        frac_hz.append(hz / cnt)
        cnt_dp.append(cnt)
    ax.plot(dps, frac_hz, label = name)
    ax2.plot(dps, cnt_dp, '--', label = name)

fig, ax = plt.subplots(figsize = (16, 9))
ax2 = ax.twinx()
for name, rel in rels.items():
    dps = list(set([x[1] for x in rel.keys()]))
    dps.sort()
    plot_hz_rel(dps, ax, ax2, name, rel)

ax.set_xlim(0, 75)
ax.set_ylim(0, 0.2)
ax2.set_ylabel('Quality of calls')
ax.set_ylabel('Fraction of Heterozygote calls')
ax.set_xlabel('Sample Read Depth (DP)')
fig.suptitle('Number of calls per depth and fraction of calls which are Hz', \
    fontsize = 'xx-large')
plt.show()
plt.savefig('P55.png')