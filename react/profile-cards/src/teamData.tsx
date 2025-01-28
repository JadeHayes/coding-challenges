import { TeamData } from "./interfaces";

export const initialData: TeamData = {
  name: "Frontend Wizards",
  description:
    "A team dedicated to crafting seamless user interfaces and exceptional user experiences.",
  members: [
    {
      id: 1,
      name: "Alice Johnson",
      role: "Team Lead",
      email: "alice.johnson@example.com",
      avatar: "https://picsum.photos/id/237/200/300",
    },
    {
      id: 2,
      name: "Bob Smith",
      role: "Senior Developer",
      email: "bob.smith@example.com",
      avatar: "https://picsum.photos/id/238/200/300",
    },
    {
      id: 3,
      name: "Charlie Brown",
      role: "UI Designer",
      email: "charlie.brown@example.com",
      avatar: "https://picsum.photos/id/239/200/300",
    },
  ],
  projects: [
    {
      id: 101,
      name: "Landing Page Redesign",
      status: "In Progress",
    },
    {
      id: 102,
      name: "Accessibility Improvements",
      status: "Completed",
    },
    {
      id: 103,
      name: "UI Component Library",
      status: "In Review",
    },
  ],
  performanceMetrics: {
    sprintVelocity: 45,
    bugFixRate: "85%",
    customerSatisfactionScore: 9.2,
  },
};
