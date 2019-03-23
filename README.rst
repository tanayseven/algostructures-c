.. image:: https://travis-ci.org/tanayseven/algostructures.svg?branch=master
    :target: https://travis-ci.org/tanayseven/algostructures


AlgoStructures
==============

A collection of algorithms and datastructures which are written in C and Haskell
--------------------------------------------------------------------------------

Setting up and using
====================

Prerequisites for Mac OSX
-------------------------

* Docker

Prerequisites for Linux
-----------------------

* Latest version of GCC

Usage Instructions for Mac OSX
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    docker build -t algostructures_test .    # Build the image that can run the tests

    docker run -it --rm --name algostructures_test algostructures_test      # Run the tests in the container

Usage Instructions for Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    make clean build   # Build all the necessary binaries for running 

    make test          # Run the tests binary that is in bin/ directory
