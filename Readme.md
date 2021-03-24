RePyTI - RESTful Python Teamcenter Interface

This is the attempt to create an OpenSource RESTful Teamcenter Interface.
It works with Flask at the moment.
At this stage of develepmont there is only one module available to allow extraction of metadata and classification properties
of an ItemRevision and CustomItemRevisions by inputting ItemID and RevisionID.

REQUIREMENTS:
Flask

SETUP:
Install Flask
In /common/tc_session.py enter your Teamcenter Server adress
In /modules/extract_item_properties enter your Teamcenter credentials
run app.py

USAGE:
REST:
REST request example is located in powershell_rest_request_example.ps1

BROWSER:
Connect to 127.0.0.1:5000 -> Extract Item Information
Enter ItemID & RevisionID -> Submit

Known Issues:
-Very crude ErrorHandling
-No cloaking of Username / password at the moment


Since this is a non-profit project, updates will take time because i have a full-time job.
Help and contribution would be appreciated.

Have Fun
Bernhard
