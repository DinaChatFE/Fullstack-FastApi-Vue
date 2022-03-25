<template>
  <navbar />
  <detail />
  <footer-nav />
</template>

<script>
import Navbar from "../components/Navbar";
import FooterNav from "../components/Footer";
import Detail from "../Layout/Details";


export default {
  name: "DetailsPage",
  components: { Navbar, FooterNav, Detail },
  created(){
    document.title = "Detail"
  }
};
</script>

<style>
</style>