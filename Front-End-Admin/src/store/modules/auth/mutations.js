import { SET_USR_TOKEN_DATA_MUTATION, LOADING_SPINNER_MUTATION, SET_AUTO_LOGOUT_MUTATION, SIDEBAR_HIDDEN_MUTATION } from "../../storeconstants";

export default {
    [SET_USR_TOKEN_DATA_MUTATION](state, payload) {
        state.token = payload.token;
        state.refreshToken = payload.refreshToken;
        state.expiresIn = payload.expiresIn;
        state.autoLogout = false
    },
    [LOADING_SPINNER_MUTATION](state, payload) {
        state.isLoading = payload;
    },
    [SIDEBAR_HIDDEN_MUTATION](state, payload) {
        state.sidebarHidden = payload;
    },
    [SET_AUTO_LOGOUT_MUTATION](state) {
        state.autoLogout = true;
    }
};