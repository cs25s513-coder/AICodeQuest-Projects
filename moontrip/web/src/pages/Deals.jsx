// BASELINE — implemented by the study team. Do not modify for tasks M1-M12.
// A plain browse-only view of data/promos.json. Applying a code at
// checkout is task M7, built on the Book page (see tasks/PromoCode.jsx).
import { useEffect, useState } from "react";

import { getJson } from "../api.js";

export default function Deals() {
  const [promos, setPromos] = useState([]);

  useEffect(() => {
    getJson("/api/promos").then(setPromos);
  }, []);

  return (
    <div>
      <h1>Deals</h1>
      <p className="tagline">Current promo codes. Apply one at checkout on the Book page.</p>

      <div className="grid section">
        {promos.map((promo) => (
          <div className="card" key={promo.code}>
            <h3>{promo.code}</h3>
            <p className="tagline">
              {promo.type === "percent" ? `${promo.value}% off` : `₹${promo.value} off`}
              {promo.min_spend_inr ? ` on orders over ₹${promo.min_spend_inr.toLocaleString("en-IN")}` : ""}
            </p>
            <p className="tagline">Expires {promo.expires}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
