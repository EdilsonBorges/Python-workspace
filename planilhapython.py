import gspread

from oauth2client.service_account import ServiceAccountCredentials

import pprint

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('planilha_python').sheet1

pp = pprint.PrettyPrinter()

result = sheet.row_values(10)

pp.pprint(result)