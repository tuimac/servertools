import urllib.request
import traceback
import json

class EC2:
    def __init__(self):
        self.baseurl = "http://169.254.169.254/latest/"
        self.path = {
            "InstanceType": "meta-data/instance-type",
            "InstanceIDDocument": "dynamic/instance-identity/document"
        }
        self.response = dict()

    def __queryAll(self) -> dict:
        for target in self.path.keys():
            self.query(target)
        return self.response

    def query(self, target="") -> dict:
        if target == "": return self.__queryAll()
        try:
            url = self.baseurl + self.path[target]
            response = urllib.request.Request(url)
            with urllib.request.urlopen(response) as data:
                body = data.read().decode("ascii")
                try:
                    self.response[target] = json.loads(body)
                    return self.response
                except json.decoder.JSONDecodeError as e:
                    self.response[target] = body
                    return self.response
        except KeyError as e:
            self.response["Error"] = "Query Error"
            return self.response
        except urllib.error.HTTPError as e:
            self.response["Error"] = "404 Not Found"
            return self.response
        except:
            traceback.print_exc()
            self.response["Error"] = "General Error"
            return self.response
