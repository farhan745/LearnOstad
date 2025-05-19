import React from 'react'

function UserGreeting({user}) {
  return (
    <div>
      <h1>
        {user.isLogin ? `Welcome , ${user.name}` : `Please login`}
      </h1>
      {
        (()=>{
            if(!user.isLogin){
                return null;
                }
            if(user.role==="Student"){
                return <p style="width">Hope your studies are going well</p>
            }
            if(user.role==="Teacher"){
                return <p>
                    Hope your classes are going well
                </p>
            }
})
      }
    </div>
  )
}

export default UserGreeting
