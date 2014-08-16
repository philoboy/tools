import json
from StringIO import StringIO

response = '{"a":"b","c":"d"}'
obj = json.loads(response)
output = StringIO()
json.dump(obj, output, sort_keys=True, indent=2,ensure_ascii=False)
output.seek(0)                                                                                                                                                         
print output.read()
