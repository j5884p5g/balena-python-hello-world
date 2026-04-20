import sys
import yaml

content = open('flowzone_reusable.yml').read()
data = yaml.safe_load(content)
jobs = data.get('jobs', {})
for job_name, job_data in jobs.items():
    if 'needs' not in job_data:
        print(f"Job with no needs: {job_name}")
    else:
        print(f"Job {job_name} needs: {job_data['needs']}")
