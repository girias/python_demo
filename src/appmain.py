"""#!/usr/bin/python"""
import json
from addusers import insert_users
from getusers import get_all_users

insert_users(json.load(open('../data/data.json')))
get_all_users()
