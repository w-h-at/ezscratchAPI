import urllib.request
messageCount1 = urllib.request.urlopen("https://api.scratch.mit.edu/users/putusernamehere/messages/count").read()
print(messageCount1)