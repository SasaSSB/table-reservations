function Reservations(props) {
  //displays and gets the data
  return (
    <div className="reservations">
      <p>Name:{props.reservations.name}</p>
      <p>Number of Guest:{props.reservations.number_of_guest}</p>
      <p>Date:{props.reservations.date}</p>
      <p>Time:{props.reservations.time}</p>
      <p>Status:{props.reservations.status}</p>
    </div>
  );
}

export default Reservations;
