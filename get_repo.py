
import requests
# import pip._vendor.requests as requests
import json




## Run Program
def run():
    user = input("Please enter a GitHub user ID: ")
    try:
        connect(user)
    except(AttributeError):
        print("Unable to find an acount with that username")

def connect(user):
    status_code = 200
    no_connection26 = "No Connection: Line 26"
    code200 = True
    repo_url = "https://api.github.com/users/%s/repos"  ## % (userid)
    commit_url = "https://api.github.com/repos/%s/%s/commits"  ## % (id, repo)

    ## Get User
    repo_page = requests.get(repo_url % user)
    if repo_page.status_code == status_code:
        repository_data = repo_page.json()
        ## Parse Repositories
        for each in repository_data:
            repo_name = each["name"]
            ## Get Repo Commits
            commit_page = requests.get(commit_url % (user, repo_name))
            if commit_page.status_code == status_code:
                commit_data = commit_page.json()
                print("Repo: ", repo_name, "   Commits: ", len(commit_data))
            else:
                print(no_connection26)
                code200 = False
    else:
        print("No Connection: Line 18")
        code200 = False

    return code200


if __name__ == '__main__':
    run()
