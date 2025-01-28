export interface TeamMember {
  id: number;
  name: string;
  role: string;
  email: string;
  avatar: string;
}

export interface Project {
  id: number;
  name: string;
  status: "In Progress" | "Completed" | "In Review"; // You can make this a union type for stricter typing
}

export interface IPerformanceMetrics {
  sprintVelocity: number;
  bugFixRate: string;
  customerSatisfactionScore: number;
}

export interface TeamData {
  name: string;
  description: string;
  members: TeamMember[];
  projects: Project[];
  performanceMetrics: IPerformanceMetrics;
}
