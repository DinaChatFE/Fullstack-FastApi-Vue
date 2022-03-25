<template>
  <!-- eslint-disable-next-line vue/max-attributes-per-line -->
  <div class="antialiased bg-gray-100 dark-mode:bg-gray-900 shadow-sm z-10">
    <div
      class="
        w-full
        text-gray-700
        bg-white
        dark-mode:text-gray-200 dark-mode:bg-gray-800
      "
    >
      <div
        x-data="{ open: true }"
        class="
          flex flex-col
          max-w-screen-xl
          px-4
          mx-auto
          md:items-center md:justify-between md:flex-row md:px-6
          lg:px-8
        "
      >
        <div class="flex flex-row items-center justify-between py-4">
          <router-link to="/">
            <a
              href="#"
              class="
                text-xl
                font-semibold
                tracking-widest
                text-gray-900
                uppercase
                rounded-lg
                text-sm
                dark-mode:text-white
                focus:outline-none focus:shadow-outline
              "
              >Event News
            </a>
          </router-link>
          <button
            class="rounded-lg md:hidden focus:outline-none focus:shadow-outline"
            @click="openNav"
          >
            <svg fill="currentColor" viewBox="0 0 20 20" class="w-6 h-6">
              <path
                x-show="!open"
                fill-rule="evenodd"
                d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM9 15a1 1 0 011-1h6a1 1 0 110 2h-6a1 1 0 01-1-1z"
                clip-rule="evenodd"
              ></path>
              <path
                x-show="open"
                fill-rule="evenodd"
                d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                clip-rule="evenodd"
              ></path>
            </svg>
          </button>
        </div>
        <nav
          :class="{ flex: open, hidden: !open }"
          class="
            flex-col flex-grow
            hidden
            pb-4
            md:pb-0 md:flex md:justify-end md:flex-row
          "
        >
          <router-link
            to="/"
            class="
              px-4
              py-2
              font-semibold
              text-sm
              bg-transparent
              rounded-lg
              dark-mode:bg-transparent
              dark-mode:hover:bg-gray-600
              dark-mode:focus:bg-gray-600
              dark-mode:focus:text-white
              dark-mode:hover:text-white
              dark-mode:text-gray-200
              md:mt-1 md:ml-4
              hover:text-gray-900
              focus:text-gray-900
              hover:bg-gray-200
              focus:bg-gray-200 focus:outline-none focus:shadow-outline
            "
            :class="current_route == 'Home' ? 'bg-gray-200' : ''"
            href="#"
            >Home</router-link
          >
          <router-link
            to="/news"
            class="
              px-4
              py-2
              mt-2
              text-sm
              font-semibold
              bg-transparent
              rounded-lg
              dark-mode:bg-transparent
              dark-mode:hover:bg-gray-600
              dark-mode:focus:bg-gray-600
              dark-mode:focus:text-white
              dark-mode:hover:text-white
              dark-mode:text-gray-200
              md:mt-1 md:ml-4
              hover:text-gray-900
              focus:text-gray-900
              hover:bg-gray-200
              focus:bg-gray-200 focus:outline-none focus:shadow-outline
            "
            :class="current_route == 'News' ? 'bg-gray-200' : ''"
            href="#"
            >News</router-link
          >
          <a
            class="
              px-4
              py-2
              mt-2
              font-semibold
              bg-transparent
              rounded-lg
              text-sm
              dark-mode:bg-transparent
              dark-mode:hover:bg-gray-600
              dark-mode:focus:bg-gray-600
              dark-mode:focus:text-white
              dark-mode:hover:text-white
              dark-mode:text-gray-200
              md:mt-1 md:ml-4
              hover:text-gray-900
              focus:text-gray-900
              hover:bg-gray-200
              focus:bg-gray-200 focus:outline-none focus:shadow-outline
            "
            href="#"
            >About</a
          >
          <router-link
            to="/profile"
            v-if="auth.is_auth"
            class="
              px-12
              font-semibold
              bg-transparent
              rounded-lg
              flex
              justify-center
              align-middle
            "
            href="#"
          >
            <img
              alt=""
              :src="imageUrl"
              class="
                shadow-2xl
                rounded-full
                align-middle
                w-10
                h-10
                object-cover
                border-none
                absolute
              "
            />
          </router-link>
          <router-link to="/register" v-else>
            <button
              class="
                ml-4
                px-4
                mt-1
                py-2
                rounded-full
                font-normal
                tracking-wide
                bg-gradient-to-b
                from-blue-600
                to-blue-700
                text-white
                outline-none
                focus:outline-none
                hover:shadow-lg hover:from-blue-700
                transition
                duration-200
                text-sm
                ease-in-out
              "
            >
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

export default {
  name: "NavBar",
  data() {
    const store = useStore();
    return {
      current_route: "",
      auth: computed(() => store.state.auth),
      getProfile() {
        store.dispatch(PROFILE);
      },
    };
  },
  computed: {
    imageUrl: function(){
      if(this.auth.profile.profile){
        return process.env.VUE_APP_STORAGE + this.auth.profile.profile
      }
      return 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png'
    }
  },
  created() {
    this.getProfile();
    this.current_route = this.$route.name;
  },
};
</script>

<style>
</style>