# Workflow and Contributions Guide

This document outlines the workflow and contributions process for the repository, including branch and commit naming conventions to ensure consistency and collaboration.

---

## Table of Contents
1. [Getting Started](#getting-started)
2. [Workflow Overview](#workflow-overview)
3. [Branch Naming Convention](#branch-naming-convention)
4. [Commit Naming Convention](#commit-naming-convention)
5. [Pull Request Process](#pull-request-process)
6. [Code Review Guidelines](#code-review-guidelines)
7. [Code of Conduct](#code-of-conduct)

---

## Getting Started

1. **Fork the Repository**: Fork this repository to your GitHub account.
2. **Clone the Repository**: Clone your forked repository to your local machine using:
   ```bash
   git clone <your-forked-repo-url>
   ```
3. **Set Up the Remote**: Add the original repository as an upstream remote to keep your fork updated:
   ```bash
   git remote add upstream <original-repo-url>
   ```
4. **Sync Your Fork**: Regularly sync your fork with the upstream repository:
   ```bash
   git fetch upstream
   git merge upstream/main
   ```

---

## Workflow Overview

We follow the **Git Feature Branch Workflow** to ensure a streamlined and organized collaboration process.

1. **Main Branch** (`main`): This branch contains the stable, production-ready code.
2. **Development Branch** (`dev`): This branch serves as the integration branch where features are developed and tested before being merged into the `main` branch.
3. **Feature Branches**: New features, bug fixes, or experiments should be developed on separate branches based on the naming convention below.

---

## Branch Naming Convention

To maintain clarity and organization, follow this naming convention for branches:

### Format
```
git branch <category/reference/description-in-kebab-case>
```

### Categories
- **feature**: For adding, refactoring, or removing a feature.
- **bugfix**: For fixing a bug.
- **hotfix**: For urgent changes or temporary solutions.
- **test**: For experimenting outside of an issue or ticket.

### Examples
- Adding a new feature: `feature/issue-42/create-new-button-component`
- Fixing a bug: `bugfix/issue-342/button-overlap-form-on-mobile`
- Emergency fix: `hotfix/no-ref/registration-form-not-working`
- Experimenting: `test/no-ref/refactor-components-with-atomic-design`

---

## Commit Naming Convention

Commit messages should be concise and follow this format:

### Format
```
git commit -m '<category: do something; do some other things>'
```

### Categories
- **feat**: Adding a new feature.
- **fix**: Fixing a bug.
- **refactor**: Improving code for performance or readability.
- **chore**: Miscellaneous tasks like writing documentation, formatting, or adding tests.

### Examples
- Adding a feature: `git commit -m 'feat: add new button component; add button to templates'`
- Fixing a bug: `git commit -m 'fix: add stop directive to button to prevent propagation'`
- Refactoring code: `git commit -m 'refactor: rewrite button component in TypeScript'`
- Documentation: `git commit -m 'chore: write button documentation'`

---

## Pull Request Process

1. **Create a Pull Request (PR)**:
   - Ensure your branch is up to date with `dev`.
   - Push your branch to your forked repository.
   - Open a PR against the `dev` branch of the main repository.
2. **Describe Your Changes**:
   - Provide a clear title and description of the changes made.
   - Reference the issue or ticket number (if applicable).
3. **Request Reviews**:
   - Add reviewers who can provide feedback and approve your PR.
4. **Address Feedback**:
   - Respond to comments and make necessary changes.
   - Push updates to the same branch used for the PR.

---

## Code Review Guidelines

- Follow the branch and commit naming conventions.
- Ensure your code adheres to the repository’s style guidelines.
- Write clear and concise comments for non-obvious code.
- Check for security vulnerabilities and performance issues.
- Test your code thoroughly before submitting a PR.

---

## Code of Conduct

By contributing to this repository, you agree to:
- Be respectful and inclusive in all communications.
- Provide constructive feedback during reviews.
- Follow the repository’s contribution and workflow guidelines.
- Report any issues or violations to the repository maintainers.

For detailed guidelines, refer to [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

---

This guide ensures a consistent and collaborative workflow. If you have any questions or suggestions, feel free to reach out via GitHub Discussions or Issues!

