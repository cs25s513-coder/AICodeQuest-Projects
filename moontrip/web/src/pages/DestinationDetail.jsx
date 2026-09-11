// BASELINE — implemented by the study team. Do not modify for tasks M1-M12.
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

import { getJson } from "../api.js";

export default function DestinationDetail() {
  const { id } = useParams();
  const [destination, setDestination] = useState(null);
  const [spacecraft, setSpacecraft] = useState([]);

  useEffect(() => {
    getJson(`/api/destinations/${id}`).then(setDestination);
    getJson("/api/spacecraft").then(setSpacecraft);
  }, [id]);

  if (!destination) {
    return <p>Loading…</p>;
  }

  return (
    <div>
      <h1>{destination.name}</h1>
      <p className="tagline">{destination.tagline}</p>
      <div className="stat-row section">
        <div className="stat">
          <div className="value">₹{destination.base_price_inr.toLocaleString("en-IN")}</div>
          <div className="label">One-way base fare</div>
        </div>
        <div className="stat">
          <div className="value">{destination.travel_days}</div>
          <div className="label">Travel days</div>
        </div>
      </div>

      <div className="section">
        <Link to="/book" className="btn">
          Book this trip
        </Link>
      </div>

      <div className="section">
        <h2>Our fleet</h2>
        <div className="grid">
          {spacecraft.map((craft) => (
            <div className="card" key={craft.id}>
              <h3>{craft.name}</h3>
              <p className="tagline">{craft.description}</p>
              <p>
                {craft.free_seats} of {craft.total_seats} seats free
              </p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
