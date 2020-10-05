import pandas as pd
import json
from pandas import ExcelWriter
import xlsxwriter


#form = UploadForm()
#file_name = form.file.data
with open('D:/17-03-20/practisse19-20/experiment2/return.json') as data_file:
    data = json.load(data_file)

results = []

for i in data['b2b']:
    for k, v in i.items():
        if k == 'inv':
            for j in v:
                tmp = [] 
                for z, x in j.items():
                    if z == 'inum':
                        tmp.append(i['ctin'])
                        tmp.append(i['cname'])
                        tmp.append(i['cfs'])
                        tmp.append(x)
                    if z == 'idt':
                        tmp.append(x)
                    if z == 'val':
                        tmp.append(x)
                    if z == 'pos':
                        tmp.append(x)
                    if z == 'inv_typ':
                        tmp.append(x)
                    if z == 'rchrg':
                        tmp.append(x)
                    if z == 'itms':
                        for g in x:
                            for a, b in g.items():
                                if a == 'itm_det':
                                    for c, d in b.items():
                                        if c == 'txval':
                                            tmp.append(d)
                                        if c == 'iamt':
                                            tmp.append(d)                
                results.append(tmp)


for i in results:
    i.append(data['gstin'])
    i.append(data['fp'])


df =  pd.DataFrame(results, columns = ['Total', 'Taxable Amount', 'IGST Amount', 'Invoice Type', 'Place of Supply(State Code)', 'Invoice Date', 'Reverse Charge', 'Customer GSTIN', 
'Customer Name', 'Customer Filling Status', 'Invoice Number', 'Taxpayer GSTIN', 'Filling Period'])

headers = ['Taxpayer GSTIN', 'Filling Period', 'Customer Filling Status', 'Customer GSTIN', 'Customer Name', 'Invoice Number', 'Invoice Date', 'Invoice Type', 'Reverse Charge', 
'Place of Supply(State Code)', 'Taxable Amount', 'IGST Amount', 'Total']

df = df[headers]

results2 = []

for i in data['b2cs']:
    tmp = []
    tmp.append(data['gstin'])
    tmp.append(data['fp'])
    for k, v in i.items():
        if k == 'sply_ty':
            tmp.append(v)
        if k == 'typ':
            tmp.append(v)
        if k == 'pos':
            tmp.append(v)
        if k == 'rt':
            tmp.append(v)
        if k == 'txval':
            tmp.append(v)
        if k == 'camt':
            tmp.append(v)
        if k =='samt':
            tmp.append(v)
    
    results2.append(tmp)

df2 =  pd.DataFrame(results2, columns = ['Taxpayer GSTIN', 'Filling Period', 'CGST Amount', 'GST Rate', 'Place of Supply(State Code)', 'Taxable Amount', 'E-Commerce Type',
'SGST Amount', 'Supply Type'])

results3 = []

for k, v in data['nil'].items():
    if k == 'inv':
        for i in v:
            tmp = []
            tmp.append(data['gstin'])
            tmp.append(data['fp'])
            for a, b in i.items():
                if a == 'sply_ty':
                    tmp.append(b)
    results3.append(tmp)

df3 = pd.DataFrame(results3, columns = ['Taxpayer GSTIN', 'Filling Period', 'Supply Type'])

results4 = []

for k, v in data['hsn'].items():
    if k == 'data':
        for i in v:
            for a, b in i.items():
                if a == 'hsn_sc':
                    results4.append(b)
                if a == 'desc':
                    results4.append(b)
                if a == 'uqc':
                    results4.append(b)
                if a == 'qty':
                    results4.append(b)
                if a == 'txval':
                    results4.append(b)
                if a == 'iamt':
                    results4.append(b)
                if a == 'camt':
                    results4.append(b)
                if a == 'csamt':
                    results4.append(b)
                if a == 'val':
                    results4.append(b)

results4.append(data['gstin'])
results4.append(data['fp'])

tmp = []
tmp.append(results4)

df4 = pd.DataFrame(tmp, columns = ['Total Value', 'Cess Amount', 'Unit', 'Quantity', 'Taxable Amount', 'CGST Amount', 'HSN/SAC', 'IGST Amount', 'Description', 'Taxpyaer GSTIN', 'Filling Period'])

headers = ['Taxpyaer GSTIN', 'Filling Period', 'HSN/SAC', 'Description', 'Unit', 'Quantity', 'Taxable Amount','IGST Amount', 'CGST Amount', 'Cess Amount', 'Total Value']

df4 = df4[headers]

results5 = []
for k, v in data['doc_issue'].items():
    if k == 'doc_det':
        for i in v:
            for a, b in i.items():
                if a == 'docs':
                    for j in b:
                        tmp = []
                        for c, d in j.items():
                            if c == 'num':
                                tmp.append(d)
                            if c == 'from':
                                tmp.append(d)
                            if c == 'to':
                                tmp.append(d)
                            if c == 'totnum':
                                tmp.append(d)
                            if c == 'cancel':
                                tmp.append(d)
                            if c == 'net_issue':
                                tmp.append(d)
                        results5.append(tmp)

df5 = pd.DataFrame(results5, columns = ['Cancel', 'Number', 'Net Issue', 'From', 'To', 'Total Line Number'])

writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name = 'GSTR-1B2BInvoices')

df.to_excel(writer, sheet_name = 'GSTR-1B2BLineItems')

df2.to_excel(writer, sheet_name = 'GSTR-1B2CSSummary')

df3.to_excel(writer, sheet_name = 'GSTR-1NilSummary')

df4.to_excel(writer, sheet_name = 'GSTR-1HSNSummary')

df5.to_excel(writer, sheet_name = 'GSTR-1DocumentIssuedDetails')

variable = writer.save()

print('Executed successfully')
