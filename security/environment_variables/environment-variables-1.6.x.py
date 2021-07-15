# Download the Python helper library from twilio.com/docs/python/install
import os

from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = os.environ['AC534dccd7e2f3b001233999ce0072b577']
auth_token = os.environ['63574844890836de8ee1a4545a18c152']
client = Client(account_sid, auth_token)

# Make API calls here...
