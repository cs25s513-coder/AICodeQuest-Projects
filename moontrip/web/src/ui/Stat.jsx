// BASELINE — implemented by the study team. Do not modify for tasks M1-M12.
export default function Stat({ label, value }) {
  return (
    <div className="stat">
      <div className="value">{value}</div>
      <div className="label">{label}</div>
    </div>
  );
}
