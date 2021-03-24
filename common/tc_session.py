import sys
import requests


class TC_Session():
    def __init__(self, username, password, serveradress="http://myserver01:8480", sessiontoken=None): #Enter your serveradress here
        self.username = username
        self.password = password
        self.serveradress = serveradress

    # Login to Teamcenter

    def login(self):

        url = f"{self.serveradress}/tc/services/Core-2006-03-Session?wsdl"
        headers = {'Content-Type': 'text/xml', 'SOAPAction': 'login'}
        body = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ses="http://teamcenter.com/Schemas/Core/2006-03/Session">
    <soapenv:Header/>
    <soapenv:Body>
    <ses:LoginInput username="{self.username}" password="{self.password}" group="" role="" sessionDiscriminator="1i52"/>
    </soapenv:Body>
    </soapenv:Envelope>"""

        response = requests.post(url, data=body, headers=headers, verify=False)

        if response.status_code == 200:
            print('Command Login successful.')
            print(response.cookies)
        else:
            print('Command Login failed.')
            sys.exit('Command Login operation failed with HTTP Code ' +
                     str(response.status_code))

        login_session_id = None
        #Get Session Id wether its ASP.NET or J2EE
        for cookie in response.cookies:
            if cookie.name == 'ASP.NET_SessionId':
                login_session_id = cookie.value
                token_name = cookie.name
            elif cookie.name == 'JSESSIONID':
                login_session_id = cookie.value
                token_name = cookie.name

        session_token = token_name + "=" + str(login_session_id)
        print(session_token)
        self.session_token = session_token
        return session_token

    def logout(self):
        #  Logout from Teamcenter
        # ---------------------------------
        url = f"{self.serveradress}/tc/services/Core-2006-03-Session?wsdl"
        headers = {'Content-Type': 'text/xml',
                   'SOAPAction': 'logout', 'Cookie': self.session_token}
        body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ses="http://teamcenter.com/Schemas/Core/2006-03/Session">
    <soapenv:Header/>
    <soapenv:Body>
    <ses:LogoutInput/>
    </soapenv:Body>
    </soapenv:Envelope>"""
        response = requests.post(url, data=body, headers=headers, verify=False)

        if response.status_code == 200:
            print('Command Logout successful.')
            # print(response.content)
        else:
            print('Command Logout failed.')
            sys.exit('Command Logout failed with HTTP Code ' +
                     str(response.status_code))


if __name__ == "__main__":
    main()
