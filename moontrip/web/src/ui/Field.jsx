// BASELINE — implemented by the study team. Do not modify for tasks M1-M12.
export default function Field({ label, children }) {
  return (
    <div className="field">
      <label>{label}</label>
      {children}
    </div>
  );
}
