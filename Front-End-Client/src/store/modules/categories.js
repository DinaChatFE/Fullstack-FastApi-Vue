import {FETCH_CATEGORY} from '../type'
import api from '../../api/categoriesApi'

export default {
    state(){
        return {
            categories: []
        }
    },
    mutations: {
        [FETCH_CATEGORY](state){
            api.getAll(res=> {
                state.categories = res.data
            }, ()=> {

            })
        }
    },
    actions: {
        [FETCH_CATEGORY]({commit}){
            commit(FETCH_CATEGORY)
        }
    }
}