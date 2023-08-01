// Import the useState hook and the React object from the 'react' module
import React, { useState } from 'react';
// Import the axios module for making HTTP requests
import axios from 'axios';

// Define a new PhoneForm component
function PhoneForm() {
  // Use the useState hook to create a state variable called phoneNumber and a function called setPhoneNumber for updating it
  const [phoneNumber, setPhoneNumber] = useState('');

  // Define an event handler function called handleSubmit that gets called when the form is submitted
  const handleSubmit = async (event) => {
    // Prevent the default form submission behavior
    event.preventDefault();
    try {
      /* Use axios to send a POST request to the /api/phone-numbers/ URL, the URL of the API endpoint in the Django app,
      with the phone number as the request data. When the Django app receives this POST request, it will create a new 
      phone number in the database. */
      await axios.post('http://127.0.0.1:8000/api/phone-numbers/', { number: phoneNumber });
      // Clear the phoneNumber state variable
      setPhoneNumber('');
    } catch (error) {
      // Log any errors to the console
      console.error(error);
    }
  };

  // Render the form
  return (
    <form onSubmit={handleSubmit}>
      <input
        type="number"
        value={phoneNumber}
        onChange={(event) => setPhoneNumber(event.target.value)}
        oninput="formatPhoneNumber(this)"
        placeholder="(123)456-7890"
      />
      <button type="submit">
        <span>Submit</span>
      </button>
    </form>
  );
}

// Export the PhoneForm component as the default export of this module
export default PhoneForm;
