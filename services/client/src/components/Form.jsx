import React from 'react';

const Form = (props) => {
    return (
        <div>
            <h1>{props.formType}</h1>
            <hr/><br/>
            <form onSubmit={(event) => props.handleUserFormSubmit(event)}>
                {props.formType === 'Register' && 
                    <div className="form-group">
                        <input
                            name="username"
                            className="form-control input-lg"
                            type="text"
                            placeholder="Enter a username"
                            defaultValue={props.formData.username}
                            onChange={props.handleFormChange}
                        />
                    </div>
                }
                <div className="form-group">
                    <input
                        name="email"
                        className="form-control input-lg"
                        type="email"
                        placeholder="Enter an email address"
                        defaultValue={props.formData.email}
                        onChange={props.handleFormChange}
                    />
                </div>
                <div className="form-group">
                    <input
                        name="password"
                        className="form-control input-lg"
                        type="password"
                        placeholder="Enter a password"
                        defaultValue={props.formData.password}
                        onChange={props.handleFormChange}
                    />
                </div>
                <input
                    type="submit"
                    className="btn btn-primary btn-lg btn-block"
                    value="Submit"
                />
            </form>
        </div>
    ) 
};

export default Form;