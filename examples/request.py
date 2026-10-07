import json, os, urllib.request
base=os.environ.get('CLAUDE_BASE_URL','https://argolink.io').rstrip('/')
key=os.environ['API_KEY']
body={'model':'claude-opus-5','max_tokens':64,'messages':[{'role':'user','content':'Return one short greeting.'}]}
req=urllib.request.Request(base+'/v1/messages',data=json.dumps(body).encode(),method='POST',headers={'Authorization':'Bearer '+key,'Content-Type':'application/json','anthropic-version':'2023-06-01','User-Agent':'claude-api-archive-guide/1.0'})
with urllib.request.urlopen(req,timeout=60) as response: print(response.read().decode())
