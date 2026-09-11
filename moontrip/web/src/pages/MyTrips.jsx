// BASELINE — implemented by the study team. Do not modify for tasks M1-M12.
// Hosts tasks M3, M4, M11.
import BookingHistory from "../tasks/BookingHistory.jsx";
import LoyaltyCard from "../tasks/LoyaltyCard.jsx";
import RefundCalculator from "../tasks/RefundCalculator.jsx";

export default function MyTrips() {
  return (
    <div>
      <h1>My trips</h1>

      <div className="section">
        <h2>Moon Miles</h2>
        <LoyaltyCard />
      </div>

      <div className="section">
        <h2>Booking history</h2>
        <BookingHistory />
      </div>

      <div className="section">
        <h2>Cancel a booking</h2>
        <RefundCalculator />
      </div>
    </div>
  );
}
