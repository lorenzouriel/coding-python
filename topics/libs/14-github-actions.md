Standard an Overview (pre-commit)
Definition: Pre-commit is a Git hook structure that helps maintain code quality by ensuring that automated reviews, such as code formatting and lint checks, are performed before each commit.
- https://pre-commit.com/

Purpose: Prevent code that does not meet specific standards from being committed.

Makes Developer's Life Easier: Automating checks and corrections, ensuring that only clean code that adheres to guidelines is submitted. You use your time with what generates value, not with formatting and things like that

Installation: Simple and quick, using poetry
```
poetry add pre-commit

pre-commit install
```

Configuration: Set your automatic checks and fixes in the .precommit-config.yaml file in your repository.

Practical Use: After configuration, precommit automatically checks and/or corrects the files to be committed, according to the defined rules.

Implementing Pre-commit is a very participatory process. Ideally, the entire team should agree on what the project standards will be.

---
Pattern an Overview (GitHub Actions)
GitHub Actions is a CI/CD (Continuous Integration/Continuous Delivery) platform that allows you to automate, customize, and run your software workflows directly in GitHub.

It aims to be a protector of your production code. It will be a 24/7 QA that performs all necessary validations.

Automate Everything: From testing, building and deploying to issue triage and more

In Action: Workflows are built through code and managed directly in your GitHub repositories.
- https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions


Workflows on GitHub Actions
Workflow Files: They are created using the YAML language and stored in the .github/workflows directory of your repository.

Trigger Events: Workflows can be triggered by a variety of events, such as push, pull requests, or even at scheduled times

Actions: Each workflow can contain one or more actions, which are individual tasks that can be performed