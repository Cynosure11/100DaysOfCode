# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
client = Client("c0e36b81040cf2876e344cefb27e984b", "c0e36b81040cf2876e344cefb27e984b")

message = client.messages.create(
                              body='Hi there',
                              from_='+18647635134',
                              to='+15083678279'
                          )

print(message.sid)
