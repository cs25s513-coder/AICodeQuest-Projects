// BASELINE — implemented by the study team. Do not modify for tasks M1-M12.
// Hosts tasks M6, M12.
import MissionStats from "../tasks/MissionStats.jsx";
import MissionStatus from "../tasks/MissionStatus.jsx";

export default function MissionControl() {
  return (
    <div>
      <h1>Mission control</h1>

      <div className="section">
        <h2>Fleet stats</h2>
        <MissionStats />
      </div>

      <div className="section">
        <h2>Active missions</h2>
        <MissionStatus />
      </div>
    </div>
  );
}
