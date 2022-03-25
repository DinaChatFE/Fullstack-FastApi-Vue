<template>
  <component :is="layout" />
</template>

<script>
import LayoutDefault from "@/layouts/LayoutDefault";
import LayoutAdmin from "@/layouts/LayoutAdmin";
import { AUTO_LOGIN_ACTION } from "@/store/storeconstants";

export default {
  components: {
    LayoutAdmin,
    LayoutDefault,
  },
  data() {
    return {
      layout: null,
    };
  },
  watch: {
    $route(to) {
      // set layout by route meta
      if (to.meta.layout !== undefined) {
        this.layout = to.meta.layout;
      } else {
        this.layout = "LayoutDefault"; // this is default layout if route meta is not set
      }
    },
  },
  created() {
    this.$store.dispatch(`auth/${AUTO_LOGIN_ACTION}`);
  },
};
</script>
