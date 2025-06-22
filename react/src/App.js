import "./App.css";
import { useState } from "react";
import { data } from "./data/data";
import TableDetails from "./components/TableDetails";
import AddReservations from "./components/addReservations";

function App() {
  const [page, setPage] = useState("home");
  const [reservationsState, setReservations] = useState(data);

  const updateReservations = (reservations) => {
    setReservations([reservations, ...reservationsState]); //new submission place at front
    // console.log(reservations);
  };

  return (
    <div className="App">
      <h1>Restaurants Reservations</h1>
      <div className="main-container">
        <div className="container">
          <nav>
            <button onClick={() => setPage("home")}>Home</button>
            <button onClick={() => setPage("tables")}>Available Slots</button>
            <button onClick={() => setPage("reservation")}>
              Add Reservation
            </button>
          </nav>
          <div className="text">
            {page === "home" && (
              <div>
                <div>
                  <p>
                    This is a real-time online table booking network for making
                    reservations at restaurants.
                  </p>
                </div>
                {[
                  "Red Wagon Burger",
                  "Cheesecake Factory",
                  "Applebee's",
                  " Zippy's",
                  "John Howies",
                  "Red Robin",
                  "The Pink Door",
                  "Shaker + Spear",
                  "The Capital Grille",
                  "Cactus",
                ].map((word) => (
                  <div
                    key={word}
                    className="restuarants"
                    onClick={() => setPage("tables")}
                  >
                    {word}
                  </div>
                ))}
              </div>
            )}
            {page === "tables" && (
              <div>
                <p>
                  Now that you have chosen a restuarant please pick a available
                  time that works for you. And it not works pleaase add a
                  reservation Instead.
                </p>
                <TableDetails reservations={reservationsState} />
                <button
                  onClick={() => {
                    setPage("reservation");
                  }}
                >
                  Add Reservation Instead?
                </button>
              </div>
            )}
            {page === "reservation" && (
              <div className="form-item ">
                <AddReservations updateReservations={updateReservations} />
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
