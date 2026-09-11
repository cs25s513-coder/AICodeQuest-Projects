// BASELINE — implemented by the study team. Do not modify for tasks M1-M12.
// Warm-up W1 adds active-link highlighting and a footer to this shared shell.
import { Link } from "react-router-dom";

const LINKS = [
  { to: "/", label: "Home" },
  { to: "/destinations", label: "Destinations" },
  { to: "/book", label: "Book" },
  { to: "/my-trips", label: "My trips" },
  { to: "/mission-control", label: "Mission control" },
  { to: "/deals", label: "Deals" },
];

export default function Nav() {
  return (
    <nav className="navbar">
      <Link to="/" className="brand">
        🌌 MoonTrip
      </Link>
      {LINKS.map((link) => (
        <Link key={link.to} to={link.to} className="nav-link">
          {link.label}
        </Link>
      ))}
    </nav>
  );
}
