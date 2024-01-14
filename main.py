from lisp_parser import LispParser

parser = LispParser('(first (list 1 (+ 2 3) 9))')
print(parser.as_list())