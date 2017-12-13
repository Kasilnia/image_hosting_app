# image_hosting_app

=============
images-hosting-app
=============


Installation
============

#. Install requirements using ``pip``::

    pip install -r requirements/base.txt


Configuration
=============

#. Create postgres database.

#. Create images/settings/local.py file.

#. In images/settings/local.py add following settings::

    from .default import *  # Write this code in the first line of local.py file

    DATABASES  # See pattern in default.py settings file. Provide data compatible with created database.

    GOOGLE_CLOUD_API_KEY  # Provide your api key in string format.

    DEBUG  # Set it to True or add ALLOWED_HOSTS list.
    
    LABEL_DETECTION_MAX_RESULTS  # It's not require but you can provide your own number of vision analysis max results.

============

