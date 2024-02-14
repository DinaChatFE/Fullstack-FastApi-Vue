<template>
  <main class="relative w-full mx-auto bg-white">
    <div class="relative -mx-4 top-0 pt-[17%] overflow-hidden">
      <img class="
          absolute
          inset-0
          object-cover object-top
          w-full
          h-full
          filter
          blur
        " :src="img_background" alt="" />
    </div>

    <div class="mt-[-10%] mx-auto px-4" style="max-width: 850px">
      <div class="relative pt-[56.25%] border overflow-hidden rounded-2xl">
        <img class="w-full h-full absolute inset-0 object-cover" :src="img_background" alt="" />
      </div>
    </div>
    <article class="max-w-4xl px-6 mx-auto py-8">
      <div class="flex justify-between mt-9">
        <div v-if="pathRoute == 'event'" class="profile flex items-center">
          <div class="flex justify-center bg-white border rounded-full overflow-hidden">
            <img class="md:h-16 md:w-16 h-12 w-12" :src="detail.created_by?.profile
              ? image_url
              : 'https://iupac.org/wp-content/uploads/2018/05/default-avatar.png'
              " alt="" />
          </div>
          <div class="px-2 text-left">
            <h2 class="text-gray-800 my-0 text-xl font-bold">
              {{ detail.created_by?.full_name }}
            </h2>
            <p class="text-gray-400 my-0">
              @{{ detail.created_by?.full_name }}
            </p>
          </div>
        </div>
        <div v-if="pathRoute == 'event'" class="operation flex items-center justify-center align-middle">
          <a @click="registerEvent" v-if="!register" class="cursor-pointer
              mr-4
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
            ">
            Register
          </a>
          <button v-if="pathRoute == 'event'" @click="toggleInterested" class="
              text-center
              rounded-2xl
              w-10
              self-center
              h-8
              flex
              items-center
              justify-center
              bg-gray-100
            " :class="is_interested ? 'text-transparent' : ''">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 24 24" stroke="currentColor"
              :fill="is_interested ? '#B0005C' : 'none'">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
            </svg>
          </button>
        </div>
      </div>

      <hr v-if="pathRoute == 'event'" class="my-6" />
      <h1 class="text-xl text-left font-bold first-letter:text-4xl">
        {{ detail.title }}
      </h1>
      <div class="mt-6"></div>
      <h2 class="mt-2 text-sm text-gray-500">{{ detail.start_date_format }}</h2>

      <p v-if="!is_news" class="text-left my-9 px-2">
        <strong>Event Details: </strong>
      </p>

      <ul class="text-left text-gray px-2">
        <li v-if="detail?.mode" class="text-gray-600">
          Mode: <strong>{{ detail?.mode }}</strong>
        </li>
        <li v-if="detail?.start_date_format" class="text-gray-600">
          Start date: <strong> {{ detail?.start_date_format }}</strong>
        </li>
        <li v-if="detail?.end_date_format" class="text-gray-600">
          Start date: <strong> {{ detail?.end_date_format }}</strong>
        </li>
      </ul>

      <hr class="my-6" />
      <div v-if="pathRoute == 'news'">
        <p class="text-left text-gray-500 py-2">
          Upload at: {{ detail.created_at_format }}
        </p>
        <p class="text-left text-gray-500">
          Category:
          <span class="bg-gray-500 text-white rounded-md px-2 py-1" v-for="cat in detail.categories_props"
            v-bind:key="cat.id">{{ cat.name }}</span>
        </p>
      </div>

      <div class="mt-6 text-left min-h-screen" v-html="detail?.description"></div>
    </article>
  </main>
</template>


<script>
import { useStore } from "vuex";
import {
  DETAIL_PAGE_EVENT,
  DETAIL_PAGE_NEWS,
  LIKE_EVENT,
  REGISTER_EVENT,
} from "../store/type";
import route from "../router";
import { computed } from "vue";
import { notify } from "@kyvg/vue3-notification";

export default {
  data() {
    const store = useStore();
    return {
      route_id: "",
      news_detail: computed(() => store.state.news.detail),
      event_detail: computed(() => store.state.event.detail),
      is_loaded: computed(() => store.state.event.is_loaded),
      auth: computed(() => store.state.auth),
      getEventDetailPage(id) {
        store.dispatch({ type: DETAIL_PAGE_EVENT, id }).then(() => { });
      },
      getNewsDetailPage(id) {
        store.dispatch({ type: DETAIL_PAGE_NEWS, id });
      },
      is_auth: computed(() => store.state.auth.is_auth),
      profile: computed(() => store.state.auth.profile),
      token: computed(() => store.state.auth.token),
      is_interested: false,
      dispatchRegister(id) {
        store.dispatch({ type: REGISTER_EVENT, id });
      },
      register: true,
      toggleEventInterested(id) {
        let obj = {};
        if (this.is_auth) {
          obj = { id, is_interested: !this.is_interested, user: this.token };
          store.dispatch({
            type: LIKE_EVENT,
            payload: obj,
          });
          this.is_interested = !this.is_interested;
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
    detail: function () {
      if (this.route_id.path == "news") {
        return this.news_detail;
      } else if (this.route_id.path == "event") {
        return this.event_detail;
      }
      return {};
    },
    is_news: function () {
      return this.route_id.path == "news";
    },
    image_url: function () {
      return `${process.env.VUE_APP_STORAGE}${this.detail.created_by?.profile}`;
    },
    img_background: function () {
      return process.env.VUE_APP_STORAGE + this.detail.thumbnail;
    },
    pathRoute: function () {
      return this.route_id.path;
    },
  },
  watch: {
    profile: function (val) {
      this.profile = val;
      this.route_id = route.currentRoute.value.params;
      this.fetchCheckInStatus(this.route_id.id, val.id)
    },
    event_detail: async function (val) {
      var user = val.register_member.filter(
        (elem) => elem.id === this.profile?.id
      );
      if (!user && !user.check_in) {
        this.register = false;
      }
    },
  },
  created() {

  },
  async mounted() {
    this.$nextTick(async () => {
      if (route.currentRoute.value.params.props !== undefined) {
        this.is_interested = route.currentRoute.value.params.props == "true";
      }
      this.route_id = route.currentRoute.value.params;

      var path = this.route_id.path;
      var id = this.route_id.id;
      if (path == "news") {
        await this.getNewsDetailPage(id);
      } else if (path == "event") {
        await this.getEventDetailPage(id);
      }

      var user = this.event_detail?.register_member?.filter(
        (elem) => elem.id === this.profile?.id
      );
      if (!user && !user?.check_in) {
        this.register = false;
      }
    });
  },
  methods: {
    toggleInterested() {
      this.toggleEventInterested(this.detail.id);
    },
    fetchCheckInStatus(event_id, user_id) {
      fetch(`http://127.0.0.1:8000/registration/${event_id}/${user_id}`).then(res => res.json()).then(res => {
        this.register = res.check_in;
        console.log(res.check_in);
      })
    },
    registerEvent() {
      if (!this.is_auth) {
        route.push({ path: "/register" });
        return;
      }
      this.$swal
        .fire({
          title: "Are you sure to register this event?",
          showCancelButton: true,
          confirmButtonText: "Yes",
        })
        .then((result) => {
          /* Read more about isConfirmed, isDenied below */
          if (result.isConfirmed) {
            this.$swal.fire("Register has been send to owner!", "", "success");
            this.dispatchRegister(this.event_detail.id);
            this.register = true
          }
        });
    },
    fetchCheckInUser() {
      // var hasUserRegister = this.event_detail.register_member.filter((object) => object.id == this.profile.id)
      // if(hasUserRegister){
      //   return hasUserRegister.check_in;
      // }
      return false;
    },
  },
};
</script>
<style>
.pt-\[17\%\] {
  padding-top: 17%;
}

.mt-\[-10\%\] {
  margin-top: -10%;
}

.pt-\[56\.25\%\] {
  padding-top: 56.25%;
}
</style>