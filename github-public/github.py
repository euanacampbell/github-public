import requests
from bs4 import BeautifulSoup


class profile:

    def __init__(self, username: str):
        self.username = username

        self.repositories = []

        repos = self.get_repos(username)
        for repo in repos:
            self.repositories.append(repository(username, repos[repo]))

    @staticmethod
    def get_repos(username):
        """locate and download all repository data from GitHub"""

        url = f"https://github.com/{username}?tab=repositories"

        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')

        repo_list = soup.findAll("li", itemprop="owns")  # repo description

        repository_data = {}

        for repo in repo_list:
            # titles
            children = repo.findChildren("a", itemprop="name codeRepository")
            for child in children:
                title = child.text.split('   ')[-1].strip()

            # description
            children = repo.findChildren("p", itemprop="description")
            try:
                description = children[0].text.split('\n')[1].strip()
            except IndexError:
                description = None

            # language
            children = repo.findChildren(
                "span", itemprop="programmingLanguage")
            try:
                language = children[0].text.split(' ')[-1]
            except IndexError:
                language = None

            repository_data[title] = {
                'title': title,
                'description': description,
                'language': language
            }

        return repository_data


class repository:

    def __init__(self, username: str, data: dict):
        self.url = f"https://github.com/{username}/{data['title']}"

        for k, v in data.items():
            setattr(self, k, v)


if __name__ == "__main__":
    git_user = profile('euanacampbell')

    for repo in git_user.repositories:

        print('')
        print(f"title: {repo.title}")
        print(f"url: {repo.url}")
        print(f"description: {repo.description}")
        print(f"language: {repo.language}")
