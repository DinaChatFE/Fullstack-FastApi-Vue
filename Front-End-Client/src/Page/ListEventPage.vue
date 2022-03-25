<template>
  <div class="row">
    <navbar />
    <list-event/>
    <footer-nav />
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue'
import FooterNav from '../components/Footer.vue'
import ListEvent from '../Layout/ListEvent.vue'
export default {
  components: { Navbar, FooterNav, ListEvent },
}
</script>

<style>

</style>