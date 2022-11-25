import './App.css'
import PostData  from './Services/PostData';
import {useState,useEffect} from 'react'

function App() {
  const [first, setfirst] = useState('')


  

  const handleSubmit =async()=>{
    console.log("hii");
    let response =await PostData('/add',{todo:first})
    console.log(response);
  }

  const handleView = async()=>{
    let response = await PostData('/view',{})
    console.log(response);
  }
  return (
    <div className="App">
      <h1>Todo App</h1>
      <div className="input-container">
        <input type="text" value={first} onChange={(e)=>setfirst(e.target.value)} />
        <button onClick={handleSubmit}>Add</button>
      </div>
      <div className="list_container">
        <table className="table-container">
          <tr>
          <th>Index</th>
          <th>Todo</th>
          <th>Edit</th>
          <th>Delete</th>
          </tr>
          <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
          </tr>
        </table>
      </div>
    </div>
  );
}

export default App;
