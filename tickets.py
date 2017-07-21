'''命令行火车票查看器


Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help    显示帮助菜单
    -g           高铁
    -d           动车
    -t           特快
    -k           快速
    -z           直达

'''

from docopt import docopt
from stations import stations
import requests
from pprint import pprint

def cli():
	"""command-line interface"""
	arguments = docopt(__doc__, version='Tickets 1.0')
	from_station = stations.get(arguments['<from>'],None)
	to_station = stations.get(arguments['<to>'],None)
	train_date = arguments['<date>']
	url = ('https://kyfw.12306.cn/otn/leftTicket/query?'
		   'leftTicketDTO.train_date={}&'
		   'leftTicketDTO.from_station={}&'
		   'leftTicketDTO.to_station={}&'
		   'purpose_codes=ADULT').format(train_date,from_station,to_station)
	r = requests.get(url,verify=False)
	pprint(r.json())

	

if __name__ == '__main__':
	cli()