import {useState} from 'react'
import '../App.css'
import axios from 'axios'

const Make = () => {

  const [make, setMake] = useState('')
  console.log(make)


  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/make', {"name":make}, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      console.log('Response:', response.data);
      // Handle success
    } catch (error) {
      console.error('Error:', error);
      // Handle error
    }
  };

  return (
    <div className='form'>
      <div className='container'>
        <form onSubmit={handleSubmit}>
          <label for="make">Make</label>
          <input type="text" id="make" name="make" placeholder="Enter Make"
           value={make}
           onChange={e=> setMake(e.target.value)}/>
          <input type="submit" value="Submit"/>
        </form>
      </div>
    </div>
  )
}

export default Make