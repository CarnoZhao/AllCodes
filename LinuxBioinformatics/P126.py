from collections import OrderedDict
num_loci = 10
pop_size = 100
num_gens = 10
init_ops = OrderedDict()
pre_ops = OrderedDict()
post_ops = OrderedDict()

import simuPOP as sp
pops = sp.Population(pop_size, loci = [1] * num_loci)
init_ops['Sex'] = sp.InitSex()
init_ops['Freq'] = sp.InitGenotype(freq = [0.5, 0.5])
post_ops['Stat-freq'] = sp.Stat(alleleFreq = sp.ALL_AVAIL)
post_ops['Stat-freq-eval'] = sp.PyEval(r"'%d %.2f\n' % (gen, alleleFreq[0][0])")
mating_scheme = sp.RandomMating()
sim = sp.Simulator(pops, rep = 1)
sim.evolve(initOps = list(init_ops.values()), preOps = list(pre_ops.values()), \
	postOps = list(post_ops.values()), matingScheme = mating_scheme, gen = num_gens)

'''from copy import deepcopy
def init_accumulator(pop, param):
	accumulators = param
	for accumulator in accumulators:
		pop.vars()[accumulator] = []
	return True

def update_accumulator(pop, param):
	accumulator, var = param
	pop.vars()[accumulator].append(deepcopy(pop.vars()[var]))
	return True
def calc_exp_he(pop):
	pop.dvars().expHe = {}
	for locus, freqs in pop.dvars().alleleFreq.items():
		f0 = freqs[0]
		pop.dvars().expHe[locus] = 1 - f0 ** 2 - (1 - f0) ** 2
	return True

init_ops['accumulators'] = sp.PyOperator(init_accumulator, param = ('num_males', 'exp_he'))
post_ops['Stat-males'] = sp.Stat(numOfMales = True)
post_ops['ExpHe'] = sp.PyOperator(calc_exp_he)
post_ops['male_accumulation'] = sp.PyOperator(update_accumulator, param = ('num_males', 'numOfMales'))
post_ops['expHe_accumulation'] = sp.PyOperator(update_accumulator, param = ('exp_he', 'expHe'))
del post_ops['Stat-freq-eval']

num_gens = 100
pops_500 = sp.Population(500, loci = [1] * num_loci)
sim = sp.Simulator(pops_500, rep = 1)
sim.evolve(initOps = list(init_ops.values()), preOps = list(pre_ops.values()), postOps = list(post_ops.values()), \
	matingScheme = mating_scheme, gen = num_gens)
pop_500_after = deepcopy(sim.population(0))
pops_40 = sp.Population(40, loci = [1] * num_loci)
sim = sp.Simulator(pops_40, rep = 1)
sim.evolve(initOps = list(init_ops.values()), preOps = list(pre_ops.values()), postOps = list(post_ops.values()), \
	matingScheme = mating_scheme, gen = num_gens)
pop_40_after = deepcopy(sim.population(0))

import numpy as np
import seaborn as sns
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def calc_loci_stat(var, fun):
	stat = []
	for gen_data in var:
		stat.append(fun(list(gen_data.values())))
	return stat

sns.set_style('white')
fig, axs = plt.subplots(1, 2, figsize = (16, 9), sharey = True, squeeze = False)

def plot_pop(ax1, pop):
	for locus in range(num_loci):
		ax1.plot([x[locus] for x in pop.dvars().exp_he], color = (0.75, 0.75, 0.75))
	mean_exp_he = calc_loci_stat(pop.dvars().exp_he, np.mean)
	ax1.plot(mean_exp_he, color = 'r')

plot_pop(axs[0, 0], pop_40_after)
plot_pop(axs[0, 1], pop_500_after)
ax = fig.add_subplot(4, 4, 13)
ax.boxplot(pop_40_after.dvars().num_males)
ax = fig.add_subplot(4, 4, 16)
ax.boxplot(pop_500_after.dvars().num_males)
fig.tight_layout()
plt.savefig('P126.png')'''