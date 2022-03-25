import api from "../../api/auth";
import { ALL_USER, LOGIN, LOG_OUT, PROFILE, REGISTER, UPDATE_USER } from "../type";
import router from '../../router'
export default {
  namespace: true,
  state() {
    return {
      is_auth: false,
      data: [],
      token: localStorage.getItem('APP_VUE_TOKEN'),
      profile: {},
      error_raise: '',
      error_body: [],
      is_loaded: true,
      user: []
    };
  },

  getters: {},
  mutations: {
    [LOGIN](state, { credential }) {
      api.login(credential, (response) => {
        localStorage.setItem("APP_VUE_TOKEN", response.data.token)
        state.is_auth = true
        state.error_raise = ""
        state.token = localStorage.getItem('APP_VUE_TOKEN')
        router.push('/')
      }, (error) => {
        if (error.response.status == 401) {
          state.error_raise = error.response.data.detail
        }
      }
      )
    },
    [PROFILE](state) {
      let token_data = localStorage.getItem('APP_VUE_TOKEN')
      token_data &&
        api.getProfile(token_data, (response) => {
          state.is_auth = true
          state.profile = response.data.data
        }, () => {
          state.profile = {}
          state.is_auth = false
        })
    },
    [REGISTER](state, { credential }) {
      state.is_loaded = false
      api.register({ ...credential, role: "client" }, response => {
        console.log(response);
        router.push('/login')
        state.error_raise = ''
        state.is_loaded = true
      }, error => {
        state.error_raise = error.response.data.detail
        state.is_loaded = true
      })
    },
    [LOG_OUT](state) {
      localStorage.removeItem('APP_VUE_TOKEN')
      state.is_auth = false
      state.token = ''
      state.profile = {}
    },
    [UPDATE_USER](state, { body }) {
      state.is_loaded = false
      api.updateUser(body, state.token, (res) => {
        state.profile = res.data
        setTimeout(() => {
          state.is_loaded = true
      }, 1400);
      },
        (error) => console.log(error))
    },
    [ALL_USER](state){
      api.getAll(state.token, res=> {
          state.user=  res.data
      }, (e)=> {
        console.log(e);
      })
    }
  },
  actions: {
    [LOGIN]({ commit }, { credential }) {
      commit(LOGIN, { credential })
    },
    [PROFILE]({ commit }) {
      commit(PROFILE)
    },
    [REGISTER]({ commit }, { credential }) {
      commit(REGISTER, { credential })
    },
    [LOG_OUT]({ commit }) {
      commit(LOG_OUT)
    },
    [UPDATE_USER]({ commit }, { body }) {
      commit(UPDATE_USER, { body })
    },
    [ALL_USER]({commit}){
      commit(ALL_USER)
    }
  },
};
