import csv,re,sys,statistics as st,collections
rows=list(csv.DictReader(open(sys.argv[1],newline='',encoding='utf-8')))
print("rows",len(rows),"columns",len(rows[0]))
dm=[r for r in rows]
nocap=lambda t: bool(re.match(r'\s*(No statutory cap|No statewide cap|No cap|No limit)',t,re.I))
n=[r['code'] for r in rows if nocap(r['deposit_max'])]
print("deposit_max begins with 'No ... cap' (no cap found):",len(n),sorted(n))
blank=[r['code'] for r in rows if not r['deposit_max'].strip()]
print("deposit_max blank:",blank)
d=[int(r['deposit_return_deadline_days']) for r in rows if re.fullmatch(r'\d+',r['deposit_return_deadline_days'])]
print("deadline n",len(d),"median",st.median(d),"min",min(d),"max",max(d))
print("deadline distribution",sorted(collections.Counter(d).items()))
print("itemization",collections.Counter(r['deposit_itemization_required'] for r in rows))
ri=lambda t:t.lower().startswith('yes')
y=[r['code'] for r in rows if ri(r['deposit_interest'])]
print("deposit_interest begins 'Yes':",len(y),sorted(y))
print("deposit_interest blank:",sum(1 for r in rows if not r['deposit_interest'].strip()))
rc=[r['code'] for r in rows if ri(r['rent_increase_statewide_rent_control'])]
print("statewide rent control text begins 'Yes':",len(rc),sorted(rc))
print("rent_increase_statewide_rent_control blank:",sum(1 for r in rows if not r['rent_increase_statewide_rent_control'].strip()))
print("rent_increase_notice blank:",sum(1 for r in rows if not r['rent_increase_notice'].strip()))
print("late_fee_rule blank:",[r['code'] for r in rows if not r['late_fee_rule'].strip()])
print("retaliation_rule blank:",sum(1 for r in rows if not r['retaliation_rule'].strip()))
print("sourced statute URL on all six topics:",sum(1 for r in rows if all(r[t+'_source_url'] for t in ['deposit','late_fee','entry','month_to_month','rent_increase','retaliation'])))
