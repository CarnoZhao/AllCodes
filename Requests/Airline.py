import urllib.request
import json

ctrip_header = \
	{'User-Agent':\
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
    'Host': \
    	'flights.ctrip.com',
    'Referer': \
    	'http://flights.ctrip.com/international/FlightResult.aspx?flighttype=D&DCity=BJS&ACity=NYC&relddate=2019-01-19&relrdate=2019-05-22'
    }
def search_flight(dayto, dayback):
	request_url = 'http://flights.ctrip.com/international/FlightResult.aspx?flighttype=D&DCity=BJS&ACity=NYC&relddate=2019-01-' \
				+ dayto \
				+ '&relrdate=2019-05-' \
				+ dayback
				#+ '&cabin=y_s&adult=1&child=0&infant=0&isbuildup=1'
	req = urllib.request.Request(request_url, headers = ctrip_header)
	body = urllib.request.urlopen(req, timeout = 30).read().decode('gbk', 'ignore')
	print(body)

if __name__ == '__main__':
    search_flight('19', '22')
