from sqlalchemy import create_engine
from sqlalchemy import (
    Table, Column, Integer, String, MetaData, ForeignKey, Float, insert,
    select, delete
)
import csv
import logging

logger = logging.getLogger( 'iris.db' )


class Iris_db:
    engine_url = 'sqlite:///APTUDE_TEST'

    def __init__( self, *args, **kw ):
        self.engine = create_engine( self.engine_url )
        logger.info( self.engine )
        metadata = MetaData()
        self.iris = Table(
            'IRIS', metadata,
            Column( 'id', Integer, primary_key=True),
            Column( 'species', String ),

            Column( 'sepal_length', Float),
            Column( 'sepal_width', Float),

            Column( 'petal_length', Float),
            Column( 'petal_width', Float),
        )
        metadata.create_all( self.engine )

        self.conn = self.engine.connect()

    def select_all( self ):
        return self.conn.execute( select( [ self.iris ] ) ).fetchall()

    def insert_list( self, data ):
        q = insert( self.iris )
        return self.conn.execute( q, list( data ) )

    def delete( self ):
        q = delete( self.iris )
        return self.conn.execute( q )

