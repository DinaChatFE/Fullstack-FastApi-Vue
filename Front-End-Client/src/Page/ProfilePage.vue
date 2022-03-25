<template>
  <navbar/>
  <profile/>
  <footer-nav/>
</template>

<script>
import FooterNav from '../components/Footer'
import Navbar from '../components/Navbar'
import Profile from '../Layout/Profile.vue'

export default {
  components: { Navbar, FooterNav, Profile },
  created(){
    document.title = "Profile"
  }
}
</script>

<style>

</style>