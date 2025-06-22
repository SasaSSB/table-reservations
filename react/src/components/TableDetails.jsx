import Reservations from "./Reservations";

function TableDetails(props) {
  //console.log(props.Reservations);
  return (
    <div className="Table">
      {props.reservations.map((reservations) => (
        <Reservations reservations={reservations} />
      ))}
    </div>
  );
}

export default TableDetails;
