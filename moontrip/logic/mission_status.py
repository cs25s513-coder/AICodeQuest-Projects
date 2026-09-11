# ============================================================
# TASK M6 — Mission status tracker
# Files for this task:
#   logic/mission_status.py     <- this file
#   api/mission_status_routes.py
#   web/src/tasks/MissionStatus.jsx
# TODO(M6):
#   [ ] implement mission_phase() in this file
#   [ ] implement the GET /api/missions/<id>/status?h= route
#   [ ] build the progress bar with phase labels on Mission control
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================


def mission_phase(timeline, hours_since_launch):
    """Return the mission's current phase and progress.

    timeline: list of {"phase": str, "starts_at_hour": number}, ordered
    by starts_at_hour ascending. The first entry always starts at hour 0.
    hours_since_launch: number (may be negative, before launch)

    The current phase is the last timeline entry whose starts_at_hour is
    <= hours_since_launch. If hours_since_launch is negative (before the
    first entry), the phase is "pre-launch". If hours_since_launch is at
    or past the last entry's starts_at_hour, the phase is "complete" once
    the mission is considered finished (treat the last entry's
    starts_at_hour as the mission's total duration).

    progress_pct is hours_since_launch / total_duration_hours * 100,
    clamped to the 0-100 range, where total_duration_hours is the last
    timeline entry's starts_at_hour.

    Returns {"phase": str, "progress_pct": float}.
    """
    raise NotImplementedError("TODO(M6)")
