<template>
  <div class="row">
    <navbar />
    <post />
    <footer-nav />
  </div>
</template>

<script>
import FooterNav from "../components/Footer";
import Navbar from "../components/Navbar";
import Post from "../Layout/ListPost.vue";

export default {
  name: "ListPost",
  components: { Post, FooterNav, Navbar },
  created() {
    document.title = "News";
  },
};
</script>

<style>
</style>