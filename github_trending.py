import requests
import datetime


def get_trending_repositories():
    weekly = (datetime.datetime.today()
              - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    search_params = {'q': 'created:>={}'.format(weekly),
                     'sort': 'stars', 'order': 'desc'}
    response = requests.get('https://api.github.com/search/repositories',
                            params=search_params)
    all_repos = response.json()
    return all_repos


def get_top(repos, quantity):
    top_repos = repos['items'][:quantity - 1]
    return top_repos


def print_data_from_repos(repos):
    for repo in repos:
        print('Название репозитория: ' + '{}'.format(repo['name']))
        print('Количество открытых issues: ' + '{}'.format(
                                                    repo['open_issues_count']))
        print('Ссылка на репозиторий: ' + '{}'.format(repo['html_url']))
        print('-' * 80)


if __name__ == '__main__':
    trending_repos = get_trending_repositories()
    repos_quantity = 20
    top_repos = get_top(trending_repos, repos_quantity)
    print_data_from_repos(top_repos)
