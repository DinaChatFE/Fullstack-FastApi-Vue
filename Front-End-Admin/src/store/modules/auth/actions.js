import axios from "axios";
import { LOGIN_ACTION, SET_USR_TOKEN_DATA_MUTATION, LOADING_SPINNER_MUTATION, LOGOUT_ACTION, AUTH_ACTION, AUTO_LOGIN_ACTION, AUTO_LOGOUT_ACTION, SET_AUTO_LOGOUT_MUTATION, BASE_URL } from "../../storeconstants";

export default {
    [LOGOUT_ACTION](context) {
        context.commit(SET_USR_TOKEN_DATA_MUTATION, {
            token: null,
            refreshToken: null,
            expiresIn: null,
        });
        localStorage.removeItem('authData');
    },
    [AUTO_LOGOUT_ACTION](context) {
        context.dispatch(LOGOUT_ACTION);
        context.commit(SET_AUTO_LOGOUT_MUTATION);
    },
    [AUTO_LOGIN_ACTION](context) {
        let authData = localStorage.getItem("authData");
        if (authData) {
            context.commit(SET_USR_TOKEN_DATA_MUTATION, JSON.parse(authData));
        }
    },
    async [LOGIN_ACTION](context, payload) {
        return context.dispatch(AUTH_ACTION, {
            ...payload,
            url: BASE_URL + 'auth/login/'
        });
    },
    async [AUTH_ACTION](context, payload) {
        let data = {
            email: payload.phone,
            password: payload.password,
            role: payload.role
        };
        // context.commit(LOADING_SPINNER_MUTATION, true, { root: true });
        // context.commit(LOADING_SPINNER_MUTATION, true);
        try {
            let response = await axios.post(payload.url, data);

            if (response.status === 200) {

                // setTimeout(() => {
                //     context.dispatch(AUTO_LOGOUT_ACTION);
                // }, (response.data.expires_in * 1000));

                console.log(response);
                let authData = {
                    token: response.data.token,
                    profile: response.data.user.profile
                    // refreshToken: response.data.refresh_token,
                    // expiresIn: response.data.expires_in,
                };
                context.commit(SET_USR_TOKEN_DATA_MUTATION, authData);
                localStorage.setItem("authData", JSON.stringify(authData));
            }
        } catch (error) {
            // context.commit(LOADING_SPINNER_MUTATION, false, { root: true });
            throw error.response;
        }
        // context.commit(LOADING_SPINNER_MUTATION, false, { root: true });
    }
};