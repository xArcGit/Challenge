# Here is a detailed guide based on your steps and requirements to log a problem in your repository:

## Step-by-Step Guide to Log a Problem

### Step 1: Solve a Problem

1. **Choose a Platform:**
   - Visit LeetCode, HackerRank, or CodeChef.
2. **Select and Solve:**
   - Pick a problem to solve.
   - Solve the problem using your preferred programming language.

### Step 2: Add an Entry to `log.md`

1. **Open `log.md`:**
   - Open the `log.md` file in your repository.
2. **Add New Entry:**
   - Append a new entry to the file using the following format:
     ```markdown
     | S.No | Date       | Type    | Name                     | Language | Link                                    | Website   | Description                     |
     |------|------------|---------|--------------------------|----------|-----------------------------------------|-----------|---------------------------------|
     | 1    | YYYY-MM-DD | new     | Problem Name             | Language | [Link](https://website.com/problem)     | Website   | Brief description of the solution |
     ```

### Step 3: Commit Your Changes

1. **Save Changes:**
   - Save the changes you made to `log.md`.
2. **Commit and Push:**
   - Open your terminal or command prompt.
   - Navigate to your repository's directory.
   - Execute the following commands:
     ```bash
     git add log.md
     git commit -m "Logged problem: [Problem Name]"
     git push origin main
     ```

# Example Log Entry Explained

Here's a breakdown of the fields for an example log entry:

- **S.No:** Sequential number tracking the total number of problems solved.
- **Date:** The date when you solved the problem in the format `YYYY-MM-DD`.
- **Type:** The type of entry: `new` for new problems, `improve` for improved solutions, and `other` for miscellaneous entries.
- **Name:** The complete name of the problem.
- **Language:** The programming language used to solve the problem.
- **Link:** A hyperlink to the problem on the respective website.
- **Website:** The platform where the problem is hosted (LeetCode, HackerRank, CodeChef).
- **Description:** A brief description of the solution or any notes about the problem.

### Special Case: Improved Solution

If the type is `improve`, locate the original problem entry in `log.md` and append the new solution details right below it without adding a new `S.No`.

## Example

Here’s a practical example of adding an entry for a new problem and an improved solution:

### New Problem Entry

```markdown
| S.No | Date       | Type    | Name              | Language | Link                                   | Website   | Description                        |
|------|------------|---------|-------------------|----------|----------------------------------------|-----------|------------------------------------|
| 1    | 2024-06-18 | new     | Two Sum           | Python   | [Link](https://leetcode.com/problems/two-sum) | LeetCode  | Used a hashmap for O(n) solution   |
```

### Improved Solution Entry

Locate the original problem log for "Two Sum" and append the new solution details below it:

```markdown
| S.No | Date       | Type    | Name              | Language | Link                                   | Website   | Description                        |
|------|------------|---------|-------------------|----------|----------------------------------------|-----------|------------------------------------|
| 1    | 2024-06-08 | new     | Two Sum           | Python   | [Link](https://leetcode.com/problems/two-sum) | LeetCode  | Used a hashmap for O(n) solution   |
|      | 2024-06-09 | improve | Two Sum           | Python   | [Link](https://leetcode.com/problems/two-sum) | LeetCode  | Optimized with early return        |
```
