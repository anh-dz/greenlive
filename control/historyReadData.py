from .History_user_db import *
from .Trade_history_user_db import *

mng = History_user_mn(Session(engine))
lmao = mng.history_user_scan(2)

mng2 = Trade_history_user_mn(Session(engine))
vanlalmao = mng2.trade_history_user_scan(2)

def convert(dictionary = {}):
  kq = []
  for i in range(len(dictionary['UserName'])):
      item = {
          'username': dictionary['UserName'][i],
          'vatdung': dictionary['BillCode'][i],
          'thoigian': dictionary['Time'][i],
          'emerald': '-' + str(dictionary['Emerald'][i])
      }
      kq.append(item)
  return kq

tkdoidiem00 = convert(lmao)

def categorize_username(data_list):
    username_list = []
    for item in data_list:
        username = item['username']
        username_list.append(username)

    # Categorize usernames into separate lists
    unique_usernames = set(username_list)
    categorized_usernames = {username: [] for username in unique_usernames}

    for item in data_list:
        username = item['username']
        categorized_usernames[username].append(item)

    # Display the categorized usernames
    for username, items in categorized_usernames.items():
        if username == 'nva':
          return items

tkdoidiem = categorize_username(tkdoidiem00)
if not isinstance(tkdoidiem, list):
   tkdoidiem = []
# tktichdiem = convert(vanlalmao)