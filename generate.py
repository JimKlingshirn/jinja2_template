import jinja2
import os
import json
from jinja2 import Environment, FileSystemLoader
 
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('template.html')  

with open('events.json') as f:
    data = json.load(f)

event_list = data['events']
news_list = data['news']

print(template.render(news=news_list, events=event_list))

filename = '/home/jim/Desktop/html/dist/news-and-events.html' #os.path.join(root, 'html', 'index.html')
with open(filename, 'w') as fh:
	fh.write(template.render(news=news_list, events=event_list))
