# Docker runner for XLS 2 CSV convertor
import yaml
import xlsx2csv

stream = open("/var/shared/config/config.yaml", 'r')
config = yaml.load(stream);
path_config = config['path'];
xlsx2csv.convert_recursive(path_config['input'], 0, path_config['output'], {});