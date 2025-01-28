import {
  IPerformanceMetrics,
  Project,
  TeamData,
  TeamMember,
} from "./interfaces";
import { initialData } from "./teamData";
import "./App.css";

function App() {
  return (
    <div>
      <TeamCard {...initialData} />
    </div>
  );
}

const TeamCard: React.FC<TeamData> = ({
  name,
  description,
  members,
  projects,
  performanceMetrics,
}) => (
  <div>
    <div>
      <h1>{name}</h1>
      <p className="secondary">{description}</p>
    </div>
    <TeamMembers members={members} />
    <TeamProjects projects={projects} />
    <PerformanceMetrics {...performanceMetrics} />
  </div>
);

const TeamMembers: React.FC<{ members: TeamMember[] }> = ({ members }) => {
  return (
    <div className="members">
      <h1>Wonderful Team Members 👥</h1>
      <ul>
        {members.map((member) => (
          <li key={member.id} className="team-member">
            <span>
              <img className="avatar" src={member.avatar} alt={member.name} />
            </span>
            <span>
              <p>{member.name}</p>
              <p>{member.role}</p>
              <p>{member.email}</p>
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
};

const TeamProjects: React.FC<{ projects: Project[] }> = ({ projects }) => {
  return (
    <>
      <h1>Projects 📂</h1>
      <ul>
        {projects.map((project) => (
          <li key={project.id}>{project.name}</li>
        ))}
      </ul>
    </>
  );
};

const PerformanceMetrics: React.FC<IPerformanceMetrics> = ({
  sprintVelocity,
  bugFixRate,
  customerSatisfactionScore,
}) => {
  return (
    <div>
      <h1>Performance Metrics 📊</h1>
      <p>Bug fix rate: {bugFixRate}</p>
      <p>Customer Satifaction Score: {customerSatisfactionScore}</p>
      <p>Sprint Velocity: {sprintVelocity}</p>
    </div>
  );
};

export default App;
