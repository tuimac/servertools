import urllib.request
import traceback

class EC2:
    def __init__(self):
        self.baseurl = "http://169.254.169.254/latest/"
        self.path = {
            "InstanceType": "meta-data/instance-type"
        }

    def query(self, target) -> str:
        try:
            url = self.baseurl + self.path[target]
            response = urllib.request.Request(url)
            with urllib.request.urlopen(response) as data:
                return data.read().decode("ascii")
        except KeyError as e:
            return "Target Error"
        except urllib.error.HTTPError as e:
            return "404 Not Found"
        except:
            traceback.print_exc()
            return "Error"
