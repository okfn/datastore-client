Python library and command line client for the `CKAN DataStore`_.

.. _CKAN DataStore: http://docs.ckan.org/en/latest/datastore.html

API Keys
========

Many operations will need your API key. This can either be set as part of the
url when conducting an operation, e.g.::

  http://{your-api-key}@thedatahub.org/api/data/fffc6388-01bc-44c4-ba0d-b860d93e6c7c'

Or you can set this in a section of your .dpmrc file in your home (~/)
directory::

  [index:{hostname}]
  api_key = {your-api-key}

For example::

  [index:thedatahub.org]
  api_key = adfakjfafdkjda

  [index:localhost]
  api_key = tester


Command Line Usage
==================

For command line usage do::

    ./datastore/client.py -h

Client Usage
============

Example:

  >>> import datastore.client
  >>> data_api = 'http://thedatahub.org/api/data/fffc6388-01bc-44c4-ba0d-b860d93e6c7c'
  >>> client = datastore.client.DataStoreClient(data_api)
  >>> client.update(...)

