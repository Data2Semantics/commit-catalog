'''
Created on Oct 29, 2012

@author: hoekstra
'''

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from gdata.spreadsheet.service import SpreadsheetsService
from gdata.spreadsheet.text_db import Record
from pprint import pprint
from copy import copy

client = SpreadsheetsService()

key = '0AoZ8cO4z-Kh7dExWOEhsaHk5WUtDdHVhQU1IbjJxOHc'





def index(request):
    client = SpreadsheetsService()
    rfeed = client.GetListFeed(key=key, wksht_id='od6', visibility='public', projection='values')

    records_dict = {}
    group_key = 'whatsthenameofthedatasetorvocabulary'   
    
    for r in rfeed.entry :
        record = Record(row_entry=r)
        row = record.content
        vocab = row[group_key]
        del(row[group_key])
        
        records_dict.setdefault(vocab,[]).append(row) 

    sorted_keys = sorted(records_dict.keys())
    
    sorted_records = []
    for k in sorted_keys :
        k_dict = {'vocab': k, 'entries': records_dict[k]}
        sorted_records.append(k_dict)
        
    return render_to_response('records.html',{'records': sorted_records})
    
        
        