
export const AUTH_ACTION = '[actions] auth user';
export const AUTO_LOGIN_ACTION = '[actions] auto login user';
export const AUTO_LOGOUT_ACTION = '[actions] auto logout user';
export const LOGIN_ACTION = '[actions] login user';
export const LOGOUT_ACTION = '[actions] logout user';
export const SET_AUTO_LOGOUT_MUTATION = '[mutations] auto logout user';
export const SET_USR_TOKEN_DATA_MUTATION = '[mutations] set user token data';
export const AUTHPROFILE = '[mutations] auth profile';
export const LOADING_SPINNER_MUTATION = '[mutations] loading spinner';
export const SIDEBAR_HIDDEN_MUTATION = '[mutations] sidebar hidden';
export const DISABLE_SUBMIT_BUTTON = '[mutations] disable submit button';
export const BREADCRUMB = '[mutations] breadcrumb';
export const GET_USER_TOKEN_GETTER = '[getters] get user token';
export const IS_USER_AUTHENTICATED_GETTER = '[getters] is user authenticated';
export const BASE_URL = process.env.VUE_APP_API ?? 'https://api-event.dinadev.pro/';
