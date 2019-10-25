import React from 'react'
import './Login.scss'

export default class Login extends React.Component {
    render() {
        return (
            <div className="login">
                <div className="row banner-part">
                    <div className="col text-center">
                        <img
                            className="login-logo"
                            src={require('./../../assets/default-monochrome.svg')}
                            alt=""
                        />
                    </div>
                </div>
                <div className="row login-part">
                    <div className="col">
                        <div className="row">
                            <div className="col-8 left-login-part">
                                <div>
                                    <img
                                        src={require('./../../assets/bck_login.jpg')}
                                        alt=""
                                    />
                                </div>
                            </div>
                            <div className="col right-login-part">
                                <div class="right-login-part-content">
                                    <div class="row">
                                        <div class="col">
                                            <h3 className="">
                                                Se connecter à son espace
                                                MyStudio
                                            </h3>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}
