# Docker runner for XLS 2 CSV convertor
import yaml
import simple_convert
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", "--data", dest="data",
                  help="write report to FILE", metavar="DATA")

(options, args) = parser.parse_args()



in_path = options.data + 'in/files/';
out_path = options.data + 'out/tables/';
stream = open(options.data + "config.yml", 'r')
config = yaml.load(stream)

if config["parameters"]["bucket"]:
	name_prefix = config["parameters"]["bucket"]
else:
	raise Exception('Config parameters.bucket is not set')

convertor = simple_convert.Convertor()
convertor.convert(in_path, out_path, name_prefix)