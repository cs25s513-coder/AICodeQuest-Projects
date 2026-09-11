// BASELINE — implemented by the study team. Do not modify for tasks M1-M12.
import { Route, Routes } from "react-router-dom";

import Nav from "./components/Nav.jsx";
import Book from "./pages/Book.jsx";
import Deals from "./pages/Deals.jsx";
import DestinationDetail from "./pages/DestinationDetail.jsx";
import Destinations from "./pages/Destinations.jsx";
import Home from "./pages/Home.jsx";
import MissionControl from "./pages/MissionControl.jsx";
import MyTrips from "./pages/MyTrips.jsx";

export default function App() {
  return (
    <div className="app-shell">
      <Nav />
      <main className="page">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/destinations" element={<Destinations />} />
          <Route path="/destinations/:id" element={<DestinationDetail />} />
          <Route path="/book" element={<Book />} />
          <Route path="/my-trips" element={<MyTrips />} />
          <Route path="/mission-control" element={<MissionControl />} />
          <Route path="/deals" element={<Deals />} />
        </Routes>
      </main>
    </div>
  );
}
