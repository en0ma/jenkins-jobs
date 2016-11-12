import json
import requests

class Jenkins(object):
    uri = "http://deadlock.netbeans.org/hudson/api/json?depth=1&tree=jobs[displayName,lastBuild[result]]"

    def listJobs(self):
        response = json.loads(requests.get(self.uri).text)

        if response.has_key('jobs') and len(response['jobs']) > 0:
            return response['jobs']
        raise Exception('No jobs found.')
