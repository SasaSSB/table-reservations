import { useState } from "react";
function AddReservations({ updateReservations }) {
  const [formData, setFormData] = useState({
    //form information for user
    name: "",
    number: "",
    date: "",
    time: "",
    status: "",
  });
  const handleChange = (e) => {
    const name = e.target.name;
    const value = e.target.value;
    setFormData({ ...formData, [name]: value });
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    // console.log(formData);
    updateReservations(formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Name:</label>
        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleChange}
          required
        />
      </div>

      <div>
        <label>Number of Guest:</label>
        <input
          type="num"
          name="number_of_guest"
          value={formData.number_of_guest}
          onChange={handleChange}
          required
        />
      </div>

      <div>
        <label>Date:</label>
        <input
          type="text"
          name="date"
          value={formData.date}
          onChange={handleChange}
          required
        />
      </div>

      <div>
        <label>Time:</label>
        <input
          type="text"
          name="time"
          value={formData.phone_number}
          onChange={handleChange}
          required
        />
      </div>

      <div>
        <label>Status:</label>
        <input
          type="text"
          name="status"
          value={formData.status}
          onChange={handleChange}
          required
        />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
}

export default AddReservations;
