import React, {Component} from 'react'
import ReactDOM from 'react-dom'
import Header from './layout/Header'
import Dashboard from './leads/Dashboard'
import Alerts from './layout/Alerts'

import { positions, Provider as AlertProvider } from 'react-alert'
import AlertTemplate from 'react-alert-template-basic'

import { Provider } from 'react-redux';
import store from '../store';


// Alert Options

const alertOptions = {
    timeout: 3000, 
    position: positions.BOTTOM_CENTER
};

export default class App extends Component {
    render (){
        return (
            <Provider store = {store}>
                <AlertProvider template = {AlertTemplate} {...alertOptions}>
                    <>
                    <Alerts />
                        <Header />
                        
                        <div className = "container">
                            <Dashboard />
                        </div>
                    </>
                </AlertProvider>
            </Provider>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));