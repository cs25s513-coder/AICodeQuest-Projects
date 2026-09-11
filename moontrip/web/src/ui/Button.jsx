// BASELINE — implemented by the study team. Do not modify for tasks M1-M12.
export default function Button({ children, secondary = false, ...rest }) {
  return (
    <button className={`btn ${secondary ? "secondary" : ""}`.trim()} {...rest}>
      {children}
    </button>
  );
}
