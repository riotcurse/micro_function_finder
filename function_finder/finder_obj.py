import argparse
import re
from itertools import groupby

class FunctionFinder:
    def __init__(self,filename):
        self.filename = filename
        self._regex = re.compile(':   [a-f0-9 ]*   ')

    def set_re(self,regex):
        self._regex = re.compile(regex)

    def read_file(self,size=-1):
        with open(self.filename) as f:
            self._raw = f.read(size)

    def search_file(self):
        raw_matches = self._regex.findall(self._raw)
        self._matches = [thing[1:].strip() for thing in raw_matches]

    def _stupid_thing(self):
        self._text = ' '.join(self._matches).split(' ')

    def _split_by_op(self,op):
        groups = groupby(self._text,lambda x: x == op)
        lists = [list(group) for k, group in groups if not k]
        self.funcs = [' '.join(thing + [op]) for thing in lists]

    def write_out(self):
        outfile = self.filename.split('.')
        outfile[0] = outfile[0] + "_out"
        outfilename = '.'.join(outfile)
        with open(outfilename, 'w') as w:
             for func in self.funcs:
                 w.write(func + '\n')

    def find_functions(self):
        self.read_file()
        self.search_file()
        self._stupid_thing()
        self._split_by_op('3041')
        self.write_out()


def main():
    thing = FunctionFinder(get_args())
    thing.find_functions()

def get_args():
    parser = argparse.ArgumentParser(description='Get file name')
    parser.add_argument('filename')
    args = parser.parse_args()
    return args.filename


if __name__ == '__main__':
    main()
