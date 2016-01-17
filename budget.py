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
    



