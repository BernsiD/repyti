# RePyTI 

RESTful Python Teamcenter Interface

This is the attempt to create an OpenSource RESTful Teamcenter Interface.
Communication to Teamcenter is done via Teamcenter Services (SOAP)
Web interface works with Flask, SOA requests made by zeep.

At this stage of development there is only two module available wich allows: 
- to extract of metadata and classification properties
- to extract of existing revision rules

There plans for next modules:
- to extract material information of item revision
- to extract effectivity of item revsion


### REQUIREMENTS:
- Flask
- zeep 
- full list is in `requirements.txt` file


### SETUP:
- Install Flask
- rename `secret.py.example` to `secret.py`
- fill it with your Teamcenter credentials
- run `app.py`

### USAGE:

- **REST:**
    - REST request example is located in powershell_rest_request_example.ps1

- **BROWSER:**
    - Connect to `127.0.0.1:5000` -> Extract Item Information
    - Enter ItemID & RevisionID -> Submit

- **Known Issues:**
    - Very crude ErrorHandling
    - No cloaking of Username / password at the moment



Since this is a non-profit project, updates will take time because i have a full-time job.
Help and contribution would be appreciated. For contact mail to bernsiaut@gmail.com


Have Fun
BernsiD
