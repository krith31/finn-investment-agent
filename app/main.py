import os, sqlite3, json, re, hashlib
from pathlib import Path
from datetime import datetime, timezone, timedelta
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

ROOT=Path(__file__).resolve().parents[1]
DB=Path(os.getenv('FINN_DB',str(ROOT/'finn.db')))
app=FastAPI(title='FINN intelligence API')
def db():
 c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c
with db() as c:
 c.executescript('CREATE TABLE IF NOT EXISTS settings(id INTEGER PRIMARY KEY,value TEXT); CREATE TABLE IF NOT EXISTS evidence(id TEXT PRIMARY KEY,ticker TEXT,title TEXT,period TEXT,page INTEGER,text TEXT,url TEXT); CREATE TABLE IF NOT EXISTS acknowledgements(id TEXT PRIMARY KEY);')
CATEGORIES=['results','M&A','fund_raise','management_change','litigation','insider_trading','earnings_call','investor_meetings','credit_rating','dividend','bonus_split','capex','press_release','postal_ballot','agm_egm','pledging','unclassified']
NAMES=[('RELIANCE','Reliance Industries','Energy'),('TCS','Tata Consultancy Services','Technology'),('HDFCBANK','HDFC Bank','Banking'),('INFY','Infosys','Technology'),('ITC','ITC','Consumer'),('LT','Larsen & Toubro','Industrials'),('SUNPHARMA','Sun Pharma','Healthcare'),('TATAMOTORS','Tata Motors','Automotive'),('BHARTIARTL','Bharti Airtel','Telecom'),('TITAN','Titan Company','Consumer'),('ULTRACEMCO','UltraTech Cement','Materials'),('NTPC','NTPC','Utilities'),('DIXON','Dixon Technologies','Electronics'),('POLYCAB','Polycab India','Industrials'),('ASTRAL','Astral','Materials'),('CDSL','CDSL','Financial services'),('PERSISTENT','Persistent Systems','Technology'),('INDHOTEL','Indian Hotels','Hospitality'),('WIPRO','Wipro','Technology'),('ASIANPAINT','Asian Paints','Consumer'),('MARUTI','Maruti Suzuki','Automotive'),('DRREDDY','Dr Reddy’s Laboratories','Healthcare')]
COMPANIES=[dict(ticker=t,name=n,sector=s,portfolio=i<18,price=round(500+i*137.3,2),change=[1.2,-.8,2.1,-3.4,.4][i%5],volume=100000*(i+2),average_volume=70000*(i+1),provenance='DEMO — synthetic EOD snapshot',as_of='2026-10-30') for i,(t,n,s) in enumerate(NAMES)]
EVENTS=[dict(id=str(i),ticker=COMPANIES[i]['ticker'],category=cat,title=title,fact=fact,interpretation=why,priority=priority,hours=hours,provenance='DEMO — fictional scenario',source=None) for i,(cat,title,fact,why,priority,hours) in enumerate([
 ('results','Growth deserves a closer look','A results filing is available in this demonstration scenario.','Check whether profit growth converts into operating cash flow.',3,2),
 ('management_change','A leadership transition to investigate','A CFO transition is simulated. No individual or career history is asserted.','Review succession timing and the incoming executive’s verified background.',3,5),
 ('credit_rating','Read beyond the rating headline','A credit-rating review is simulated.','Examine the rationale, liquidity and debt maturities before drawing conclusions.',2,9),
 ('capex','Capacity today. Returns tomorrow?','A capacity expansion announcement is simulated.','Track funding, utilisation assumptions and return on invested capital.',2,12),
 ('investor_meetings','Investor meeting notice','A routine investor meeting notice is simulated.','No operating change is implied by a meeting notice.',0,16),
 ('dividend','Capital return notice','A dividend announcement is simulated.','Verify the record date in the original filing.',1,36)])]
class Settings(BaseModel):
 volume:float=Field(2,ge=1,le=20)
 positive:float=Field(3,gt=0,le=50)
 negative:float=Field(3,gt=0,le=50)
 categories:list[str]=Field(default_factory=lambda:['results','management_change','M&A'])
class Query(BaseModel):
 ticker:str=Field(min_length=1,max_length=30)
 question:str=Field(min_length=3,max_length=2000)
class Evidence(BaseModel):
 ticker:str=Field(pattern=r'^[A-Z0-9&.-]{1,30}$')
 title:str=Field(min_length=3,max_length=200)
 period:str=Field(min_length=2,max_length=50)
 page:int=Field(ge=1)
 text:str=Field(min_length=30,max_length=50000)
 url:str=Field(pattern=r'^https://',max_length=2000)
def settings():
 with db() as c:r=c.execute('SELECT value FROM settings WHERE id=1').fetchone()
 return json.loads(r[0]) if r else Settings().model_dump()
@app.get('/api/portfolio')
def portfolio():return COMPANIES
@app.get('/api/settings')
def get_settings():return dict(**settings(),available_categories=CATEGORIES)
@app.put('/api/settings')
def save_settings(s:Settings):
 if any(x not in CATEGORIES for x in s.categories):raise HTTPException(422,'Unknown category')
 with db() as c:c.execute('INSERT OR REPLACE INTO settings VALUES(1,?)',(s.model_dump_json(),))
 return s
@app.get('/api/digest')
def digest(hours:int=24,category:str='all'):
 if hours not in [24,72,168]:raise HTTPException(422,'Choose 24, 72 or 168 hours')
 with db() as c:ack={r[0] for r in c.execute('SELECT id FROM acknowledgements')}
 return [dict(e,acknowledged=e['id'] in ack) for e in EVENTS if e['hours']<=hours and (category=='all' or e['category']==category)]
@app.post('/api/acknowledge/{id}')
def acknowledge(id:str):
 if id not in {e['id'] for e in EVENTS}:raise HTTPException(404)
 with db() as c:c.execute('INSERT OR IGNORE INTO acknowledgements VALUES(?)',(id,))
 return {'ok':True}
@app.get('/api/alerts')
def alerts():
 s=settings(); out=[]
 for c in COMPANIES:
  if not c['portfolio']:continue
  ratio=c['volume']/c['average_volume']
  if ratio>s['volume']:out.append(dict(ticker=c['ticker'],reason=f'Volume {ratio:.2f}× baseline',kind='CALCULATION',provenance=c['provenance']))
  if c['change']>=s['positive'] or c['change']<=-s['negative']:out.append(dict(ticker=c['ticker'],reason=f"EOD move {c['change']:+.1f}%",kind='FACT',provenance=c['provenance']))
 return out+[dict(ticker=e['ticker'],reason=e['title'],kind='FACT',provenance=e['provenance']) for e in EVENTS if e['category'] in s['categories']]
@app.post('/api/evidence')
def add_evidence(e:Evidence):
 # Human-reviewed primary-source excerpts only. Never silently certify a URL.
 id=hashlib.sha256(e.model_dump_json().encode()).hexdigest()[:20]
 with db() as c:c.execute('INSERT OR REPLACE INTO evidence VALUES(?,?,?,?,?,?,?)',(id,e.ticker,e.title,e.period,e.page,e.text,e.url))
 return {'id':id,'status':'User-supplied primary-source excerpt; authenticity not independently verified'}
@app.get('/api/evidence/{ticker}')
def evidence(ticker:str):
 with db() as c:return [dict(r) for r in c.execute('SELECT * FROM evidence WHERE ticker=?',(ticker.upper(),))]
@app.post('/api/research')
def research(q:Query):
 terms=set(re.findall(r'[a-z]{3,}',q.question.lower()))-{'the','and','what','how','company','does'}
 rows=evidence(q.ticker)
 ranked=sorted([(len(terms & set(re.findall(r'[a-z]{3,}',r['text'].lower()))),r) for r in rows],key=lambda x:x[0],reverse=True)
 hits=[r for score,r in ranked if score>0][:5]
 return {'mode':'Extractive evidence retrieval — no generative model configured','answer':'Relevant primary-source passages are shown below. Interpretation requires analyst review.' if hits else 'Insufficient evidence. Add a relevant annual-report, results or earnings-call excerpt to investigate this question.','citations':hits,'kind':'FACT','warning':'User-supplied excerpts are not independently authenticated.'}
@app.get('/api/health')
def health():return {'status':'ok','mode':'demonstration','market_frequency':'EOD','live_integrations':False}
app.mount('/static',StaticFiles(directory=ROOT/'static'),name='static')
@app.get('/')
def index():return FileResponse(ROOT/'static/index.html')
