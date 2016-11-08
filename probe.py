from src/jenkins import Jenkins
from src/job_repository import JobRepository
import time

class Probe(object):

    def checkJobs(self):
        try:
            jobs = Jenkins.listJobs()
            job_title = []
            job_status = []
            checked_at = []
            timestamp = time.now()

            for job in jobs:
                job_title.append(job['title'])
                job_status.append(job['status'])
                checked_at.append(timestamp)

            db_data = zip(job_title, job_status, checked_at)
            JobRepository.insert(db_data)

        except Exception as e:
            raise

probe = new Probe()
probe.checkJobs()
