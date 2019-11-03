import ReactDOM from 'react-dom';
import React, {Component} from 'react';
class Form1 extends Component{
    render(){
        return (
            <div class="form">
                <form action="http://10.225.125.24:5000/result" method="get">
                    Place: <input type="text" name="place"/>
                    <input type="submit" value="Submit"/>
                </form>
            </div>
        );
    }
}
export default Form1;