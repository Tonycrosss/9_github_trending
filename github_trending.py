import requests
import datetime

for_a_week = (datetime.datetime.today() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')


def get_trending_repositories():
    response = requests.get('https://api.github.com/search/repositories?'
                            'q=created:>={}&sort=stars'
                            '&order=desc'.format(for_a_week))
    all_repos = response.json()
    return all_repos


def get_top_20(repos):
    top_20_repos = repos['items'][0:21]
    return top_20_repos


def get_open_issues_amount(repo_owner, repo_name):
    pass


if __name__ == '__main__':
    get_trending_repositories()
