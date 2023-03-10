import os
from github import Github
from github.Repository import Repository
from getpass import getpass


def get_access_token():
    return os.getenv("GH_TOKEN") or getpass("Enter your GitHub access token: ")


def get_repo_name():
    return os.getenv("GH_REPO") or input("Enter your GitHub repo name: ")


def unstringify(val: str):
    val = val.strip()
    if val.startswith('"') and val.endswith('"'):
        return val[1:-1]
    return val


def read_env_file() -> dict[str, str]:
    values = {}
    with open(".env", "r") as f:
        for line in f:
            key, val = line.split("=", 1)
    with open(".env", "r") as env_file:
        [values.update({key: unstringify(val)}) for line in env_file for key, val in [line.split("=", 1)]]
    return values


def upload_secret(repo: Repository, secret_name: str, secret_value: str):
    repo.create_secret(secret_name, secret_value)


def main(exit_on_failure=True) -> bool:
    if not os.path.exists(".env"):
        print("No '.env' file found at current directory. Exiting...")
        exit_on_failure and exit(1)
        return False

    access_token = get_access_token()
    repo_name = get_repo_name()
    env_values = read_env_file()

    g = Github(access_token)
    repo = g.get_repo(repo_name)

    if not repo:
        print(f"Unable to find repository {repo_name}. Exiting...")
        exit_on_failure and exit(1)
        return False

    for key, val in env_values.items():
        upload_secret(repo, key, val)

    print(f"Created {len(env_values)} keys.")
    return True
