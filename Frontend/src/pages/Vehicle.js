import React from 'react'
import '../App.css'
import {Link} from 'react-router-dom'

const Vehicle = () => {
  return (
    <div className="container">
    <h1>Vechiles page</h1>

    <Link to="/vehicle/add" className='button'> Add New </Link>
    <br/>

    <div className="listing">
        <div className="card">
            <h6>card content</h6>
            <p>goes here</p>
        </div>
        <div className="card">
            <h6>card content</h6>
            <p>goes here</p>
        </div>
        <div className="card">
            <h6>card content</h6>
            <p>goes here</p>
        </div>
    </div>

</div>
  )
}

export default Vehicle