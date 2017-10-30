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
        print('Название репозитория: {}'.format(repo['repo_name']))
        print('Имя владельца репозитория: {}'.format(repo['repo_owner']))
        print('Количество открытых issues: {}'.format(
            repo['repo_issues_quantity']))
        print('Ссылка на репозиторий: {}'.format(repo['repo_html_url']))
        print('-' * 80)


def get_repo_clean_info(repos):
    clean_repo_info = []
    for repo in repos:
        repo_owner = repo['owner']['login']
        repo_name = repo['name']
        repo_html_url = repo['html_url']
        response = requests.get('https://api.github.com/repos/{}/{}/issues'.
                                format(repo_owner, repo_name))
        issues_data = response.json()
        issues_quantity = len(issues_data)
        clean_repo_info.append({'repo_name': repo_name,
                                'repo_owner': repo_owner,
                                'repo_issues_quantity': issues_quantity,
                                'repo_html_url': repo_html_url})
    return clean_repo_info


if __name__ == '__main__':
    repos_quantity = 20
    trending_repos = get_trending_repositories(repos_quantity)
    clean_repos_info = get_repo_clean_info(trending_repos)
    print_data_from_repos(clean_repos_info)
