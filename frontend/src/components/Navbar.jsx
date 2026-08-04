import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-slate-900 text-white px-8 py-4 flex justify-between">

      <h1 className="font-bold text-xl">
        SupplyPrescript
      </h1>

      <div className="flex gap-6">

        <Link to="/">Dashboard</Link>

        <Link to="/predict">Predict</Link>

        <Link to="/history">History</Link>

        <Link to="/insights">Insights</Link>

      </div>

    </nav>
  );
}