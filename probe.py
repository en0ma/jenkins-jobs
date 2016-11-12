from src.jenkins import Jenkins
from src.job_repository import JobRepository
from datetime import datetime

class Probe(Jenkins, JobRepository):

    def checkJobs(self):
        try:
            jobs = Jenkins.listJobs(self)
            job_title = []
            job_status = []
            checked_at = []
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            for job in jobs:
                #edge case -1
                #newly created jobs that are yet to build
                if job['lastBuild'] is None:
                    job['lastBuild'] = {'result': 'PENDING'}

                #edge- case -2
                #jobs whose execution was terminate due user terminating it manually
                if job['lastBuild']['result'] is None:
                    job['lastBuild']['result'] = 'TERMINATED'

                print 'probing job: '+job['displayName']+ ' having status: '+job['lastBuild']['result']+ ' ....'
                job_title.append(job['displayName'])
                job_status.append(job['lastBuild']['result'])
                checked_at.append(current_time)

            print 'Saving probe results to database....'
            db_data = zip(job_title, job_status, checked_at)
            JobRepository.insert(self, db_data)
            print "Finished probing jobs"
        except Exception as e:
            print 'Opps, something went wrong: ', e

probe = Probe()
probe.checkJobs()
