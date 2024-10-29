from atlassian import Jira
import config
import json

from configuration.read_config import read_config

# print('JIRA CONFIG FILE?:')
# print(jira)
# cfg = config.Config('configuration/jira.cfg')
# print(cfg.__repr__())
# print('=== DICT ===')
# print(cfg['username'])



def connect_with_username_and_password():
    params = read_config()
    jira = Jira(
        url=params['url'],
        username=params['username'],
        password=params['password'],
        cloud=True
    )
    return jira

# For server version only, Cloud edition doens't have PAT
def connect_with_personal_access_token():
    # [jiraURL]/secure/ViewProfile.jspa?selectedTab=com.atlassian.pats.pats-plugin:jira-user-personal-access-tokens
    params = read_config()
    jira_access_token = params['token'] # "NTE4MDc5MzU0Njk4OuypuPOv8L/8M+1gsWCNmvr6b2Ap"
    jira = Jira(
        url=params['url'],
        token=jira_access_token
    )
    return jira

def connect_with_api_key(url, username, token):
    # Create a token using this link (then log-in with your Atlassian Account)
    # https://id.atlassian.com/manage-profile/security/api-tokens
    jira = Jira(
        url,
        username,
        password=token,
        cloud=False
    )
    return jira

# TODO: Remove?
def step_two():

    # Step 2 -- Print out projects
    jira = connect_with_personal_access_token()
    projects = jira.get_all_projects()

    def output_id_name(proj):
        return [ proj['id'], proj['name'] ]

    proj_info = map(output_id_name, projects)

    for p in proj_info:
        print(p)

    projects = jira.get_all_projects()

# step_two()

def connect_to_jira():
    params = read_config()
    jira = connect_with_api_key(params['url'], params['username'], params['token'])
    return jira


# output to a site
# export to Excel / CSV

