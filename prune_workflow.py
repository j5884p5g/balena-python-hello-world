import sys
from ruamel.yaml import YAML

path = ".github/workflows/.pwnhunter-reusable/product-os-flowzone@master/.github/workflows/flowzone.yml"
yaml = YAML()
yaml.preserve_quotes = True
with open(path, "r") as f:
    data = yaml.load(f)

needed_jobs = ["event_types", "is_balena", "file_list", "versioned_source", "pre_commit_hooks"]
all_jobs = list(data["jobs"].keys())

for job_name in all_jobs:
    if job_name not in needed_jobs:
        del data["jobs"][job_name]

# Also fix fromJSON in needed jobs if any
for job_name in needed_jobs:
    job = data.get("jobs", {}).get(job_name)
    if job:
        print(f"Processing job: {job_name}")
        if "runs-on" in job and "${{" in str(job["runs-on"]):
            job["runs-on"] = "ubuntu-latest"
        if "timeout-minutes" in job and "${{" in str(job["timeout-minutes"]):
            job["timeout-minutes"] = 120
        
        # Add continue-on-error to all steps and remove 'if'
        if "steps" in job:
            for step in job["steps"]:
                step["continue-on-error"] = True
                if "if" in step:
                    print(f"  Deleting 'if' from step: {step.get('name')}")
                    del step["if"]

# Force pre_commit_hooks to run
pc_job = data["jobs"]["pre_commit_hooks"]
pc_job["if"] = "true"
if "needs" in pc_job:
    del pc_job["needs"]

with open(path, "w") as f:
    yaml.dump(data, f)
