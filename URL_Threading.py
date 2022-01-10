import queue
import threading
import urllib.request

# called by each thread
def get_url(q, url):
    q.put(urllib.request.urlopen(url).read())

theurls = ["http://google.com", "http://yahoo.com"]

q = queue.Queue()

for u in theurls:
    t = threading.Thread(target=get_url, args = (q,u))
    t.daemon = True
    t.start()

s = q.get()
print (s)

##
##import urllib.request
##url = "http://www.google.com/"
##request = urllib.request.Request(url)
##response = urllib.request.urlopen(request)
##print (response.read().decode('utf-8'))
