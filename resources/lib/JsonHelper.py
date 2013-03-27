import simplejson as json
import urllib, urllib2

class JsonHelper:

    def callMethod(self, serverParameter, method, queries={}):
        url = self.getRestUrl(serverParameter, method, queries)
        try:
            response = urllib2.urlopen(url)
            try:
                json_response = json.loads(response.read())
            except ValueError:
                print("Error parsing json")
                return False
        except urllib2.URLError,e:
            print("Error calling method: " + str(e))
            return False
        
        payload = json_response.get('subsonic-response', None)
        return payload

    def getRestUrl(self, serverParameter, method, queries):
        queries.update({'v': serverParameter['apiVersion'],
                        'c': serverParameter['clientName'],
                        'u': serverParameter['user'],
                        'p': serverParameter['password'],
                        'f': 'json'})
        query = '&'.join([k+'='+urllib.quote(str(v)) for (k,v) in queries.items()])

        url = '%s/rest/%s?%s' %  (serverParameter['server'], method, query)

        return url

