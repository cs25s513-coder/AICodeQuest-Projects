// BASELINE — implemented by the study team. Do not modify for tasks M1-M12.
// Hosts task M2 (LaunchWindowBadge) on each destination card.
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import { getJson } from "../api.js";
import LaunchWindowBadge from "../tasks/LaunchWindowBadge.jsx";

export default function Destinations() {
  const [destinations, setDestinations] = useState([]);
  const [sortBy, setSortBy] = useState("");

  useEffect(() => {
    const query = sortBy ? `?sort_by=${sortBy}` : "";
    getJson(`/api/destinations${query}`).then(setDestinations);
  }, [sortBy]);

  return (
    <div>
      <h1>Destinations</h1>
      <div className="field" style={{ maxWidth: 220 }}>
        <label htmlFor="sort">Sort by</label>
        <select id="sort" value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
          <option value="">Default</option>
          <option value="name">Name</option>
          <option value="price">Price</option>
          <option value="travel_days">Travel time</option>
        </select>
      </div>

      <div className="grid section">
        {destinations.map((d) => (
          <div className="card" key={d.id}>
            <h3>{d.name}</h3>
            <p className="tagline">{d.tagline}</p>
            <p>
              ₹{d.base_price_inr.toLocaleString("en-IN")} one-way ·{" "}
              {d.travel_days} day{d.travel_days === 1 ? "" : "s"}
            </p>
            <LaunchWindowBadge destinationId={d.id} />
            <div style={{ marginTop: 12 }}>
              <Link to={`/destinations/${d.id}`} className="btn secondary">
                View details
              </Link>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
