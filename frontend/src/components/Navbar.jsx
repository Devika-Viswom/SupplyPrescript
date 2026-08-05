import { NavLink } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-slate-900 text-white px-8 py-4 flex justify-between">

      <h1 className="font-bold text-xl">
        SupplyPrescript
      </h1>

      <div className="flex gap-6">

        <NavLink
          to="/"
          className={({ isActive }) =>
            isActive
              ? "text-blue-400 font-semibold"
              : "text-white"
          }
        >
          Dashboard
        </NavLink>

        <NavLink
          to="/predict"
          className={({ isActive }) =>
            isActive
              ? "text-blue-400 font-semibold"
              : "text-white"
          }
        >
          Predict
        </NavLink>

        <NavLink
          to="/history"
          className={({ isActive }) =>
            isActive
              ? "text-blue-400 font-semibold"
              : "text-white"
          }
        >
          History
        </NavLink>

        <NavLink
          to="/insights"
          className={({ isActive }) =>
            isActive
              ? "text-blue-400 font-semibold"
              : "text-white"
          }
        >
          Insights
        </NavLink>

      </div>

    </nav>
  );
}