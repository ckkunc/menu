import React, { useState, useEffect } from "react";
import PhoneForm from './PhoneForm';


function App() {
  useEffect(() => {
    document.title = "Pocket Menu"
  }, []);
  return (
    <div>
      <div class="left-side"><h1>Pocket Menu</h1>
        <h3>Lenoir and Chase's menus, sent to your<br class="break-large"></br>phone every day.<br class="break-small"></br> Quick, convenient, easy.</h3>
      </div>
      <div class="right-side">
        <PhoneForm />
      </div>
    </div>
  );
}

export default App;