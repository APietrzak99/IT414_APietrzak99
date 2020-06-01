from twilio.rest import Client

accountID = "ACcec8af6098cfe935fd65582b9cde4e12"
authToken = "9a0a47762972e26f1b7c9da832c0e5ad"
trialNumber = "+12058512860" # number must be prefixed with a +1, e.g. +12058512860
cellNumber = "+15862462296" # use same number format as above

twClient = Client(accountID, authToken)

my_message = twClient.messages.create(body="Hi Anthony", from_=trialNumber, to=cellNumber)

print (my_message.sid)