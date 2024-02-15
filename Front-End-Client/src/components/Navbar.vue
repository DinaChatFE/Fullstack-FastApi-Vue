<template>
  <!-- eslint-disable-next-line vue/max-attributes-per-line -->
  <div class="antialiased bg-gray-100 dark-mode:bg-gray-900 shadow-sm z-10">
    <div class="
        w-full
        text-gray-700
        bg-white
        dark-mode:text-gray-200 dark-mode:bg-gray-800
      ">
      <div x-data="{ open: true }" class="
          flex flex-col
          max-w-screen-xl
          px-4
          mx-auto
          md:items-center md:justify-between md:flex-row md:px-6
          lg:px-8
        ">
        <div class="flex flex-row items-center justify-between py-4">
          <div class="flex">
            <button class="md:hidden rounded-lg focus:outline-none focus:shadow-outline" @click="openNav">
              <img src="@/assets/burger.svg" class="w-6 h-6" alt="burger icon"/>
            </button>
            <router-link to="/" class="px-2">
              <a href="#" class="text-xl font-semibold tracking-widest text-gray-900 uppercase rounded-lg dark-mode:text-white focus:outline-none focus:shadow-outline
                ">Event News
              </a>
            </router-link>
          </div>
          <div class="nav-responsive md:hidden">
            <profile-icon-header :auth="auth" v-if="auth.is_auth" />
          </div>

        </div>
        <nav class="hidden flex-col flex-grow pb-4 md:pb-0 md:flex md:justify-end md:flex-row
          ">
          <router-link to="/" class=" px-4 py-2 font-semibold text-sm bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 md:mt-1 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline
            " :class="current_route == 'Home' ? 'bg-gray-200' : ''" href="#">Home</router-link>
          <router-link to="/news" class=" px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 md:mt-1 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline
            " :class="current_route == 'News' ? 'bg-gray-200' : ''" href="#">News</router-link>
          <a class="px-4 py-2 mt-2 font-semibold bg-transparent rounded-lg text-sm dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 md:mt-1 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline
            " href="#">About</a>
          <profile-icon-header :auth="auth" v-if="auth.is_auth" />
          <router-link to="/register" v-else>
            <button class="ml-4 px-4 mt-1 py-2 rounded-full font-normal tracking-wide bg-gradient-to-b from-blue-600 to-blue-700 text-white outline-none focus:outline-none hover:shadow-lg hover:from-blue-700 transition duration-200 text-sm ease-in-out
              ">
              Register
            </button>
          </router-link>
        </nav>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from "vue";
import { useStore } from "vuex";
import { PROFILE } from "../store/type";
import ProfileIconHeader from "./common/ProfileIconHeader.vue";

export default {
  name: "NavBar",
  data() {
    const store = useStore();
    return {
      open: false,
      current_route: "",
      auth: computed(() => store.state.auth),
      getProfile() {
        store.dispatch(PROFILE);
      },
    };
  },
  methods: {
    openNav: function () {
      this.open = !this.open;
    }
  },
  created() {
    this.getProfile();
    this.current_route = this.$route.name;
  },
  components: { ProfileIconHeader }
};
</script>

<style></style>