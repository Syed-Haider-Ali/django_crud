import React from 'react'
import '../App.css'

const AddVehicle = () => {
  return (
    <div className='form'>
      <div className='container'>
        <form action="/action_page.php">
          <label for="name">Vechile Name</label>
          <input type="text" id="name" name="name" placeholder="Enter Name"/>

          <label for="make">Make</label>
          <select id="make" name="make">
            <option value="1">Honda</option>
            <option value="2">Toyota</option>
            <option value="3">Suzuki</option>
          </select>

          <label for="model">Model</label>
          <input type='number' id="model" name="model" placeholder="e.g. 2011"/>

          <label for="color">Color</label>
          <select id="color" name="color">
            <option value="yellow">Yellow</option>
            <option value="red">Red</option>
            <option value="blue">Blue</option>
            <option value="green">Green</option>
            <option value="orange">Orange</option>
            <option value="purple">Purple</option>
            <option value="pink">Pink</option>
            <option value="black">Black</option>
            <option value="white">White</option>
            <option value="gray">Gray</option>
            <option value="brown">Brown</option>
            <option value="cyan">Cyan</option>
          </select>

          <input type="submit" value="Submit"/>
        </form>
      </div>
    </div>
  )
}

export default AddVehicle