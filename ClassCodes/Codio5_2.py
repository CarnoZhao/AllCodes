import os
import subprocess
#import toytree
import requests
import pandas as pd
# execute this cell to create the get_uids function

def get_uids(term, retmax=10):
    "Search NCBI nucleotide database and return N sequence matches"
    
    # make a request to esearch 
    res = requests.get(
        url="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi", 
        params={
            "db": "nucleotide",
            "term": term,
            "sort": "length",
            "retmode": "text",
            "retmax": retmax,
            "tool": "genomics-course", 
            "email": "de2356@columbia.edu",
            },
        )
    
    # parse the xml output
    count = res.text.split("<Count>")[1].split("</Count>")[0].strip()
    
    # if nothing found then bail out
    if not int(count):
        raise ValueError("No UIDs found")
    
    # return the list of UIDs
    uids = []
    ids = res.text.split("<IdList>")[1].split("</IdList>")[0].strip()
    for item in ids.split("\n"):
        uids.append(item[4:-5])
    return uids

def get_fasta(uids):
    """
    Fetch fasta sequence data from NCBI for a list of uids
    and return as a dictionary of {name: sequence}.
    """
    # make a request to efetch 
    res = requests.get(
        url="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi", 
            params={
            "db": "nucleotide",
            "id": ",".join(uids),
            "seq_start": "1",
            "seq_stop": "2000",
            "strand": "1",
            "retmode": "text",   
            "rettype": "fasta",
            "tool": "genomics-course", 
            "email": "de2356@columbia.edu",
            },
        )
    
    # split fasta string into separate fasta sequences
    fastas = res.text.strip().split("\n\n")
    
    # write to output file
    with open("sequences.fasta", 'w') as out:
        for fasta in fastas:

            # separate name and sequence
            name, sequence = fasta.split("\n", 1)

            # reorder and shorten fasta names for easier reading
            bits = name.split()
            genus = bits[1][0]
            species = bits[2]
            accession = bits[0][1:].split(":")[0]
            name = ">{}_{}_{}".format(genus, species, accession)

            # remove line breaks from sequence
            sequence = sequence.replace("\n", "")

            # write to file
            out.write("{}\n{}\n".format(name, sequence))
    
    # print statement
    print("Wrote {} sequences to ./sequences.fasta".format(len(fastas)))
    
def highlight_dna(cell):
    "A function to color cells by DNA base"
    color = {"A": 'red', "T": 'blue', "C": 'green', "G": 'yellow', "-": "lightgrey"}
    return 'background-color: {}'.format(color[cell])


def colored_slice(fasta, start, stop):
    "returns a colored dataframe over a given slice"
    # load seq data 
    with open(fasta) as infile:

        # load sequence file as a dictionary
        fdict = {}
        for fa in infile.read().strip()[1:].split("\n>"):
            name, seq = fa.split("\n")
            fdict[name] = list(seq)[start: stop]

        # make dataframe from dictionary
        df = pd.DataFrame(fdict, index=range(start, stop)).T

    # show dataframe as colored cells
    return df.style.applymap(highlight_dna)
def align_fasta(fasta_file):
    
    # the output aligned file name to use
    aligned = fasta_file + ".aligned"
    
    # run muscle alignment program on fasta file to produce output file
    cmd = ["muscle", "-in", fasta_file, "-out", aligned]
    subprocess.call(cmd)

    # read in results of aligned file
    with open(aligned) as infile:
        fastas = infile.read().strip()[1:].split("\n>")
        
    # remove newlines from aligned file
    with open(aligned, 'w') as out:
        for fasta in fastas:

            # separate name and sequence
            name, sequence = fasta.split("\n", 1)

            # remove line breaks from sequence
            sequence = sequence.replace("\n", "")

            # write to file
            out.write(">{}\n{}\n".format(name, sequence))
    
    # print statement
    print("Wrote aligned file to {}".format(aligned))
    

# call the function to get uids and store as a list
term = "eIF1B[GENE] AND Bos[ORGN]"
ingroup = get_uids(term=term, retmax=20)

# call the function to uids from an *outgroup* and add to list
oterm = "eIF1B[GENE] AND Homo[ORGN]"
outgroup = get_uids(term=oterm, retmax=2)

# show uids
uids = ingroup + outgroup
print(uids)

# get fasta data for the UIDs
get_fasta(uids)

# run the alignment program
align_fasta("./sequences.fasta")

# looking in the middle of the file it's clear they are not aligned
#colored_slice("./sequences.fasta.aligned", 100, 150)