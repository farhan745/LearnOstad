import React from 'react'
import Name from './components/Name'
import UserGreeting from './components/UserGreeting'


function App() {
  const active = true;
  const user = {
    isLogin : false,
    name : "Jashim",
    age : 30,
    active: false,
    role:'Student'
  };
  return (
    <div>
      <UserGreeting user={user}/>
      <Name name = {"Fahim"} age={31}/>
      <h1>Hello World</h1>
      {/* <Name name = {"Kamal"} age={28}/> */}

      
      {active ? <h1>Online</h1>:<h1>Offline</h1>}
      </div>
    
  )
}

export default App
