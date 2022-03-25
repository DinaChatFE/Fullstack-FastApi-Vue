<template>
  <div class="px-8 text-left">
    <h1 class="mb-4 text-lg font-bold text-gray-700">Poster</h1>
    <div
      class="
        flex flex-col
        max-w-sm
        px-6
        py-4
        mx-auto
        bg-white
        rounded-lg
        shadow-md
      "
    >
      <ul class="-mx-4">
        <a
          v-for="user in data"
          v-bind:key="user.id"
          @click="appendLink(user.id)"
        >
          <li class="flex items-center">
            <img
              :src="
                user.profile
                  ? `${storage_url}${user.profile}`
                  : 'https://iupac.org/wp-content/uploads/2018/05/default-avatar.png'
              "
              alt="avatar"
              class="object-cover w-10 h-10 mx-4 rounded-full"
            />
            <p class="line-clamp-1 my-3">
              <a
                href="#"
                class="mx-1 font-bold text-gray-700 hover:underline"
                >{{ user.full_name }}</a
              >
            </p>
          </li>
        </a>
      </ul>
    </div>
  </div>
</template>

<script>
import { computed } from "vue-demi";
import { useStore } from "vuex";
import { ALL_USER, FILTER_NEWS_WITH_PAGE } from "../../store/type";
import router from "../../router";
export default {
  data() {
    const store = useStore();
    return {
      data: computed(() => store.state.auth.user),
      getData() {
        store.dispatch(ALL_USER);
      },
      dispatchFetch(page) {
        store.dispatch({ type: FILTER_NEWS_WITH_PAGE, page });
      },
    };
  },
  computed: {
    storage_url: function () {
      return process.env.VUE_APP_STORAGE;
    },
  },
  methods: {
    appendLink(push) {
      router.push({ query: { admin: push } });
      this.dispatchFetch(1);
    },
  },
  created() {
    this.getData();
  },
};
</script>

<style>
</style>