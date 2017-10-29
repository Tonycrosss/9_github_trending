import requests
import datetime

for_a_week = (datetime.datetime.today() - datetime.timedelta(days=7)).strftime(
                                                                    '%Y-%m-%d')


def get_trending_repositories():
    search_params = {'q': 'created:>={}'.format(for_a_week),
                     'sort': 'stars', 'order': 'desc'}
    response = requests.get('https://api.github.com/search/repositories',
                            params=search_params)
    all_repos = response.json()
    return all_repos


def get_top_20(repos):
    top_20_repos = repos['items'][:21]
    return top_20_repos


def print_data_from_repos(repos):
    for repo in repos:
        print('Название репозитория: ' + '{}'.format(repo['name']))
        print('Количество открытых issues: ' + '{}'.format(
                                                    repo['open_issues_count']))
        print('Ссылка на репозиторий: ' + '{}'.format(repo['html_url']))
        print('-' * 80)


if __name__ == '__main__':
    top_repos = get_trending_repositories()
    top_20 = get_top_20(top_repos)
    print_data_from_repos(top_20)
