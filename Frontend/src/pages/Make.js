import React from 'react'
import '../App.css'
import {Link} from 'react-router-dom'

const Make = () => {
  return (
    <div className="container">
        <h1>Make page</h1>

        <Link to="/make/add" className='button'> Add New </Link>
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

export default Make