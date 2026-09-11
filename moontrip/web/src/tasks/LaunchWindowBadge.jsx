// ============================================================
// TASK M2 — Mars launch windows
// Files for this task:
//   logic/launch_windows.py
//   api/launch_windows_routes.py
//   web/src/tasks/LaunchWindowBadge.jsx   <- this file
// TODO(M2):
//   [ ] implement is_window_open() and next_launch_window() in
//       logic/launch_windows.py
//   [ ] implement the GET /api/destinations/<id>/next-window route
//   [ ] build this badge
//   [ ] use an AI assistant; tag its lines honestly in the PR
//
// Intended UI: a small badge on each destination card reading something
// like "Next window in 12 days" (or "Window open now"), fetched from
// GET /api/destinations/<id>/next-window. destinationId is passed in as
// a prop from the Destinations page.
// ============================================================
import TaskPlaceholder from "../ui/TaskPlaceholder.jsx";

export default function LaunchWindowBadge() {
  return <TaskPlaceholder title="M2 Next launch window" />;
}
