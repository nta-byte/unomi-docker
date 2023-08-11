import requests

"""
Make a request to Unomi to create a profile with ID = 10
"""
r = requests.get('http://localhost:8182/cxs/profiles/count',
                  auth=('karaf', 'karaf'),
                  )


print(r)
print(r.content)
# r = requests.get('http://localhost:8181/cxs/scopes',
#                   auth=('karaf', 'karaf'),
#                   )
# print(r)
# print(r.content)