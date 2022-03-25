<template>
  <content-loader
    class="pt-4 pl-2"
    viewBox="0 0 476 124"
    primaryColor="#f3f3f3"
    speed=1
    secondaryColor="#cccccc"
  >
    <rect x="48" y="8" rx="3" ry="3" width="88" height="6" />
    <rect x="48" y="26" rx="3" ry="3" width="52" height="6" />
    <rect x="0" y="56" rx="3" ry="3" width="420" height="6" />
    <rect x="0" y="72" rx="3" ry="3" width="380" height="6" />
    <rect x="0" y="88" rx="3" ry="3" width="178" height="6" />
    <circle cx="20" cy="20" r="20" />
  </content-loader>
</template>

<script>
import { ContentLoader } from "vue-content-loader";

export default {
  components: { ContentLoader },
};
</script>

<style>
</style>