from linkedin.linkedin import LinkedInAuthentication, LinkedInApplication
import sys

# ============ Client Application Credentials ============ #
# Can be found here: https://www.linkedin.com/developer/apps

CLIENT_ID = None
CLIENT_SECRET = None
PORT = 80

# ============ Authorization Code ============ #
# If not used, please set its value to: None
AUTH_CODE = None
# AUTH_CODE     = "##############################################################################################################################################################"

# Set it correctly or assign it to: None
AUTH_TOKEN = None


# AUTH_TOKEN    = '###################################################################################################################################################################################'

class LinkedInWrapper(object):

    def __init__(self, id, secret, auth_token=None, auth_code=None):
        self.id = id
        self.secret = secret

        self.callback_url = 'http://localhost/linkedinapi/'

        print("CLIENT ID: %s" % self.id)
        print("CLIENT SECRET: %s" % self.secret)
        print("Callback URL: %s" % self.callback_url)

        if auth_token is None:

            self.authentication = LinkedInAuthentication(
                self.id,
                self.secret,
                self.callback_url,

                permissions=['r_basicprofile', 'r_emailaddress', 'rw_company_admin', 'w_share']
            )

            if auth_code is None:
                print("Please open this address in your browser in order to obtain the authorization_code\n\n")
                print(self.authentication.authorization_url)

                print(
                    "\n\nIn case of error, please double check that the callback URL has been correctly added in the developer console: https://www.linkedin.com/developer/apps/")
                sys.exit()

            else:
                self.authentication.authorization_code = auth_code
                result = self.authentication.get_access_token()

                print("\n\nAccess Token:", result.access_token)
                print("Expires in (seconds):", result.expires_in)
                sys.exit()

        else:
            print()
            self.application = LinkedInApplication(token=auth_token)


lkin_api = LinkedInWrapper(CLIENT_ID, CLIENT_SECRET, PORT, auth_token=AUTH_TOKEN, auth_code=AUTH_CODE)

print("Getting your profile information...")
print(lkin_api.application.get_profile())
