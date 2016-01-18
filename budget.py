import os
import sys
import logging
import argparse
try:
    from backend import Budget, Produto
except ImportError:
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    from backend import Budget, Produto







if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manipulate the budget.csv table')
    parser.add_argument('--add', '-a', help='add new product to the table', nargs='+')
    parser.add_argument('--show', 's', help='show information')
    args = parser.parse_args()





