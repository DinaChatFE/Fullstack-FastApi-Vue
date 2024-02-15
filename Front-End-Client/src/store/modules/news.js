import api from '../../api/newsApi'
import {  FILTER_BY_CAT_NEWS, FILTER_BY_USER_NEWS, FILTER_NEWS_WITH_PAGE, GET_ALL_NEW, DETAIL_PAGE_NEWS } from '../type'
import pageCalc from '../../utils/paginate'

const token = localStorage.getItem('APP_VUE_TOKEN')
export default {
    state() {
        return {
            news: [],
            is_loaded: true,
            page: 1,
            page_count: 0,
            query: [],
            detail: {}
        }
    },
    getters: {},
    mutations: {
        [GET_ALL_NEW](state, { payload }) {
            state.is_loaded = false
            api.getAllNews(state.query, payload, state.page, token, (res) => {
                state.news = res.data.data
                state.page = res.data.current_page
                state.page_count = pageCalc.getLinkCount(res.data.page_count)
                state.is_loaded = true
            }, (error) => {
                console.log(error);
            })
        },
        [FILTER_NEWS_WITH_PAGE](state, { page }) {
            state.page = page
            console.log(page);
        },
        [FILTER_BY_CAT_NEWS](state, { cat_id }) {
            state.is_loaded = false
            api.getByCategories(cat_id, state.page, token, (res) => {
                state.news = res.data.data
                state.page = res.data.current_page
                state.page_count = pageCalc.getLinkCount(res.data.page_count)
                setTimeout(() => {
                    state.is_loaded = true
                }, 1000);
            }, error => {
                console.error(error);
            })

        },
        [FILTER_BY_USER_NEWS](state, { user_id }) {
            state.is_loaded = false
            api.getByUser(user_id, state.page, token, (res) => {
                state.news = res.data.data
                state.page = res.data.current_page
                state.page_count = pageCalc.getLinkCount(res.data.page_count)
                setTimeout(() => {
                    state.is_loaded = true
                }, 1000);
            }, error => {
                console.log(error);
            })
        },
        [DETAIL_PAGE_NEWS](state, { id }) {
            state.is_loaded = false
            api.getDetail(id, token, (res) => {
                state.detail = res.data
            }, error => {
                console.log(error);
            })
        }
    },
    actions: {
        [GET_ALL_NEW]({ commit }, { payload }) {
            commit(GET_ALL_NEW, { payload })
        },
        [FILTER_NEWS_WITH_PAGE]({ commit }, { page }) {
            commit(FILTER_NEWS_WITH_PAGE, { page })
        },
        [FILTER_BY_USER_NEWS]({ commit }, { user_id }) {
            commit(FILTER_BY_USER_NEWS, { user_id })
        },
        [FILTER_BY_CAT_NEWS]({ commit }, { cat_id }) {
            commit(FILTER_BY_CAT_NEWS, { cat_id })
        },
        [DETAIL_PAGE_NEWS]({commit}, {id}){
            commit(DETAIL_PAGE_NEWS, {id})
        }   
    }
}