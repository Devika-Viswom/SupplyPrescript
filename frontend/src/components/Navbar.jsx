import { NavLink } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="sticky top-0 z-50 bg-slate-950 border-b border-slate-800 shadow-lg">
      <div className="max-w-7xl mx-auto px-8 h-18 flex items-center justify-between">

        <div>
          <h1 className="text-2xl font-bold text-white tracking-tight">
            SupplyPrescript
          </h1>

          <p className="text-xs text-slate-400">
            Predictive & Prescriptive Supply Chain Analytics
          </p>
        </div>

        <div className="flex items-center gap-2">

          <NavLink
            to="/"
            className={({ isActive }) =>
              `px-4 py-2 rounded-lg transition-all ${
                isActive
                  ? "bg-blue-600 text-white font-semibold"
                  : "text-slate-300 hover:bg-slate-800 hover:text-white"
              }`
            }
          >
            Dashboard
          </NavLink>

          <NavLink
            to="/predict"
            className={({ isActive }) =>
              `px-4 py-2 rounded-lg transition-all ${
                isActive
                  ? "bg-blue-600 text-white font-semibold"
                  : "text-slate-300 hover:bg-slate-800 hover:text-white"
              }`
            }
          >
            Predict
          </NavLink>

          <NavLink
            to="/history"
            className={({ isActive }) =>
              `px-4 py-2 rounded-lg transition-all ${
                isActive
                  ? "bg-blue-600 text-white font-semibold"
                  : "text-slate-300 hover:bg-slate-800 hover:text-white"
              }`
            }
          >
            History
          </NavLink>

          <NavLink
            to="/insights"
            className={({ isActive }) =>
              `px-4 py-2 rounded-lg transition-all ${
                isActive
                  ? "bg-blue-600 text-white font-semibold"
                  : "text-slate-300 hover:bg-slate-800 hover:text-white"
              }`
            }
          >
            Insights
          </NavLink>

        </div>
      </div>
    </nav>
  );
}