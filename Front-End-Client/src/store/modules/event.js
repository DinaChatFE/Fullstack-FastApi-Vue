import api from '../../api/eventApi'
import { GET_ALL_EVENT, FETCH_MORE_EVENT, FILTER_EVENT,  LIKE_EVENT, DETAIL_PAGE_EVENT, REGISTER_EVENT, EVENT_BY_INTERESTED, REMOVE_INTERESTED } from '../type'
import paginate from '../../utils/paginate'

export default {
    namespace: true,
    state() {
        return {
            event: [],
            page: 1,
            raiseError: "",
            filter_by: "all",
            is_loaded: true,
            event_count: 0,
            next: true,
            query: [],
            detail: {},
            message: '',
            registerEventMessage: ''
        }
    },
    getters: {

    },
    mutations: {
        [GET_ALL_EVENT](state, { payload }) {
            let token = localStorage.getItem("APP_VUE_TOKEN")
            state.page = 1
            state.is_loaded = false
            state.next = true
            api.getAllEvent(state.query, payload, state.page, token, (response) => {
                if (response.data.page_count < process.env.VUE_APP_COUNT_PAGE) state.next = false
                state.event = response.data.data
                state.event_count = paginate.getLinkCount(response.data.page_count)
                state.is_loaded = true
            }, (error) => {
                state.raiseError = error.response.data
            })
        },
        [FETCH_MORE_EVENT](state) {
            let token = localStorage.getItem("APP_VUE_TOKEN")

            state.is_loaded = false
            api.getAllEvent(state.query, state.token, state.page, token, (response) => {
                state.event_count = paginate.getLinkCount(response.data.page_count)
                if (state.page > paginate.getLinkCount(response.data.page_count) - 1) {
                    state.next = false
                } else {
                    state.page++;
                }
                response.data.data.forEach(v => state.event.push(v))
                state.is_loaded = true
            }, (error) => {
                console.log(error);
                state.is_loaded = true
            })
        },
        [FILTER_EVENT](state, { query }) {

            state.is_loaded = false
            state.query = query
        },
        [LIKE_EVENT](state, { payload }) {
            let token = localStorage.getItem("APP_VUE_TOKEN")
            api.postPreference(payload, token, (res) => {
                state.message = res?.message
            }, error => console.log(error))
        },
        [DETAIL_PAGE_EVENT](state, { id }) {
            let token = localStorage.getItem("APP_VUE_TOKEN")

            state.is_loaded = false
            api.getDetail(id, token, (res) => {
                state.detail = res.data
            }, error => {
                console.log(error);
            })
        },
        [REMOVE_INTERESTED](state){
            state.event = state.event.map(elem => {
                elem.is_interested = false
            });
        },
        [EVENT_BY_INTERESTED](state) {

            state.is_loaded = false
            let token = localStorage.getItem("APP_VUE_TOKEN")
            api.filterByEventInterested(token, state.page, (res) => {
                state.is_loaded = true
                state.event = res.data.data
                state.event_count = paginate.getLinkCount(res.data.page_count)
                if (state.page > paginate.getLinkCount(res.data.page_count) - 1) {
                    state.next = false
                } else {
                    state.page++;
                }
            }, error => {
                console.log(error);
            })
        },
        [REGISTER_EVENT](state, { id }) {
            let token = localStorage.getItem("APP_VUE_TOKEN")

            state.is_loaded = false
            api.registerEventApi(id, token, (res) => {
                console.log(res);
                state.is_loaded = true
                state.registerEventMessage = "You have been register event"
            }, error => {
                console.error(error.response.data);
            })
        }
    },
    actions: {
        [GET_ALL_EVENT]({ commit }, { payload }) {
            commit(GET_ALL_EVENT, { payload })

        },
        [FETCH_MORE_EVENT]({ commit }) {
            commit(FETCH_MORE_EVENT)
        },
        [FILTER_EVENT]({ commit }, { query }) {
            commit(FILTER_EVENT, { query })
        },
        [LIKE_EVENT]({ commit }, { payload }) {
            commit(LIKE_EVENT, { payload })
        },
        [DETAIL_PAGE_EVENT]({ commit }, { id }) {
            commit(DETAIL_PAGE_EVENT, { id })
        },
        [REGISTER_EVENT]({ commit }, { id }) {
            commit(REGISTER_EVENT, { id })
        },
        [EVENT_BY_INTERESTED]({ commit }) {
            commit(EVENT_BY_INTERESTED)
        },
        [REMOVE_INTERESTED]({commit}){
            commit(REMOVE_INTERESTED)
        }
    }
}