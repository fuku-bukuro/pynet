#!/usr/bin/env python
import textfsm
from pprint import pprint

template_file = "ex2_show_int_status.tpl"
template = open(template_file)

with open("ex2_show_int_status.txt") as f:
    raw_text_data = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

table_keys = re_table.header

final_list = list()

for fsm_list in data:
    entry = dict(zip(table_keys,fsm_list))
    final_list.append(entry)

print()
pprint(final_list)
print()

