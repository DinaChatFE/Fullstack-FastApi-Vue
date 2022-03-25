<template>
  <header class="app-header navbar">
    <button
      class="navbar-toggler mobile-sidebar-toggler d-lg-none"
      type="button"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <a class="navbar-brand" href="#"> Event News </a>
    <button
      class="navbar-toggler sidebar-toggler d-md-down-none"
      type="button"
      @click="sidebarToggler"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <!-- <ul class="nav navbar-nav d-md-down-none mr-auto">
      <li class="nav-item px-3">
        <a class="nav-link" href="#">Dashboard</a>
      </li>
      <li class="nav-item px-3">
        <a class="nav-link" href="#">Users</a>
      </li>
      <li class="nav-item px-3">
        <a class="nav-link" href="#">Settings</a>
      </li>
    </ul> -->
    <ul class="nav navbar-nav ml-auto">
      <li class="nav-item dropdown">
        <a
          class="nav-link nav-link"
          data-toggle="dropdown"
          href="#"
          role="button"
          aria-haspopup="true"
          aria-expanded="false"
        >
          <img
            v-bind:src="
              profile
                ? 'http://127.0.0.1:8000/static/images/' + profile
                : 'https://iupac.org/wp-content/uploads/2018/05/default-avatar.png'
            "
            class="img-avatar"
            alt=""
          />
        </a>
        <div class="dropdown-menu dropdown-menu-right">
          <div class="dropdown-header text-center">
            <strong>Account</strong>
          </div>
          <router-link :to="'/profile'" class="dropdown-item"
            ><i class="fa fa-user"></i> Profile</router-link
          >
          <a class="dropdown-item" href="#" @click="onLogout()"
            ><i class="fa fa-lock"></i> Logout</a
          >
        </div>
      </li>
      <button class="navbar-toggler aside-menu-toggler" type="button">
        <!-- <span class="navbar-toggler-icon"></span> -->
      </button>
    </ul>
  </header>
</template>

<script>
import { mapActions, mapGetters, mapMutations, mapState } from "vuex";
import {
  IS_USER_AUTHENTICATED_GETTER,
  LOGOUT_ACTION,
  SIDEBAR_HIDDEN_MUTATION,
  AUTHPROFILE,
} from "@/store/storeconstants";
export default {
  name: "SideBar",
  data() {
    return {
      sidebarHidden: false,
    };
  },
  created() {
    let authData = localStorage.getItem("authData");
    if (authData) {
      this.authProfile(JSON.parse(authData).profile);
    }
  },
  computed: {
    ...mapState({
      profile: (state) => state.authProfile,
    }),
    ...mapGetters("auth", {
      isAuthenticated: IS_USER_AUTHENTICATED_GETTER,
    }),
  },
  methods: {
    ...mapActions("auth", {
      logout: LOGOUT_ACTION,
    }),
    ...mapMutations({
      sidebarHiddenMutation: SIDEBAR_HIDDEN_MUTATION,
      authProfile: AUTHPROFILE,
    }),
    sidebarToggler() {
      this.sidebarHidden = !this.sidebarHidden;
      this.sidebarHiddenMutation(this.sidebarHidden);
    },
    onLogout() {
      this.logout();
      this.$router.replace({ path: "/sign-in" });
    },
  },
};
</script>

<style>
</style>