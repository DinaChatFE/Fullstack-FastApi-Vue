<template>
  <div class="row">
    <navbar />
    <hero-section />
    <card-items v-if="event" :event_items="event" />
    <footer-nav />
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
import HeroSection from "../components/HeroSection";
import FooterNav from "../components/Footer.vue";
import CardItems from "../components/CardItems.vue";
import { useStore } from "vuex";
import { compile, computed } from "vue";
import { PROFILE, GET_ALL_EVENT, } from "../store/type";

export default {
  name: "App",
  components: { Navbar, FooterNav, HeroSection, CardItems },
  data() {
    const store = useStore();
    return {
      profile: computed(() => store.state.auth.profile),
      is_auth: computed(() => store.state.auth.is_auth),
      token: computed(()=> store.state.auth.token),
      event: computed(() => store.state.event.event),
      query: compile(() => store.state.event.event),
    };
  },
  async created() {
    document.title = "Home"
    const store = useStore();
    this.$nextTick(() => {
      store.dispatch(PROFILE); 
      store.dispatch({type: GET_ALL_EVENT, payload: this.token})
    })
  },
  async mounted(){
    const store = useStore();
    store.dispatch({type: GET_ALL_EVENT, payload: this.token})
    // store.dispatch(PROFILE)
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #f5f6f7;
}
</style>