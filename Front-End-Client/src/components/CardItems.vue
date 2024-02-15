<template>
  <div class="bg-gray-100 min-h-screen py-32 px-10 mx-auto max-w-2/3" style="max-width: 1400px">
    <h1 class="text-left font-bold text-2xl">
      Location at <span class="text-red-500">Cambodia</span>
    </h1>
    <div class="my-4"></div>
    <div class="
        border-b border-gray-200
        dark:border-gray-700
        mb-4
        flex
        justify-between
        items-center
      ">
      <ul class="flex overflow-x-scroll -mb-px" id="myTab" data-tabs-toggle="#myTabContent" role="tablist">
        <li class="mr-2" role="presentation">
          <button @click="filter('disable', 'all')" class="inline-block text-gray-500 hover:text-gray-600 rounded-t-lg py-4 px-4 text-sm font-medium text-center border-transparent border-b-2 dark:text-gray-400 dark:hover:text-gray-300
            " :class="queryParams == 'all' || queryParams == undefined
              ? 'border-blue-500 text-blue-500'
              : ''
              " id="profile-tab" data-tabs-target="#profile" type="button" role="tab" aria-controls="profile"
            aria-selected="false">
            All
          </button>
        </li>
        <li class="mr-2" role="presentation" v-if="is_auth">
          <button @click="filterInterested()" class="inline-block text-gray-500 hover:text-gray-600 rounded-t-lg py-4 px-4 text-sm font-medium text-center border-transparent border-b-2 dark:text-gray-400 dark:hover:text-gray-300 active
            " :class="queryParams == 'interested' ? 'border-blue-500 text-blue-500' : ''
              " id="dashboard-tab" data-tabs-target="#dashboard" type="button" role="tab" aria-controls="dashboard"
            aria-selected="true">
            Interested
          </button>
        </li>
        <li class="mr-2" role="presentation">
          <button @click="filter('mode', 'Online')" class="inline-block text-gray-500 hover:text-gray-600 rounded-t-lg py-4 px-4 text-sm font-medium text-center border-transparent border-b-2 dark:text-gray-400 dark:hover:text-gray-300
            " id="settings-tab" data-tabs-target="#settings" type="button" role="tab" aria-controls="settings"
            aria-selected="false" :class="queryParams == 'online' ? 'border-blue-500 text-blue-500' : ''
              ">
            Online
          </button>
        </li>
        <li role="presentation">
          <button @click="filter('mode', 'Offline')" class="inline-block text-gray-500 hover:text-gray-600 hover:border-gray-300 rounded-t-lg py-4 px-4 text-sm font-medium text-center border-transparent border-b-2 dark:text-gray-400 dark:hover:text-gray-300
            " :class="queryParams == 'Offline' ? 'border-blue-500 text-blue-500' : ''
              " id="contacts-tab" data-tabs-target="#contacts" type="button" role="tab" aria-controls="contacts"
            aria-selected="false">
            Offline
          </button>
        </li>
      </ul>
      <p class="shrink-0 whitespace-nowrap">Page {{ page }} / {{ event_count }}</p>
    </div>
    <div class="my-10"></div>

    <div class="responsive w-full overflow-hidden">
      <card-content-load v-if="!is_loaded" />
    </div>

    <no-items v-if="is_loaded && !event_items.length" />

    <div class="
        grid grid-cols-1
        md:grid-cols-3
        lg:grid-cols-4
        md:gap-x-4
        xl-grid-cols-4
        gap-y-10 gap-x-6
      ">

      <card v-for="event in event_items" v-bind:key="event.id" :event="event" />
    </div>
    <div class="my-2"></div>
    <button @click="fetchMore" class="
        bg-gray-200
        hover:bg-gray-300
        duration-75
        border-sm
        text-center
        rounded-md
        p-3
        px-20
      " :class="!next ? 'hidden' : ''">
      <span v-if="is_loaded">More</span>
      <div v-else class="w-4 h-4 mt-1 border-4 border-blue-600 rounded-full loader"></div>
    </button>
  </div>
</template>

<script>
import { computed } from "vue-demi";
import { useStore } from "vuex";
import Card from "./Card.vue";
import {
  EVENT_BY_INTERESTED,
  FETCH_MORE_EVENT,
  FILTER_EVENT,
  GET_ALL_EVENT,
} from "../store/type";
import CardContentLoad from "../components/CardContentLoad.vue";
import router from "../router";
import NoItems from './NoItems.vue';

export default {
  components: { Card, CardContentLoad, NoItems },
  props: ["event_items"],
  data() {
    const store = useStore();

    return {
      queryParams: "",
      is_loaded: computed(() => store.state.event.is_loaded),
      dataList: computed(() => store.state.event.event),
      is_auth: computed(() => store.state.auth.is_auth),
      next: computed(() => store.state.event.next),
      page: computed(() => store.state.event.page),
      event_count: computed(() => store.state.event.event_count),
      token: computed(() => store.state.auth.token),
      query: computed(() => store.state.event.query),
      fetchMore() {
        store.dispatch(FETCH_MORE_EVENT);
      },
      filter(key, value) {
        let obj = [{ key, value }];
        if (key == "disable") obj = [];
        router.replace({ name: "Home", query: { q: value } });
        store.dispatch({ type: FILTER_EVENT, query: obj });
        store.dispatch({ type: GET_ALL_EVENT, payload: this.token });
        setTimeout(() => {
          this.queryParams = router.currentRoute.value.query.q;
        }, 200);
      },
      fetchAll() {
        store.dispatch({ type: GET_ALL_EVENT, payload: this.token });
      },
      filterInterested() {
        router.replace({ name: "Home", query: { q: "interested" } });
        store.dispatch(EVENT_BY_INTERESTED);
        setTimeout(() => {
          this.queryParams = router.currentRoute.value.query.q;
        }, 200);
      },
    };
  },
  async created() {
    this.queryParams = this.$route.query?.q;
    this.$nextTick(async () => {
      switch (this.queryParams) {
        case "interested":
          await this.filterInterested();
          break;
        case "offline":
          await this.filter("mode", "offline");
          break;
        case "online":
          this.filter("mode", "online");
          break;
        default:
          this.fetchAll();
      }
    });
  },
  methods: {
    fetchMoreEvent() {
      this.fetchMore();
    },
  },
};
</script>

<style>
@keyframes loader-rotate {
  0% {
    transform: rotate(0);
  }

  100% {
    transform: rotate(360deg);
  }
}

.loader {
  border-right-color: transparent;
  animation: loader-rotate 1s linear infinite;
}
</style>