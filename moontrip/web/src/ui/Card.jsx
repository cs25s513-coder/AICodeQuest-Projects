// BASELINE — implemented by the study team. Do not modify for tasks M1-M12.
export default function Card({ children, className = "" }) {
  return <div className={`card ${className}`.trim()}>{children}</div>;
}
