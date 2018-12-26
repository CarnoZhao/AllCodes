import requests

ensembl_server = 'http://rest.ensembl.org'

def do_request(server, sevice, *args, **kwargs):
	url_params = ''
	for a in args:
		if a is not None:
			url_params += '/' + a
	req = requests.get('%s/%s%s' % (server, sevice, url_params), \
		params = kwargs, \
		headers = {'Content-Type': 'application/json'})
	if not req.ok:
		req.raise_for_status()
	return req.json()

all_species = do_request(ensembl_server, 'info/species')
#for sp in all_species['species']:
#	print(sp['name'])

ext_dbs = do_request(ensembl_server, 'info/external_dbs', 'homo_sapiens', filter = 'HGNC%')
#print(ext_dbs)

ensembl = do_request(ensembl_server, 'lookup/symbol', 'homo_sapiens', 'LCT')
#print(ensembl)
lct_id = ensembl['id']
	
lct_seq = do_request(ensembl_server, 'sequence/id', lct_id)
#print(lct_seq)

lct_xrefs = do_request(ensembl_server, 'xrefs/id', lct_id)
for xref in lct_xrefs:
	print(xref['db_display_name'])
	#print(xref)

hom_response = do_request(ensembl_server, 'homology/id', lct_id, type = 'orthologues', sequence = 'none')
homologies = hom_response['data'][0]['homologies']
for homology in homologies:
	#print(homology['target']['species'])
	if homology['target']['species'] != 'equus_caballus':
		continue
	#print(homology)
	print(homology['taxonomy_level'])
	horse_id = homology['target']['id']

horse_req = do_request(ensembl_server, 'lookup/id', horse_id)
print(horse_req)