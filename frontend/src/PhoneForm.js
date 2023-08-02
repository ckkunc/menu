// Import the useState hook and the React object from the 'react' module
import React, { useState } from 'react';
// Import the axios module for making HTTP requests
import axios from 'axios';

// Define a new PhoneForm component
function PhoneForm() {
  // Use the useState hook to create a state variable called phoneNumber and a function called setPhoneNumber for updating it
  const [phoneNumber, setPhoneNumber] = useState('');

  // Define a function called formatPhoneNumber that gets called when the value of the input field changes
  const formatPhoneNumber = (event) => {
    // Get the current value of the input field
    let inputValue = event.target.value;
    // Initialize a variable called formattedValue to store the formatted phone number
    let formattedValue = '';
    
    // Remove any non-digit characters from the input value
    inputValue = inputValue.replace(/\D/g, '');
    // Truncate the input value to a maximum of 10 characters
    inputValue = inputValue.slice(0, 10);
    
    // If the input value contains more than 3 characters, format it as a phone number
    if (inputValue.length > 3) {
      // Add the first three characters of the input value to formattedValue, surrounded by parentheses
      formattedValue += `(${inputValue.slice(0, 3)})`;
      // If the input value contains more than 3 characters, add the next three characters to formattedValue
      if (inputValue.length > 3) {
        formattedValue += `${inputValue.slice(3, 6)}`;
      }
      // If the input value contains more than 6 characters, add a hyphen and the remaining characters to formattedValue
      if (inputValue.length > 6) {
        formattedValue += `-${inputValue.slice(6)}`;
      }
    } else {
      // If the input value contains 3 or fewer characters, set formattedValue to the input value
      formattedValue = inputValue;
    }
    
    // Update the phoneNumber state variable with the formatted phone number
    setPhoneNumber(formattedValue);
  };  
  
  // Define an event handler function called handleSubmit that gets called when the form is submitted
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      // Remove any non-digit characters from the phoneNumber state variable
      let unformattedPhoneNumber = phoneNumber.replace(/\D/g, '');
      // Use axios to send a POST request to the /api/phone-numbers/ URL with the unformatted phone number as the request data
      await axios.post('http://127.0.0.1:8000/api/phone-numbers/', { number: unformattedPhoneNumber });
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
        type="tel"
        value={phoneNumber}
        onChange={(event) => formatPhoneNumber(event)}
        placeholder="(123)456-7890"
      />
      <button type="submit" disabled={phoneNumber.replace(/\D/g, '').length !== 10}>
        <span>Submit</span>
      </button>
    </form>
  );
}

// Export the PhoneForm component as the default export of this module
export default PhoneForm;
