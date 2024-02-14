<template>
  <div class="overflow-x-hidden bg-gray-100 max-w-7xl mx-auto my-2">
    <div class="py-8 px-7">
      <div class="container flex justify-between mx-auto">
        <div class="w-full lg:w-8/12">
          <div class="flex items-center justify-between my-4">
            <h1 class="text-xl font-bold text-gray-700 md:text-lg">Event</h1>
            <div>
              <select
                class="
                  w-full
                  border-gray-300
                  rounded-md
                  shadow-sm
                  focus:border-indigo-300
                  focus:ring
                  focus:ring-indigo-200
                  focus:ring-opacity-50
                "
              >
                <option>Latest</option>
                <option>Last Week</option>
              </select>
            </div>
          </div>
          <!-- <post-list-content-load v-if="!is_loaded"/> -->
          <event-list />
          <event-list />
          <event-list />
          <event-list />

          <paginate v-if="is_loaded" />
        </div>
        <div class="hidden w-4/12 -mx-8 lg:block">
          <author />
          <categories />
          <recent-post />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from "vue-demi";
import { useStore } from "vuex";
import Paginate from "../components/Paginate.vue";
import EventList from "../components/EventList.vue";
import Author from "../Layout/Patial/Author.vue";
import Categories from "../Layout/Patial/Categories.vue";
import RecentPost from "../Layout/Patial/RecentPost.vue";
import { FILTER_BY_CAT_NEWS, FILTER_BY_USER_NEWS, GET_ALL_NEW } from "../store/type";
import { FILTER_NEWS_WITH_PAGE } from "../store/type";
import router from "../router";

export default {
  components: { Author, Categories, RecentPost, Paginate, EventList },
  data() {
    const store = useStore();
    return {
      news: computed(() => store.state.news),
      is_loaded: computed(()=> store.state.news.is_loaded),
      route: {},
      pageQuery: "",
      fetch() {
        store.dispatch({ type: GET_ALL_NEW, payload: "" });
      },
      filterPage(p) {
        store.dispatch({ type: FILTER_NEWS_WITH_PAGE, page: p });
      },
      filterByUser(u){
        store.dispatch({type: FILTER_BY_USER_NEWS, user_id: u})
      },
      filterByCategories(cat){
        store.dispatch({type: FILTER_BY_CAT_NEWS, cat_id: cat})
      },
      dispatchFetch(page) {
        store.dispatch({ type: FILTER_NEWS_WITH_PAGE, page });
      },
    };
  },
  created() {
    this.fetch();
    this.route = router.currentRoute.value.query;
  },
  watch: {
    $route (to){
        if(to.query?.category){
          this.filterByCategories(to.query.category)
        }else if (to.query?.admin){
          this.filterByUser(to.query.admin)
        }else{
          this.fetch()
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