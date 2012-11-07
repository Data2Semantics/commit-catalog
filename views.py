'''
Created on Oct 29, 2012

@author: hoekstra
'''

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from gdata.spreadsheet.service import SpreadsheetsService
from gdata.spreadsheet.text_db import Record
from datetime import datetime
from pprint import pprint
from copy import copy
from models import Entry
import oauth2 as oauth

client = SpreadsheetsService()

key = '0AoZ8cO4z-Kh7dExWOEhsaHk5WUtDdHVhQU1IbjJxOHc'



CONSUMER_KEY = "BRDxVY2tIkIin3Qs3iopWw"
CONSUMER_SECRET = "Rb15FFj0CXBulQnqEzlB1RwewE1DJ1HKpW4PSS5xOWE"
token_key = "368874255-U6XY15PuoRnwlgOMAT3Bxh2l7SvlonkOf6Ne8JPr"
token_secret = "g52I9RKN1zso84z3C0L1fedpimkeTpB1dXQAqMytg"


cons = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
tok = oauth.Token(token_key, token_secret)
c = oauth.Client(cons, tok)





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
        
    check_for_updates(sorted_records)
    
    return render_to_response('records.html',{'records': sorted_records})
    

def check_for_updates(records):
    
    for r in records:
        name = r['vocab']
        for e in r['entries'] :
            timestamp = datetime.strptime(e['timestamp'],'%m/%d/%Y %H:%M:%S')
            
            m = Entry.objects.filter(name=name,timestamp=timestamp)
            if len(m) == 0 :
                entry = Entry(name=name,timestamp=timestamp)
                entry.save()
                print '{} ({}) is new!'.format(name,str(timestamp))
                tweet_about_it(name, e)
            else :
                print '{} ({}) already exists!'.format(name,str(timestamp))
        

def tweet_about_it(name, entry):
    tweet = 'status={}'.format("{} just added {} to the #COMMIT_nl Data and Vocabulary Catalog at http://bit.ly/d2scatalog".format(entry['whatsyourname'].encode('utf-8'),name.encode('utf-8')))

    c.request('http://api.twitter.com/1.1/statuses/update.json',method="POST",body=tweet)
    
    return
        