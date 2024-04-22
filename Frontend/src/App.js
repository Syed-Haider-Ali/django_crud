import './App.css';
import {Routes, Route} from 'react-router-dom'

import Make from './pages/Make'
import Main from './pages/Main'
import Vehicle from './pages/Vehicle'

import Navbar from './components/Navbar'
import AddMake from './components/AddMake'
import AddVehicle from './components/AddVehicle'



function App() {
  return (
   <>
    <Navbar/>
      <Routes>
        <Route path='/' element={<Main/>}/>

        <Route path='/make' element={<Make/>}/>
        <Route path='/make/add' element={<AddMake/>}/>

        <Route path='/vehicle' element={<Vehicle/>}/>
        <Route path='/vehicle/add' element={<AddVehicle/>}/>

      </Routes>
   </>
  );
}

export default App;
