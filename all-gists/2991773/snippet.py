#! /usr/bin/env python
# -*- conding:utf8 -*-
# authors Julien Recurt
#         Christophe Narbonne

import sys
import urllib
import commands
import collections
import socket
import re
import pprint
import json


def my_default():
    return '1'

countries = collections.defaultdict(my_default)
SECRET_VAR = "azerty"
SERVER_ADDRESS = "http://blacklist.servme.fr/reciver.php"

countries.update({ 'AF':  '2',
	'AX':  '3',
	'AL':  '4',
	'DZ':  '5',
	'AS':  '6',
	'AD':  '7',
	'AO':  '8',
	'AI':  '9',
	'AQ':  '10',
	'AG':  '11',
	'AR':  '12',
	'AM':  '13',
	'AW':  '14',
	'AU':  '15',
	'AT':  '16',
	'AZ':  '17',
	'BS':  '18',
	'BH':  '19',
	'BD':  '20',
	'BB':  '21',
	'BY':  '22',
	'BE':  '23',
	'BZ':  '24',
	'BJ':  '25',
	'BM':  '26',
	'BT':  '27',
	'BO':  '28',
	'BA':  '29',
	'BW':  '30',
	'BV':  '31',
	'BR':  '32',
	'IO':  '33',
	'BN':  '34',
	'BG':  '35',
	'BF':  '36',
	'BI':  '37',
	'KH':  '38',
	'CM':  '39',
	'CA':  '40',
	'CV':  '41',
	'KY':  '42',
	'CF':  '43',
	'TD':  '44',
	'CL':  '45',
	'CN':  '46',
	'CX':  '47',
	'CC':  '48',
	'CO':  '49',
	'KM':  '50',
	'CG':  '51',
	'CD':  '52',
	'CK':  '53',
	'CR':  '54',
	'CI':  '55',
	'HR':  '56',
	'CU':  '57',
	'CY':  '58',
	'CZ':  '59',
	'DK':  '60',
	'DJ':  '61',
	'DM':  '62',
	'DO':  '63',
	'EC':  '64',
	'EG':  '65',
	'SV':  '66',
	'GQ':  '67',
	'ER':  '68',
	'EE':  '69',
	'ET':  '70',
	'FK':  '71',
	'FO':  '72',
	'FJ':  '73',
	'FI':  '74',
	'FR':  '75',
	'GF':  '76',
	'PF':  '77',
	'TF':  '78',
	'GA':  '79',
	'GM':  '80',
	'GE':  '81',
	'DE':  '82',
	'GH':  '83',
	'GI':  '84',
	'GR':  '85',
	'GL':  '86',
	'GD':  '87',
	'GP':  '88',
	'GU':  '89',
	'GT':  '90',
	'GG':  '91',
	'GN':  '92',
	'GW':  '93',
	'GY':  '94',
	'HT':  '95',
	'HM':  '96',
	'VA':  '97',
	'HN':  '98',
	'HK':  '99',
	'HU':  '100',
	'IS':  '101',
	'IN':  '102',
	'ID':  '103',
	'IR':  '104',
	'IQ':  '105',
	'IE':  '106',
	'IM':  '107',
	'IL':  '108',
	'IT':  '109',
	'JM':  '110',
	'JP':  '111',
	'JE':  '112',
	'JO':  '113',
	'KZ':  '114',
	'KE':  '115',
	'KI':  '116',
	'KP':  '117',
	'KR':  '118',
	'KW':  '119',
	'KG':  '120',
	'LA':  '121',
	'LV':  '122',
	'LB':  '123',
	'LS':  '124',
	'LR':  '125',
	'LY':  '126',
	'LI':  '127',
	'LT':  '128',
	'LU':  '129',
	'MO':  '130',
	'MK':  '131',
	'MG':  '132',
	'MW':  '133',
	'MY':  '134',
	'MV':  '135',
	'ML':  '136',
	'MT':  '137',
	'MH':  '138',
	'MQ':  '139',
	'MR':  '140',
	'MU':  '141',
	'YT':  '142',
	'MX':  '143',
	'FM':  '144',
	'MD':  '145',
	'MC':  '146',
	'MN':  '147',
	'ME':  '148',
	'MS':  '149',
	'MA':  '150',
	'MZ':  '151',
	'MM':  '152',
	'NA':  '153',
	'NR':  '154',
	'NP':  '155',
	'NL':  '156',
	'AN':  '157',
	'NC':  '158',
	'NZ':  '159',
	'NI':  '160',
	'NE':  '161',
	'NG':  '162',
	'NU':  '163',
	'NF':  '164',
	'MP':  '165',
	'NO':  '166',
	'OM':  '167',
	'PK':  '168',
	'PW':  '169',
	'PS':  '170',
	'PA':  '171',
	'PG':  '172',
	'PY':  '173',
	'PE':  '174',
	'PH':  '175',
	'PN':  '176',
	'PL':  '177',
	'PT':  '178',
	'PR':  '179',
	'QA':  '180',
	'RE':  '181',
	'RO':  '182',
	'RU':  '183',
	'RW':  '184',
	'EH':  '185',
	'BL':  '186',
	'SH':  '187',
	'KN':  '188',
	'LC':  '189',
	'PM':  '190',
	'VC':  '191',
	'WS':  '192',
	'SM':  '193',
	'MF':  '194',
	'ST':  '195',
	'SA':  '196',
	'SN':  '197',
	'RS':  '198',
	'SC':  '199',
	'SL':  '200',
	'SG':  '201',
	'SK':  '202',
	'SI':  '203',
	'SB':  '204',
	'SO':  '205',
	'ZA':  '206',
	'GS':  '207',
	'ES':  '208',
	'LK':  '209',
	'SD':  '210',
	'SR':  '211',
	'SJ':  '212',
	'SZ':  '213',
	'SE':  '214',
	'CH':  '215',
	'SY':  '216',
	'TW':  '217',
	'TJ':  '218',
	'TZ':  '219',
	'TH':  '220',
	'TL':  '221',
	'TG':  '222',
	'TK':  '223',
	'TO':  '224',
	'TT':  '225',
	'TN':  '226',
	'TR':  '227',
	'TM':  '228',
	'TC':  '229',
	'TV':  '230',
	'UG':  '231',
	'UA':  '232',
	'AE':  '233',
	'GB':  '234',
	'US':  '235',
	'UM':  '236',
	'UY':  '237',
	'UZ':  '238',
	'VU':  '239',
	'VE':  '240',
	'VN':  '241',
	'VG':  '242',
	'VI':  '243',
	'WF':  '244',
	'EH':  '245',
	'YE':  '246',
	'ZM':  '247',
    'ZW':  '248',
})

banning_ip, rule_name = sys.argv[1:3]


current_whois = commands.getoutput('whois %s' % (banning_ip))
#current_nmap = commands.getoutput('nmap %s' % (banning_ip))


current_re = re.compile('netname:(?P<name>.*)', re.IGNORECASE)

my_match = re.search(current_re, current_whois)

if my_match:
    netname = my_match.groupdict()['name'].strip()

current_re = re.compile('country:(?P<country>.*)', re.IGNORECASE)
my_match = re.search(current_re, current_whois)

if my_match:
    country = countries.get(my_match.groupdict()['country'].strip(), None)

host_name = socket.gethostbyaddr(banning_ip)[0]

data = {"data": json.dumps({'host_nname': host_name, 'netname': netname, 'country':country,
    'current_whois':current_whois,'banning_ip':banning_ip})}

urllib.urlopen(SERVER_ADDRESS, data=data["data"])