# 🚀 Twine-Autodeploy Workflow

This is is an autodeploy workflow that automatically bumps the version based on the PR description and then pushes to the repository and uploads to twine after using bumpver!


## ❔ How to use
1. First ensure that you have an API token in the secrets, as ``TWINE_USERNAME``
2. Then in the Pull Request Description, simply place the string "version: " followed by either "major", "minor", or "patch" depending on what you want to bump.
3. This is will bump the version on merge, and then deploy it to PyPi
