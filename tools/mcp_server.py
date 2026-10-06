"""Read-only MCP 2025-06-18 stdio adapter. No executable tools."""
import json
import re
import sys

from .cli import ROOT, catalog, inside, read, resolve

TOOLS = [
    {'name':'catalog','description':'List Minecraft skills without loading instructions.',
     'inputSchema':{'type':'object','properties':{},'additionalProperties':False}},
    {'name':'skill','description':'Read a named canonical skill document from trusted checkout.',
     'inputSchema':{'type':'object','properties':{
         'name':{'type':'string','pattern':'^[a-z0-9]+(?:-[a-z0-9]+)*$'},
         'document':{'type':'string','enum':['SKILL.md','REFERENCE.md','contract.json']}},
         'required':['name','document'],'additionalProperties':False}},
    {'name':'resolve','description':'Resolve documented exact-version facts; never certifies APIs.',
     'inputSchema':{'type':'object','properties':{'context':read(ROOT/'schemas/project.schema.json')},
                    'required':['context'],'additionalProperties':False}},
]
for tool in TOOLS:
    tool['annotations']={'readOnlyHint':True,'destructiveHint':False,'idempotentHint':True,'openWorldHint':False}


def call(name, args):
    from .cli import schema_check
    tool = next((t for t in TOOLS if t['name']==name),None)
    if tool is None:
        raise ValueError('Unknown tool')
    schema_check(args,tool['inputSchema'])
    if name=='catalog':
        return json.dumps(catalog(ROOT),indent=2)
    if name=='resolve':
        return json.dumps(resolve(args['context'],ROOT),indent=2)
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',args['name']):
        raise ValueError('Invalid skill name')
    row = next((x for x in catalog(ROOT)['skills'] if x['name']==args['name']),None)
    if row is None:
        raise ValueError('Unknown skill')
    return inside(ROOT,ROOT/row['path']/args['document']).read_text(encoding='utf-8')


def main():
    initialized = False
    ready = False
    limit = 1024*1024
    for line in iter(lambda:sys.stdin.buffer.readline(limit+1),b''):
        if len(line)>limit:
            print('Inbound MCP message exceeds limit.',file=sys.stderr)
            return 1
        ident = None
        notification = False
        try:
            message = json.loads(line)
            if not isinstance(message,dict) or message.get('jsonrpc')!='2.0' or not isinstance(message.get('method'),str):
                raise ValueError('Invalid JSON-RPC request')
            ident = message.get('id')
            notification = 'id' not in message
            if not notification and (isinstance(ident,bool) or not isinstance(ident,(int,str))):
                raise ValueError('Invalid request ID')
            method = message['method']
            params = message.get('params',{})
            if not isinstance(params,dict):
                raise ValueError('Invalid params')
            if notification:
                if method=='notifications/initialized' and initialized:
                    ready=True
                continue
            if method=='initialize':
                if initialized or not isinstance(params.get('protocolVersion'),str):
                    raise ValueError('Invalid initialization')
                initialized=True
                result={'protocolVersion':'2025-06-18','capabilities':{'tools':{'listChanged':False}},
                        'serverInfo':{'name':'minecraft-agent-skills','version':'1.0.0'}}
            elif method=='ping':
                result={}
            elif not ready:
                raise ValueError('Initialization not complete')
            elif method=='tools/list':
                result={'tools':TOOLS}
            elif method=='tools/call':
                try:
                    value=call(params.get('name'),params.get('arguments',{}))
                    result={'content':[{'type':'text','text':value}],'isError':False}
                except (ValueError,KeyError,OSError,TypeError) as error:
                    result={'content':[{'type':'text','text':str(error)}],'isError':True}
            else:
                reply={'jsonrpc':'2.0','id':ident,'error':{'code':-32601,'message':'Method not found'}}
                print(json.dumps(reply),flush=True)
                continue
            reply={'jsonrpc':'2.0','id':ident,'result':result}
        except (ValueError,KeyError,TypeError) as error:
            if notification:
                continue
            reply={'jsonrpc':'2.0','id':ident,'error':{'code':-32700 if isinstance(error,json.JSONDecodeError) else -32600,'message':str(error)}}
        print(json.dumps(reply),flush=True)
    return 0


if __name__=='__main__':
    raise SystemExit(main())
