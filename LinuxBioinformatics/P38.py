import pysam
from collections import defaultdict
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
bam = pysam.AlignmentFile('NA18489.chrom20.ILLUMINA.bwa.YRI.exome.20121211.bam', 'rb')

def Headerinspect():
    headers = bam.header
    for record_type, records in headers.items():
        print(record_type)
        for i, record in enumerate(records):
            print('\t%d' % (i + 1))
            if type(record) == str:
                print('\t\t%s' % record)
            elif type(record) == dict:
                for field, value in record.items():
                    print('\t\t%s\t%s' % (field, value))

def RecordInspect():
    for rec in bam:
        if rec.cigarstring.find('M') > -1 and \
            rec.cigarstring.find('S') > -1 and \
            not rec.is_unmapped and \
            not rec.mate_is_unmapped:
            break
    print(rec.query_name, rec.reference_id, bam.getrname(rec.reference_id), rec.reference_start, rec.reference_end, '\n')
    print(rec.cigarstring, '\n')
    print(rec.query_alignment_start, rec.query_alignment_end, rec.query_alignment_length, '\n')
    print(rec.next_reference_id, rec.next_reference_start, rec.template_length, '\n')
    print(rec.is_paired, rec.is_proper_pair, rec.is_unmapped, rec.mapping_quality, '\n')
    print(rec.query_qualities, '\n')
    print(rec.query_alignment_qualities, '\n')
    print(rec.query_sequence, '\n')

def PlotDistribution():
    counts = [0] * 76
    for n, rec in enumerate(bam.fetch('20', 0, 10000000)):
        for i in range(rec.query_alignment_start, rec.query_alignment_end):
            counts[i] += 1
    freqs = [x / (n + 1.) for x in counts]
    plt.plot(range(1, 77), freqs)
    plt.show()


def PhredDistribution():
    phreds = defaultdict(list)
    for rec in bam.fetch('20', 0, None):
        for i in range(rec.query_alignment_start, rec.query_alignment_end):
            phreds[i].append(rec.query_qualities[i])
    maxs = [max(phreds[i]) for i in range(76)]
    tops = [np.percentile(phreds[i], 95) for i in range(76)]
    medians = [np.percentile(phreds[i], 50) for i in range(76)]
    bottoms = [np.percentile(phreds[i], 5) for i in range(76)]
    medians_fig = [x - y for x, y in zip(medians, bottoms)]
    tops_fig = [x - y for x, y in zip(tops, medians)]
    maxs_fig = [x - y for x, y in zip(maxs, tops)]
    fig, ax = plt.subplots()
    ax.stackplot(range(1, 77), (bottoms, medians_fig, tops_fig))
    ax.plot(range(1, 77), maxs, 'k-')
    plt.show()

#Headerinspect()

#RecordInspect()

#PlotDistribution()

PhredDistribution()