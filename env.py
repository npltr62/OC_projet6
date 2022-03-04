import yaml #call yaml module
with open('config.yaml') as f: #parsing yaml config file
    config = yaml.load(f, Loader=yaml.FullLoader)
user= config['vm']['user'] #get value from 'user' key
host= config['vm']['host'] #get value from 'host' key
pwd= config['vm']['pwd'] #get value from 'pwd' key
datestr = config['latest_dump_file']['date'] #get value from 'date' key
syntaxe= config['cron']['syntaxe'] #get value from 'syntaxe' key