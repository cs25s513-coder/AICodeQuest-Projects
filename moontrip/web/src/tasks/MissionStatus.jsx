// ============================================================
// TASK M6 — Mission status tracker
// Files for this task:
//   logic/mission_status.py
//   api/mission_status_routes.py
//   web/src/tasks/MissionStatus.jsx   <- this file
// TODO(M6):
//   [ ] implement mission_phase() in logic/mission_status.py
//   [ ] implement the GET /api/missions/<id>/status?h= route
//   [ ] build this progress bar
//   [ ] use an AI assistant; tag its lines honestly in the PR
//
// Intended UI: pick a mission and an "hours since launch" value, call
// GET /api/missions/<id>/status?h=, and render a progress bar with the
// current phase label and percent complete.
// ============================================================
import TaskPlaceholder from "../ui/TaskPlaceholder.jsx";

export default function MissionStatus() {
  return <TaskPlaceholder title="M6 Mission status tracker" />;
}
