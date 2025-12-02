```mermaid

  flowchart TD
    Ui --> Services
    Services --> Entities
    Services --> Repositories
    Entities --> Repositories
    Repositories --> Entities

```