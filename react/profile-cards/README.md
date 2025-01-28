# Interview Problem: Build a Team Profile Component

## Prompt

You are tasked with building a **React component** to display a **Team Profile**. This component should provide an overview of a team's information, including the team's name, description, members, active projects, and performance metrics.

Your goal is to:

- **Display the team's name and description** prominently.
- **Render a list of team members** with their roles and contact information.
- **Showcase a list of active projects** with their statuses.
- **Include performance metrics** (e.g., scorecards or KPIs) in a visually clear and concise manner.

You are free to style the component as you like, but prioritize **usability** and **readability**.

---

## Example JSON Object

Here is the JSON object with example profile information:

```json
{
  "team": {
    "name": "Frontend Wizards",
    "description": "A team dedicated to crafting seamless user interfaces and exceptional user experiences.",
    "members": [
      {
        "id": 1,
        "name": "Alice Johnson",
        "role": "Team Lead",
        "email": "alice.johnson@example.com",
        "avatar": "https://example.com/avatars/alice.jpg"
      },
      {
        "id": 2,
        "name": "Bob Smith",
        "role": "Senior Developer",
        "email": "bob.smith@example.com",
        "avatar": "https://example.com/avatars/bob.jpg"
      },
      {
        "id": 3,
        "name": "Charlie Brown",
        "role": "UI Designer",
        "email": "charlie.brown@example.com",
        "avatar": "https://example.com/avatars/charlie.jpg"
      }
    ],
    "projects": [
      {
        "id": 101,
        "name": "Landing Page Redesign",
        "status": "In Progress"
      },
      {
        "id": 102,
        "name": "Accessibility Improvements",
        "status": "Completed"
      },
      {
        "id": 103,
        "name": "UI Component Library",
        "status": "In Review"
      }
    ],
    "performanceMetrics": {
      "sprintVelocity": 45,
      "bugFixRate": "85%",
      "customerSatisfactionScore": 9.2
    }
  }
}
```
