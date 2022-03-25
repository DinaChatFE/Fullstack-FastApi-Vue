<template>
  <div class="container m-2 mx-auto">
    <form class="border-b-2">
      <input
        type="text"
        v-model="name"
        placeholder="Name"
        class="p-2 input-primary"
      />
      <input
        type="number"
        aria-rowcount="1"
        v-model="price"
        placeholder="Price"
        class="p-2 input-primary"
      />
      <input
        type="number"
        aria-rowcount="1"
        v-model="quantity"
        placeholder="Quantity"
        class="p-2 input-primary"
      />
      <input
        type="text"
        aria-rowcount="1"
        v-model="img"
        placeholder="Image"
        class="p-2 input-primary"
      />
      <input
        @click="addNewData"
        type="submit"
        class="
          inline-flex
          shadow-sm
          duration-100
          focus:outline-none
          focus:ring-4 focus:ring-purple-100
          bg-purple-200
          hover:bg-purple-300
          p-2
          m-1
          uppercase
          rounded-md
          text-purple-800
        "
        value="+ Add"
      />
      <input
        type="reset"
        class="
          inline-flex
          shadow-sm
          duration-100
          focus:outline-none
          focus:ring-4 focus:ring-red-100
          bg-red-200
          hover:bg-red-300
          p-2
          m-1
          uppercase
          rounded-md
          text-red-800
        "
      />
    </form>
    <Product :data="data" :deleteProduct="deleteProduct" />
    <p v-if="!processing && data.length === 0" class="py-8 font-bold text-sm">
      No data found 😭
    </p>
  </div>
  <div v-if="processing">
    <Spinner />
  </div>
</template>

<script>
import Spinner from "./Spinner.vue";
import moment from "moment";
import Product from "./Product.vue";
import { computed } from "vue";
import { useStore } from "vuex";
import {
  ADD_NEW_PRODUCT,
  DELETE_PRODUCT,
  GET_ALL_PRODUCT,
} from "../store/type";

export default {
  components: {
    Spinner,
    Product,
  },
  setup() {
    const store = useStore();
    return {
      name: "",
      quantity: "",
      img: "",
      moment,
      price: "",
      data: computed(() => store.state.products.data),
      processing: computed(() => store.state.products.processing),
      addNewData: function (e) {
        e.preventDefault();
        if (!this.name || !this.quantity || !this.img || !this.price) return;
        store.dispatch({
          type: ADD_NEW_PRODUCT,
          product: {
            name: this.name,
            quantity: this.quantity,
            img: this.img,
            price: this.price,
            created_at: new Date(),
          },
        });
      },
      deleteProduct: function (id) {
        store.dispatch(DELETE_PRODUCT, id);
      },
    };
  },
  created: function () {
    const store = useStore();
    store.dispatch(GET_ALL_PRODUCT);
  },
};
</script>

<style lang="scss" scoped>
</style>