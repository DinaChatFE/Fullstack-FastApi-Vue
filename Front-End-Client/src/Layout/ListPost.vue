<template>
  <div class="overflow-x-hidden bg-gray-100 max-w-7xl mx-auto my-2">
    <div class="py-8 px-7" style="min-height: 800px">
      <div class="container flex justify-between mx-auto">
        <div class="w-full lg:w-8/12">
          <div class="flex items-center justify-between">
            <h1 class="text-xl font-bold text-gray-700 md:text-lg">News</h1>
          </div>
          <no-items v-if="is_loaded && !news.news.length"/>
          <post-list-content-load v-if="!is_loaded" />
          <post-horizontal
            v-else
            v-for="n in news.news"
            v-bind:key="n.id"
            :data="n"
          />

          <paginate v-if="is_loaded && news.news.length" />
        </div>
        <div class="hidden w-4/12 -mx-8 lg:block">
          <author />
          <categories />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from "vue-demi";
import { useStore } from "vuex";
import Paginate from "../components/Paginate.vue";
import PostHorizontal from "../components/PostHorizontal.vue";
import Author from "../Layout/Patial/Author.vue";
import Categories from "../Layout/Patial/Categories.vue";
import {
  FILTER_BY_CAT_NEWS,
  FILTER_BY_USER_NEWS,
  GET_ALL_NEW,
} from "../store/type";
import { FILTER_NEWS_WITH_PAGE } from "../store/type";
import router from "../router";
import PostListContentLoad from "../components/PostListContentLoad.vue";
import NoItems from '../components/NoItems.vue';

export default {
  components: {
    PostHorizontal,
    Author,
    Categories,
    Paginate,
    PostListContentLoad,
    NoItems,
  },
  data() {
    const store = useStore();
    return {
      news: computed(() => store.state.news),
      is_loaded: computed(() => store.state.news.is_loaded),
      route: {},
      pageQuery: "",
      fetch() {
        store.dispatch({ type: GET_ALL_NEW, payload: "" });
      },
      filterPage(p) {
        store.dispatch({ type: FILTER_NEWS_WITH_PAGE, page: p });
      },
      filterByUser(u) {
        store.dispatch({ type: FILTER_BY_USER_NEWS, user_id: u });
      },
      filterByCategories(cat) {
        store.dispatch({ type: FILTER_BY_CAT_NEWS, cat_id: cat });
      },
      dispatchFetch(page) {
        store.dispatch({ type: FILTER_NEWS_WITH_PAGE, page });
      },
    };
  },
  async created() {
    this.fetch();
    this.$nextTick(async () => {
      this.route = router.currentRoute.value.query;
      let to = router.currentRoute.value;
      if (to.query?.category) {
        await this.filterByCategories(to.query.category);
      } else if (to.query?.admin) {
        await this.filterByUser(to.query.admin);
      } else {
        await this.fetch();
      }
    });
  },
  watch: {
    $route(to) {
      if (to.query?.category) {
        this.filterByCategories(to.query.category);
      } else if (to.query?.admin) {
        this.filterByUser(to.query.admin);
      } else {
        this.fetch();
      }
    },
    route: {
      handler(val) {
        console.log(val);
      },
      deep: true,
    },
  },
};
</script>

<style>
</style>