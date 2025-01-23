**GitHub Workflow Guide for Collaborations**

This guide outlines the branching and collaboration workflow for our GitHub repository. It defines how we work on features, review code, and ensure a stable and deployable main branch.

---

### **Branching Strategy**

#### **1. Main Branch (****`main`****)**

- The `main` branch is our **stable, production-ready branch**.
- Only thoroughly tested and reviewed code should be merged into `main`.
- Protected from direct commits; all changes must come through Pull Requests (PRs).

#### **2. Development Branch (****`dev`****)**

- The `dev` branch is our **integration branch** for active development.
- All feature branches are merged into `dev` after review and approval.
- Periodically, when `dev` is stable, it is merged into `main`.

#### **3. Feature Branches (****`feature/<feature-name>`****)**

- Feature branches are created off of `dev` to work on specific features or bug fixes.
- Naming convention: `feature/<feature-name>` (e.g., `feature/login-page`).
- Once completed, feature branches are merged back into `dev` via a PR.

---

### **Workflow Steps**

#### **1. Setting Up Your Local Environment**

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Fetch all branches and set up tracking:
   ```bash
   git fetch origin
   ```
3. Set the upstream branches:
   ```bash
   git checkout main
   git branch --set-upstream-to=origin/main main

   git checkout dev
   git branch --set-upstream-to=origin/dev dev
   ```

---

#### **2. Starting a New Feature**

1. Check out the `dev` branch:
   ```bash
   git checkout dev
   ```
2. Pull the latest changes:
   ```bash
   git pull origin dev
   ```
3. Create a new feature branch:
   ```bash
   git checkout -b feature/<feature-name>
   ```

---

#### **3. Working on the Feature**

- Commit changes to the feature branch:
  ```bash
  git add .
  git commit -m "Description of the changes"
  ```
- Push the branch to the remote repository:
  ```bash
  git push origin feature/<feature-name>
  ```

---

#### **4. Submitting a Pull Request**

1. Once the feature is complete, go to the repository on GitHub.
2. Create a Pull Request (PR) from your `feature/<feature-name>` branch into `dev`.
3. Follow these guidelines when creating a PR:
   - **Title**: Briefly describe the feature or fix.
   - **Description**: Include:
     - What was done.
     - Any dependencies or setup required.
     - Relevant issue numbers (if applicable).
4. Request at least one reviewer to review the PR.

---

#### **5. Code Review and Approval**

- Reviewers check the PR for:
  - Code quality.
  - Adherence to project conventions.
  - Completeness and correctness.
- Address any requested changes.
- Once approved, the PR can be merged into `dev`.

---

#### **6. Merging ****`dev`**** into ****`main`**

- When the `dev` branch is stable and all features are tested:
  1. Check out the `main` branch:
     ```bash
     git checkout main
     ```
  2. Merge `dev` into `main`:
     ```bash
     git merge dev
     ```
  3. Push the updated `main` branch to the remote repository:
     ```bash
     git push origin main
     ```

---

### **Branch Protection Rules**

To ensure stability and quality, the following rules are applied:

1. **Main Branch (****`main`****):**
   - Require PR reviews before merging.
   - Restrict direct pushes.
   - Require passing status checks (e.g., tests) before merging.
2. **Development Branch (****`dev`****):**
   - Allow PRs from feature branches only.

---

### **Best Practices**

1. **Commit Often**: Commit your changes frequently with meaningful messages.
2. **Pull Regularly**: Keep your feature branch up-to-date with the latest `dev` branch.
   ```bash
   git pull origin dev
   ```
3. **Write Clear PR Descriptions**: Help reviewers understand your changes.
4. **Test Locally**: Test your code locally before submitting a PR.
5. **Resolve Conflicts**: If merge conflicts occur, resolve them in your feature branch before creating a PR.

---

### **Summary of Workflow**

1. Work on a feature branch created from `dev`.
2. Submit a PR to merge your feature branch into `dev`.
3. Review and test changes in `dev`.
4. Merge `dev` into `main` when ready for deployment.

This workflow ensures clear collaboration, stable releases, and a structured development process.

---

If you have any questions or suggestions, feel free to raise them in our team discussions!



