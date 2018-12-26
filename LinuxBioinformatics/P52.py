import numpy as np
import functools
import matplotlib.pyplot as plt
import vcf

def do_window(recs, size, fun):
    start = None
    win_res = []
    for rec in recs:
        if not rec.is_snp or len(rec.ALT) > 1:
            continue
        if start is None:
            start = rec.POS
        my_win = 1 + (rec.POS - start) // size
        while len(win_res) < my_win:
            win_res.append([])
        win_res[my_win - 1].extend(fun(rec))
    return win_res

def apply_win_funs(wins, funs):
    fun_results = []
    for win in wins:
        my_funs = {}
        for name, fun in funs.items():
            try:
                my_funs[name] = fun(win)
            except:
                my_funs[name] = None
        fun_results.append(my_funs)
    return fun_results

#Used in P49.py

mq0_wins = {}
vcf_names = ['centro.vcf.gz', 'standard.vcf.gz']
size = 5000

def get_sample(rec, annot, my_type):
    res = []
    samples = rec.samples
    for sample in samples:
        if sample[annot] == None:
            continue
        res.append(my_type(sample[annot]))
    return res

for vcf_name in vcf_names:
    recs = vcf.Reader(filename = vcf_name)
    mq0_wins[vcf_name] = do_window(recs, size, functools.partial(get_sample, annot = 'MQ0', my_type = int))

stats = {}
colors = ['b', 'g']
i = 0
fig, ax = plt.subplots(figsize = (16, 9))
for name, nwins in mq0_wins.items():
    stats[name] = apply_win_funs(nwins, {'median': np.median, '75': functools.partial(np.percentile, q = 75)})
    x_lim = [j * size for j in range(len(stats[name]))]
    ax.plot(x_lim, [x['median'] for x in stats[name]], label = name, color = colors[i])
    ax.plot(x_lim, [x['75'] for x in stats[name]], '--', color = colors[i])
    i += 1

ax.legend()
ax.set_xlabel('Genomic location in the downloaded segment')
ax.set_ylabel('MQ0')
fig.suptitle('Distribution of MQ0 along the genome', fontsize = 'xx-large')

plt.show()