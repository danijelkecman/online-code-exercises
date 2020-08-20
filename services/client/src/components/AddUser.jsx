import React from 'react';

const AddUser = (props) => {
  return (
    <form onSubmit={(event) => props.addUser(event)}>
        <div className="form-group">
            <input 
                name="username" 
                className="form-control input-lg" 
                type="text" 
                placeholder="Enter a username" 
                required
                defaultValue={props.username}
                onChange={props.handleChange}
            />
        </div>
        <div className="form-group"> 
            <input 
                name="email" 
                className="form-control input-lg" 
                type="email" 
                placeholder="Enter an email address" 
                required
                defaultValue={props.email}
                onChange={props.handleChange}
            />
        </div>
        <input type="submit" className="btn btn-primary btn-lg btn-block" value="Submit"/>
    </form>
    )
};
export default AddUser;