from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

import requests


def fetch_data(username, token):
    """Fetches data from GitHub.

    :param str username: GitHub username
    :param str token: Access token
    :return:
    """

    def get(url):
        response = requests.get(url, auth=(username, token))
        return response.json()

    status_warning = 'warning'
    status_danger = 'danger'

    def process_repo(repo):

        def contribute_to_relevant_issues():
            relevant_issues.append({
                'id': issue_id,
                'number': issue_number,
                'title': issue_title,
                'url': issue_url,
                'date': datetime.strptime(issue_date.rstrip('Z'), '%Y-%m-%dT%H:%M:%S'),
                'status': issue_status,
                'hint': issue_hint,
                'comment': issue_comment,
                'tags': issue_tags,
            })

        if not repo['open_issues_count']:
            return

        if repo['fork']:
            return

        relevant_issues = []

        url_issues = '%s?state=open&per_page=100' % repo['issues_url'].replace('{/number}', '')
        for issue in get(url_issues):
            issue_id = issue['number']
            issue_number = issue['number']
            issue_title = issue['title']
            issue_url = issue['html_url']
            issue_date = issue['updated_at']
            issue_status = status_danger
            issue_comment = ''
            issue_tags = [
                {'color': label['color'], 'name': label['name']}
                for label in issue['labels']]

            if not issue['comments']:
                issue_hint = 'Issue has not comments. Please comment on it.'
                contribute_to_relevant_issues()
                continue

            comments = get('%s?per_page=100' % issue['comments_url'])

            relevant_comment = comments[-1]
            commenter = relevant_comment['user']['login']

            if commenter == username:
                issue_hint = 'You\'re the last commenter. Please review the issue.'
                issue_status = status_warning
            else:
                issue_hint = 'You\'re not the last commenter. Dialogue awaits for your answer.'

            issue_date = relevant_comment['updated_at']
            issue_comment = relevant_comment['body']
            contribute_to_relevant_issues()

        result = {
            'id': repo['id'],
            'name': repo['name'],
            'issues': relevant_issues
        }

        return result

    url_repos = 'https://api.github.com/users/%s/repos' % username
    repos = get(url_repos)

    with ThreadPoolExecutor(max_workers=6) as executor:
        results = [repo_data for repo_data in executor.map(process_repo, repos) if repo_data]

    return results
