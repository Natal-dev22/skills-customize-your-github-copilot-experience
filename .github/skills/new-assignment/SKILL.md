---
name: new-assignment
description: "Create, scaffold, or add a programming assignment or homework exercise for this project. Use when a user asks to develop a new student assignment, starter code, or assignment materials."
---

# Creating a New Assignment

## When to Use

Use this skill when creating a programming assignment or adding assignment materials to the student portal.

## Procedure

1. If the user has not provided a topic, ask what concept the assignment should teach. Keep the scope suitable for the intended student level.
2. Choose a descriptive kebab-case ID and create `assignments/<id>/README.md`.
3. Follow the [assignment template](../../.github/templates/assignment-template.md). Keep its title, objective, and tasks sections, with two action-oriented tasks. Make requirements clear and measurable, and use student-friendly language.
4. Add starter code or sample data in the same assignment directory when it helps students focus on the learning goals. Keep starter code runnable where possible and mark incomplete sections clearly.
5. Add an entry for the assignment to the root `config.json` `assignments` array. Use the directory ID, a concise title and description, and the path `assignments/<id>`. Add attachment entries for files students should download.
6. Verify that `config.json` parses, the assignment README and any configured attachments exist, and the README follows the template structure.
