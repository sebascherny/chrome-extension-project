# chrome-extension-project

## Extension installation

To install the extension, follow the steps at https://developer.chrome.com/docs/extensions/get-started?hl=es-419 , selecting this folder `chrome-extension-project` as the extension folder.

## Backend communication

The extension uses two endpoints:

- POST to /log-event : Sends to the backend the information about different events: when the notification is displayed, and when the user either dismisses it or acknowledges it.

- POST to /get-notification : Gets the notification's HTML content to display depending on the url that the tab is on.


## Backend service

Running these commands will start the service in 127.0.0.1:8001 , which is the location that the extension's code contemplates for doing the backend communication.
It will create a db.sqlite3 file which works as a local, simple database.


```
cd notification_project/
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8001
```

## Using the extension

Navigate to one of the desired web pages (https://www.hilton.com, https://www.flytap.com, https://www.fctgl.com) and check that a notification is displayed at the top right of the page.

The notification in www.hilton.com is the most similar to the one given in the PDF requirements.

## Django Admin

First, create an admin user running `python manage.py createsuperuser` in a console after following the first steps as above.
You can check locally the Django Admin (http://127.0.0.1:8001/admin/) and see the events there, or check the `events.log` file.