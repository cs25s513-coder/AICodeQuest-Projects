// ============================================================
// TASK M5 — Seat allocation
// Files for this task:
//   logic/seating.py
//   api/seating_routes.py
//   web/src/tasks/SeatMap.jsx   <- this file
// TODO(M5):
//   [ ] implement allocate_seats() in logic/seating.py
//   [ ] implement the POST /api/craft/<id>/allocate route
//   [ ] build this seat map
//   [ ] use an AI assistant; tag its lines honestly in the PR
//
// Intended UI: pick a spacecraft and a group size, call
// POST /api/craft/<id>/allocate, then render the craft's seat grid with
// the allocated seats highlighted (and a message if the group can't fit).
// ============================================================
import TaskPlaceholder from "../ui/TaskPlaceholder.jsx";

export default function SeatMap() {
  return <TaskPlaceholder title="M5 Seat allocation" />;
}
