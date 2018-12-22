import jinja2
import os
import json
from jinja2 import Environment, FileSystemLoader
 
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('template.html')  

with open('/home/jim/Desktop/html/dist/assets/json/events.json') as f:
    data = json.load(f)

event_list = data['events']

#
# items = []
# for event in event_list:
#     i = str(i)
#
#     # dict == {}
#     # you just don't have to quote the keys
#     an_item = dict(date="2012-02-" + i, id=i, position="here", status="waiting")
#     items.append(an_item)

print(template.render(events=event_list))
filename = '/home/jim/Desktop/html/dist/events_jinja2.html' #os.path.join(root, 'html', 'index.html')
with open(filename, 'w') as fh:
	fh.write(template.render(events=event_list))
