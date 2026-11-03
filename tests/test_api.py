import os,tempfile,unittest
os.environ['FINN_DB']=tempfile.mktemp(suffix='.db')
from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
class API(unittest.TestCase):
 def test_portfolio(self):
  rows=client.get('/api/portfolio').json();self.assertEqual(sum(r['portfolio'] for r in rows),18)
 def test_window(self):
  self.assertGreater(len(client.get('/api/digest?hours=72').json()),len(client.get('/api/digest').json()))
  self.assertEqual(client.get('/api/digest?hours=-1').status_code,422)
 def test_settings(self):
  self.assertEqual(client.put('/api/settings',json={'volume':0}).status_code,422)
  self.assertEqual(client.put('/api/settings',json={'volume':3,'positive':4,'negative':4,'categories':['results']}).status_code,200)
  self.assertEqual(client.get('/api/settings').json()['volume'],3)
 def test_grounding(self):
  q={'ticker':'TEST','question':'operating cash flow'}
  self.assertEqual(client.post('/api/research',json=q).json()['citations'],[])
  source={'ticker':'TEST','title':'Test annual report','period':'FY2026','page':12,'text':'Operating cash flow was 100 units in this test document.','url':'https://example.com/report.pdf'}
  client.post('/api/evidence',json=source)
  r=client.post('/api/research',json=q).json();self.assertEqual(r['citations'][0]['page'],12)
  self.assertEqual(client.post('/api/research',json={'ticker':'OTHER','question':q['question']}).json()['citations'],[])
 def test_home(self):self.assertEqual(client.get('/').status_code,200)
 def test_ack(self):self.assertEqual(client.post('/api/acknowledge/0').status_code,200)
if __name__=='__main__':unittest.main()
