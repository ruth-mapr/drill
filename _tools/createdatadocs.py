#!/usr/bin/python

import json
from itertools import tee, islice, chain, izip

def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return izip(prevs, items, nexts)

def pretty_print(data, filename=None):
    if filename is None:
        print(json.dumps(data, sort_keys=True, indent=4))
    else:
        with open(filename, 'w') as outfile:
            json.dump(data, outfile, sort_keys=True, indent=4)

def add_docs(docs_in_order, doc):
    docs_in_order.append(doc)
    for doc in doc['children']:
        add_docs(docs_in_order, doc)

def create_previous_and_next(docs_in_order):
    for previous_doc, current_doc, next_doc in previous_and_next(docs_in_order):
        if previous_doc is not None:
            current_doc['previous_title'] = previous_doc['title']
            current_doc['previous_url'] = previous_doc['url']
        else:
            current_doc['previous_title'] = ''
            current_doc['previous_url'] = ''
        if next_doc is not None:
            current_doc['next_title'] = next_doc['title']
            current_doc['next_url'] = next_doc['url']
        else:
            current_doc['next_title'] = ''
            current_doc['next_url'] = ''
    
def create_breadcrumbs(docs_in_order, docs_by_title):
    for doc in docs_in_order:
        doc['breadcrumbs'] = []
        parent_title = doc.get('parent')
        while parent_title != '':
            parent = docs_by_title[parent_title]
            doc['breadcrumbs'].append({'url': parent['url'], 'title': parent['title']})
            parent_title = parent.get('parent')

if __name__ == '__main__':
    input_path = '_site/data/index.html'
    output_path = '_data/docs.json'

    with open(input_path) as input_file:
        docs = json.load(input_file)

    docs_by_title = {}
    docs_in_order = []
    top_level_docs = []
    
    for doc in docs:
        docs_by_title[doc['title']] = doc
        doc['children'] = []

    for doc in docs:
        if doc['parent'] == '':
            top_level_docs.append(doc)
        else:
            docs_by_title[doc['parent']]['children'].append(doc)

    for doc in top_level_docs:
        add_docs(docs_in_order, doc)
    
    create_previous_and_next(docs_in_order)
    create_breadcrumbs(docs_in_order, docs_by_title)

    result = {'hierarchy': top_level_docs, 'by_title': docs_by_title}
    pretty_print(result)
    pretty_print(result, output_path)
    