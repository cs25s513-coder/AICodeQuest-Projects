# ============================================================
# TASK M2 — Mars launch windows
# Files for this task:
#   logic/launch_windows.py     <- this file
#   api/launch_windows_routes.py
#   web/src/tasks/LaunchWindowBadge.jsx
# TODO(M2):
#   [ ] implement is_window_open() and next_launch_window() in this file
#   [ ] implement the GET /api/destinations/<id>/next-window route
#   [ ] show a "next window in N days" badge on destination cards
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================


def is_window_open(window, date):
    """Return True if `date` falls inside `window`.

    window: {"opens": "YYYY-MM-DD", "closes": "YYYY-MM-DD"}
    date: "YYYY-MM-DD"

    A window is open if opens <= date <= closes (inclusive both ends).
    """
    raise NotImplementedError("TODO(M2)")


def next_launch_window(windows, today):
    """Return the next launch window on or after `today`.

    windows: list of {"opens": "YYYY-MM-DD", "closes": "YYYY-MM-DD"}
    today: "YYYY-MM-DD"

    The next window is the earliest window with closes >= today. If that
    window is already open (per is_window_open), days_until is 0.
    Otherwise days_until is the number of days from today to opens.

    Returns {"opens": ..., "closes": ..., "days_until": int}, or None if
    `windows` is empty or every window has already closed.
    """
    raise NotImplementedError("TODO(M2)")
