<template>
  <!-- This is an example component -->
  <div class="
      bg-white
      shadow-md
      border border-gray-200
      rounded-lg
      max-w-sm
      mb-5
      hover:shadow-2xl
      transition
      duration-300
      overflow-hidden
    ">
    <img class="rounded-t-lg-2 h-40 w-full object-cover overflow-hidden z-0" :src="event_thumbnail" alt="" />
    <div class="p-5 items-start">
      <a href="#">
        <h6 class="
            text-left text-gray-900
            font-bold
            text-xl
            tracking-tight
            mb-2
            line-clamp-2
          ">
          {{ event.title }}
        </h6>
      </a>
      <p class="text-left text-red-400 text-sm font-bold my-3 text-ellipsis">
        {{ event.start_date_format }}
      </p>
      <p class="text-gray-500 text-left text-sm">{{ event.mode }}</p>
      <div class="my-3"></div>
      <div class="flex justify-between">
        <div @click="pushRoute">
          <a class="
              text-white
              bg-blue-700
              hover:bg-blue-800
              focus:ring-4 focus:ring-blue-300
              font-medium
              rounded-lg
              text-sm
              px-3
              py-2
              inline-flex
            " href="#">
            Read more
          </a>
        </div>
        <button v-if="!is_interested_route" @click="toggleInterested" class="
            rounded-2xl
            w-10
            h-8
            flex
            items-center
            justify-center
            bg-gray-100
          " :class="is_interested ? 'text-transparent' : ''">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" :fill="is_interested ? '#B0005C' : 'none'"
            viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from "vue-demi";
import { useStore } from "vuex";
import { LIKE_EVENT } from "../store/type";
import { notify } from "@kyvg/vue3-notification";
import route from "../router";
export default {
  props: ["event"],
  data() {
    const store = useStore();
    return {
      is_interested: this.event.is_interested,
      is_auth: computed(() => store.state.auth.is_auth),
      token: computed(() => store.state.auth.token),
      event_thumbnail: process.env.VUE_APP_STORAGE + this.event.thumbnail,
      toggleEventInterested(id) {
        let obj = {};
        if (this.is_auth) {
          this.is_interested = !this.is_interested;
          obj = { id, is_interested: this.is_interested, user: this.token };
          store.dispatch({
            type: LIKE_EVENT,
            payload: obj,
          });
        } else {
          delete obj.user;
          notify({
            type: "warn",
            title: "Login required",
            text: "You have to login to be able to like the event",
          });
        }
      },
    };
  },
  computed: {
    is_interested_route: function () {
      return route.currentRoute.value.query?.q == 'interested'
    },
  },
  methods: {
    toggleInterested() {
      this.toggleEventInterested(this.event.id);
    },
    pushRoute() {
      route.push({
        name: "Details",
        params: {
          path: "event",
          id: this.event.id,
          data: { name: "welcome" },
          props: this.is_interested,
        },
      });
    },
  },
};
</script>

<style></style>