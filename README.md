# 🚀 Twine-Autodeploy Workflow

This is is an autodeploy workflow that automatically uploads to twine after using bumpver!

## How to use
First ensure that you have an API token in the secrets, as ``TWINE_USERNAME``

Then in the Pull Request Description, simply place the string "version: " followed by either "major", "minor", or "patch" depending on what you want to bump.

This is will bump the version on merge, and then deploy it to PyPi
