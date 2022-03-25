import api from "../../api";
import { ADD_NEW_PRODUCT, DELETE_PRODUCT, GET_ALL_PRODUCT } from "../type";
export default {
  namespace: true,
  state() {
    return {
      data: [],
      processing: true,
    };
  },

  getters: {},
  mutations: {
    [GET_ALL_PRODUCT](state) {
      api.getProductApi(res => {
        state.data = res.data;
        state.processing = false;
      });
    },
    addNewProduct(state, { product }) {
      state.data = [...state.data, product];
    },
    [ADD_NEW_PRODUCT](state, { product }) {
      state.processing = true;
      api.addNewProductApi(product.product, function() {
        api.getProductApi(res => {
          state.data = res.data;
          state.processing = false;
        });
      });
    },
    deleteProduct(state, id) {
      state.data = state.data.filter(i => i.id !== id);
    },
    [DELETE_PRODUCT](state, id) {
      api.deleteProductApi(id, function() {
        state.data = state.data.filter(i => i.id !== id);
      });
    },
  },
  actions: {
    [GET_ALL_PRODUCT]({ commit }) {
      commit(GET_ALL_PRODUCT);
    },
    [ADD_NEW_PRODUCT]({ commit }, product) {
      commit(ADD_NEW_PRODUCT, { product });
    },
    [DELETE_PRODUCT]({ commit }, id) {
      commit(DELETE_PRODUCT, id);
    },
  },
};
