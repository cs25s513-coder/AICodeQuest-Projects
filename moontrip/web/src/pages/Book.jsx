// BASELINE — implemented by the study team. Do not modify for tasks M1-M12.
// Hosts tasks M1, M5, M7, M8, M9, M10 — each section below is a task slot.
import ItineraryValidator from "../tasks/ItineraryValidator.jsx";
import LuggageEstimator from "../tasks/LuggageEstimator.jsx";
import PassengerChecks from "../tasks/PassengerChecks.jsx";
import PriceCalculator from "../tasks/PriceCalculator.jsx";
import PromoCode from "../tasks/PromoCode.jsx";
import SeatMap from "../tasks/SeatMap.jsx";

export default function Book() {
  return (
    <div>
      <h1>Book your trip</h1>
      <p className="tagline">
        Pick a destination, choose your seats, and check out. Every step
        below is a task a participant will build.
      </p>

      <div className="section">
        <h2>Price calculator</h2>
        <PriceCalculator />
      </div>

      <div className="section">
        <h2>Seat map</h2>
        <SeatMap />
      </div>

      <div className="section">
        <h2>Passenger details</h2>
        <PassengerChecks />
      </div>

      <div className="section">
        <h2>Luggage</h2>
        <LuggageEstimator />
      </div>

      <div className="section">
        <h2>Itinerary</h2>
        <ItineraryValidator />
      </div>

      <div className="section">
        <h2>Checkout summary</h2>
        <PromoCode />
      </div>
    </div>
  );
}
