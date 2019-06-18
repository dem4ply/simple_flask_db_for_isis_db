=======
the csv
=======

in this example is assuming the csv always if going to have the next headers
sepal_length, sepal_width, petal_length, petal_width, species and if have
one empty column is going to be used like the id of the record

===================
the command iris.py
===================

the next example is going to insert all the records in the csv
.. code-block:: shell
	./iris.py -i iris.csv

the next example is going to delete all the records
before insert the csv in the database
.. code-block:: shell
	./iris.py -i iris.csv -d true

the next example is going to ignore the ids have the csv and add all the records
.. code-block:: shell
	./iris.py -i iris.csv --ignore_pk true

========================
how to run the flask app
========================

.. code-block:: shell
	FLASK_APP=app.py flask run

after start the develop serve you can enter in you browser `http://127.0.0.1:5000/`
for see the web page for upload the csv

when is upload the csv is the equivalent to use the next command
.. code-block:: shell
	./iris.py -i iris.csv --ignore_pk true
