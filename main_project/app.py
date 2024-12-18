""" Main entry point for Flask application, with endpoints defined """
import json
import sys
sys.path.append('/configuration')
sys.path.append('/output')
sys.path.append('/interface')
sys.path.append('/tests')
sys.path.append('/templates')

from output.create_html import build_html_table
from output.create_spreadsheet import create_spreadsheet
from interface.get_issue_types import get_issue_types
from flask import Flask, render_template
import config
cfg = config.Config('configuration/jira.cfg')

app = Flask(__name__)


# keep
@app.route("/")
def home():
    """Creates entry endpoint, displays search form(s)
    """
    return render_template(
        "index.html",
        issuetypes=json.dumps(get_issue_types()),
    )

# SET UP ROUTES
@app.route("/test")
def test():
    """Test endpoint
    """
    return "Flask is running!"

@app.route("/testtable")
def testtable():
    """Test endpoint
    """
    return render_template("sample_table.html")

@app.route("/results/<issuetype>", defaults={'do_export': False})
@app.route("/results/<issuetype>/<do_export>")
def results(issuetype=None, status=None, do_export=False):
    """Creates endpoint for showing issues from search in HTML table format
        or, if do_export is True, creates spreadsheet and returns it
    """
    print(do_export)
    if do_export == 'export':
        return create_spreadsheet(issuetype)
    else:
        results_table = build_html_table(issuetype)
        export_url="/results/"+issuetype+"/export"
        return render_template("results.html", results_table=results_table, export_url=export_url)
    
if __name__ == "__main__":
    app.run(port=5000, debug=True)
