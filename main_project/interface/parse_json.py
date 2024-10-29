""" Methods to handle the complex metadata objects returned by Jira API """

def get_issue_type(issue):
    """Strips issue type (string) from an issue object

    Args:
        issue (object): Issue object from Jira API

    Returns:
        string: name of issue type
    """
    print(issue)
    return issue["fields"]["issuetype"]["name"]


def get_issue_key(issue):
    """Strips issue key (string) from an issue object

    Args:
        issue (object): Issue object from Jira API

    Returns:
        string: issue key
    """
    return issue["key"]

def get_summary(issue):
    """Strips summary from issue object

    Args:
        issue (object): Issue object from Jira API

    Returns:
        string: summary for given issue
    """
    return issue["fields"]["summary"]

def get_status(issue):
    """Strips status from issue object

    Args:
        issue (object): Issue object from Jira API

    Returns:
        string: status name for given issue
    """
    status = issue["fields"]["status"]["name"]
    return status


# def get_sprint_link(issue):
#     """Strips sprint link from issue object

#     Args:
#         issue (object): Issue object from Jira API

#     Returns:
#         string: sprint link for given issue
#     """
#     if issue["fields"]["customfield_10004"]:
#         customfield = issue["fields"]["customfield_10004"]
#         customfield_split = customfield[0].split(",")[3]
#         sprint_name_field = customfield_split.split("=")[1]

#         return sprint_name_field
#     return "-"
