# Welcome to madlib

Welcome to the MkDocs madlib plugin example.

## Example

Normal fenced code:

```python
print("normal fenced code")
```

Madlib fenced code:

```madlib
project=project

resource "google_project_iam_member" "project" {
  project = "your-project-id"
  role    = "roles/editor"
  member  = "user:jane@example.com"
}
```
