<template>
  <content-loader
    width="1920"
    height="1200"
    primaryColor="#f3f3f3"
    secondaryColor="#cccccc"
  >
 
      <rect x="0" y="8" rx="3" ry="10" width="320" height="350" />
      <rect x="332" y="8" rx="3" ry="10" width="320" height="350" />
      <rect x="664" y="8" rx="3" ry="10" width="320" height="350" />
      <rect x="996" y="8" rx="3" ry="10" width="320" height="350" />

      <rect x="0" y="380" rx="3" ry="10" width="320" height="350" />
      <rect x="332" y="380" rx="3" ry="10" width="320" height="350" />
      <rect x="664" y="380" rx="3" ry="10" width="320" height="350" />
      <rect x="996" y="380" rx="3" ry="10" width="320" height="350" />
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