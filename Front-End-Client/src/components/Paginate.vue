<template>
  <div class="mt-8">
    <div class="flex">
      <a
        v-if="current_page != 1"
        @click="previous"
        href="#"
        aria-disabled="true"
        class="px-3 py-2 mx-1 font-medium bg-white rounded-md hover:bg-blue-500 hover:text-white"
        :class="
          current_page == 1
            ? 'cursor-not-allowed text-gray-500'
            : 'text-gray-700'
        "
      >
        previous
      </a>

      <a
        v-for="p in Array(page_count).keys()"
        v-bind:key="p"
        @click="linkPage(p + 1)"
        href="#"
        class="
          px-3
          py-2
          mx-1
          font-medium
          bg-white
          rounded-md
           hover:text-white
          duration-200
        "
        :class="
          current_page == p + 1 ? 'bg-blue-600 text-white hover:bg-white-500' : 'text-gray-700 hover:bg-blue-500'
        "
      >
        {{ p + 1 }}
      </a>
      <a
        @click="next"
        class="
          px-3
          py-2
          mx-1
          font-medium
          bg-white
          rounded-md
          hover:bg-blue-500 hover:text-white
        "
        href="#"
        v-if="current_page != page_count"
        :class="
          current_page == page_count
            ? 'cursor-not-allowed text-gray-500'
            : 'text-gray-700'
        "
      >
        Next
      </a>
    </div>
  </div>
</template>

<script>
import { computed } from "vue-demi";
import { useStore } from "vuex";
// import router from "../router";
import { FILTER_NEWS_WITH_PAGE } from "../store/type";
export default {
  data() {
    const store = useStore();
    return {
      page_count: computed(() => store.state.news.page_count),
      current_page: computed(() => store.state.news.page),
      dispatchFetch(page) {
        store.dispatch({ type: FILTER_NEWS_WITH_PAGE, page });
      },
      pNext() {
        store.dispatch({
          type: FILTER_NEWS_WITH_PAGE,
          page: this.current_page + 1,
        });
      },
      pPrevious() {
        store.dispatch({
          type: FILTER_NEWS_WITH_PAGE,
          page: this.current_page - 1,
        });
      },
    };
  },
  created() {
   /*  var qPage = router.currentRoute.valu */
   /*  qPage && this.dispatchFetch(qPage); */
  },
  methods: {
    linkPage(p) {
      this.dispatchFetch(p);
    },
    next() {
      this.pNext();
    },
    previous() {
      this.pPrevious();
    },
  },
};
</script>

<style>
</style>