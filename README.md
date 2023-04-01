# 🚀 Twine-Autodeploy Workflow

This is is an autodeploy workflow that automatically bumps the version based on the PR description and then pushes to the repository and uploads to twine after using bumpver!


## ❔ How to use
1. First ensure that you have an API token in the secrets, as ``TWINE_USERNAME``
2. Make a ``bumpver.toml`` file to contain all the versions to be updated and the version pattern (look at the ``bumpver.toml`` example)
3. When making a Pull Request simply place the string "version: " followed by either "major", "minor", or "patch" in the description, depending on what you want to bump. Note that "version: " is the default leading regex, but this is configurable under the regex input argument for the github action.
5. This is will bump the version on merge, make a new tag, and deploy it to PyPi

