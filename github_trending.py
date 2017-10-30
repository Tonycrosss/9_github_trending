import requests
import datetime


def get_trending_repositories(quantity):
    weekly = (datetime.datetime.today()
              - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    search_params = {'q': 'created:>={}'.format(weekly),
                     'sort': 'stars', 'order': 'desc'}
    response = requests.get('https://api.github.com/search/repositories',
                            params=search_params)
    all_repos = response.json()
    trending_repos = all_repos['items'][:quantity - 1]
    return trending_repos


def print_data_from_repos(repos):
    for repo in repos:
        repo_name = repo['name']
        repo_owner = repo['owner']['login']
        repo_issues_quantity = get_repo_issue_quantity(repo_owner, repo_name)
        print('Название репозитория: {}'.format(repo_name))
        print('Имя владельца репозитория: {}'.format(repo_owner))
        print('Количество открытых issues: {}'.format(repo_issues_quantity))
        print('Ссылка на репозиторий: {}'.format(repo['html_url']))
        print('-' * 80)


def get_repo_issue_quantity(repo_owner, repo_name):
    response = requests.get('https://api.github.com/repos/{}/{}/issues'.format(
                                                        repo_owner, repo_name))
    issues_data = response.json()
    issues_quantity = len(issues_data)
    return issues_quantity


if __name__ == '__main__':
    repos_quantity = 20
    trending_repos = get_trending_repositories(repos_quantity)
    print_data_from_repos(trending_repos)
