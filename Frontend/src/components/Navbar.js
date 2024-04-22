import React from 'react'
import '../App.css';
import {Link} from 'react-router-dom'


const Navbar = () => {
  return (
    <>
    <navbar class="navbar">
        <div class="container">
            <div class="logo"><Link to='/'>JS Motors</Link></div>
           <ul>
            <li><Link to="/make">Make</Link></li>
            <li><Link to="/vehicle">Vechiles</Link></li>
           </ul>
        </div>
    </navbar>
    </>
  )
}

export default Navbar