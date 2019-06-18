#!/usr/bin/env python3
import csv
import itertools
from argparse import ArgumentParser

from db import Iris_db


def chunks( iterable, size=50 ):
    """
    Make digestible chunks of something that can be iterated

    Arguments
    ---------
    iterable: list, tuple, generator
        Just have to support the iter function will break it
        in digestible chunks
    size: size of the digestibles chunks

    Examples
    --------
    >>> [ list( chunk ) for chunk in chunks( range( 10 ), size=5 ) ]
    [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
    """
    iterator = iter( iterable )
    for i in iterator:
        yield itertools.chain( [i], itertools.islice( iterator, size - 1 ) )


parser = ArgumentParser()
parser.add_argument(
    "-i", "--iris", dest="iris",
    help="path of iris.csv" )

parser.add_argument(
    "-d", "--delete_db", dest="delete", default=False,
    help="if true is going to delete the iris table" )

parser.add_argument(
    "--ignore_pk", dest="ignore_pk", default=False,
    help="if is true is going to ignore the id in the csv" )


def insert_from_file( file_name, ignore_pks=False ):
    db = Iris_db()
    rows = csv.DictReader( open( file_name ) )
    x = []
    for row in rows:
        pk = row.pop( '', None )
        if pk:
            row[ 'id' ] = pk
        x.append( row )
        if ignore_pks:
            row.pop( 'id', None )
    for chunk in chunks( x ):
        db.insert_list( chunk )

if __name__ == '__main__':
    args = parser.parse_args()
    if args.iris is None:
        parser.print_help()

    db = Iris_db()

    if args.delete:
        db.delete()

    insert_from_file( args.iris, ignore_pks=args.ignore_pk )

    # print( db.select_all() )
