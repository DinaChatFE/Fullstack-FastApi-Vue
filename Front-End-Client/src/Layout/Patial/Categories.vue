<template>
  <div class="px-8 mt-10 text-left">
    <h1 class="mb-4 text-lg font-bold text-gray-700">Categories</h1>
    <div
      class="
        flex flex-col
        max-w-sm
        px-4
        py-6
        mx-auto
        bg-white
        rounded-lg
        shadow-md
      "
    >
      <ul>
        <li class="list-none py-1" v-for="cat in data" v-bind:key="cat.id">
          <a
            @click="appendPush(cat.id)"
            href="#"
            class="
              mx-1
              font-bold
              text-gray-700
              hover:text-gray-600 hover:underline
            "
            >{{ cat.name }}
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { computed } from "vue-demi";
import { useStore } from "vuex";
import { FETCH_CATEGORY, FILTER_NEWS_WITH_PAGE } from "../../store/type";
import router from "../../router";
// import router from '../../router';

export default {
  data() {
    const store = useStore();
    return {
      data: computed(() => store.state.categories.categories),
      getAll() {
        store.dispatch(FETCH_CATEGORY);
      },
      dispatchFetch(page) {
        store.dispatch({ type: FILTER_NEWS_WITH_PAGE, page });
      },
    };
  },
  methods: {
    appendPush(push) {
      router.push({ query: { category: push } });
      this.dispatchFetch(1);
    },
  },
  created() {
    this.getAll();
  },
};
</script>

<style>
</style>