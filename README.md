# GitHub Env (GHENV)
#### Copy your .env into GitHub Secrets within seconds

#### Flow:
1. Checks if a .env exists at your current workdir, errors out if it doesn't.
2. Loads all the environment variables from the .env file.
3. Asks for the name of the repository you'd like to use.
4. Creates KV pairs of the environment variables and their values on GitHub secrets on your chosen repo.

#### Optional environment variables:
1. `GH_TOKEN` - GitHub token to use for authentication. If not provided, it will ask for a token.
2. `GH_REPO` - GitHub repository to use. If not provided, it will ask for a repository.