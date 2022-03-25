<template>
  <Loader v-if="isLoading" />
  <body class="hold-transition sidebar-mini layout-fixed">
    <router-view />
  </body>
</template>

<script>
import { mapState } from "vuex";
import Loader from "@/components/Loader";
export default {
  name: "layout-default",
  components: {
    Loader,
  },
  computed: {
    // this is root state we can create multi state and call by there name
    // ...mapState("auth", {
    //   isLoading: (state) => state.isLoading,
    // }),
    ...mapState({
      isLoading: (state) => state.isLoading,
      // autoLogout: (state) => state.auth.autoLogout,
    }),
  },
};
</script>