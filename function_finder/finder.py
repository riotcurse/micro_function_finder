import argparse
import re
from itertools import groupby

parser = argparse.ArgumentParser(description='Get file name')
parser.add_argument('filename')
args = parser.parse_args()

filename = args.filename

r = re.compile(':   [a-f0-9 ]*   ')

lines = []

with open(filename) as f:
    outfile = name_outfile(filename)

    thing = '\n'
    while thing != '':
        thing = f.readline()
        try:
            result = r.search(thing).group(0)
        except:
            result = ''
        lines.append(result[1:].strip())

    text = stupid_thing(lines)

    functions = split_by_op('3041',text)

    with open(outfile, 'w') as w:
         for line in lines:
             w.write(line + '\n')

def split_by_op(op,code):
    groups = groupby(code,lambda x: x == op)
    funcs = [list(group) for k, group in groups if not k]
    return [' '.join(thing.append(op)) for thing in funcs]

def name_outfile(infilename):
    outfile = infilename.split('.')
    outfile[0] = outfile[0] + "_out"
    return '.'.join(outfile)

#split lines of space-separated text into an array of individual
#items
def stupid_thing(lines):
    return ' '.join(lines).split(' ')
