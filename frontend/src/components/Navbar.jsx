import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav>
      <Link to="/">Dashboard</Link> |{" "}
      <Link to="/predict">Predict</Link> |{" "}
      <Link to="/history">History</Link> |{" "}
      <Link to="/insights">Insights</Link>
    </nav>
  );
}