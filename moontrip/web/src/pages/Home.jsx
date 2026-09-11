// BASELINE — implemented by the study team. Do not modify for tasks M1-M12.
import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div>
      <div className="hero">
        <div className="stars" />
        <div className="moon" />
        <h1>Round trip to the Moon: ₹12,400 only.</h1>
        <p>
          MoonTrip sells seats on real (and wildly subsidised) rockets to the
          Moon, Mars, and the orbital hotels in between. Browse the
          destinations, pick a launch, and go.
        </p>
        <div style={{ marginTop: 24 }}>
          <Link to="/destinations" className="btn">
            Browse destinations
          </Link>
        </div>
      </div>

      <div className="section">
        <h2>Why fly with us</h2>
        <div className="grid">
          <div className="card">
            <h3>Six destinations</h3>
            <p className="tagline">From lunar day-trips to a Mars expedition.</p>
          </div>
          <div className="card">
            <h3>A real fleet</h3>
            <p className="tagline">Four spacecraft, each with its own seat map.</p>
          </div>
          <div className="card">
            <h3>Flexible plans</h3>
            <p className="tagline">Loyalty miles, refunds, and launch-day deals.</p>
          </div>
        </div>
      </div>
    </div>
  );
}
