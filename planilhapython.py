import gspread

from oauth2client.service_account import ServiceAccountCredentials

import pprint

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('planilha_python').sheet1

pp = pprint.PrettyPrinter()

#result = sheet.get_all_records()	# all records
#result = sheet.row_values(10)		# just a row
result = sheet.cell(5,13).value		# specific cell

pp.pprint(result)