import sys
import time
from github import Github
from datetime import datetime, timedelta
today = datetime.today()
thirty_days_ago = today - timedelta(days=30)
yesterday = today - timedelta(days=1)

def delay(dividend, divisor, wait):
    if dividend % divisor == 0:
        print(f"Sleeping for {wait} seconds")
        time.sleep(wait)


token = sys.argv[1]
target_team = sys.argv[2]
WAIT_TIME = int(sys.argv[3])  # Wait this many seconds between dispatch batches
BATCH_SIZE = int(sys.argv[4])  # Pause every N repos
repo_name = sys.argv[5]

g = Github(token)
print(f"Logged in as {g.get_user().name}")

source = None
for team in g.get_user().get_teams():
    if team.name == "iX":
        source = team
if source is None:
    raise ValueError(f"Team {target_team} Not Found")

count = 0
eventType = "staleprworkflow"

for repo in source.get_repos():
    print(repo.name)
    repo.get_commits(since=yesterday)
    

"""for repo in source.get_repos():    
    if not repo_name or repo_name in repo.name:
        repo.create_repository_dispatch(event_type=eventType)
        print(f"Triggered {eventType} for {repo.name}")
        delay(count, BATCH_SIZE, WAIT_TIME)
    count += 1
"""
print("Stale PR Workflow COMPLETE")