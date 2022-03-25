<template>
  <Loader v-if="isLoading" />
  <body
    class="app header-fixed sidebar-fixed aside-menu-fixed aside-menu-hidden"
    :class="{ 'sidebar-hidden': sidebarHidden }"
  >
    <Navbar></Navbar>
    <div class="app-body">
      <Sidebar></Sidebar>
      <!-- Main content -->
      <main class="main">
        <ContentHeader></ContentHeader>
        <div class="container-fluid">
          <router-view />
          <div class="animated fadeIn"></div>
        </div>
      </main>
    </div>
  </body>
</template>

<script>
import { mapState } from "vuex";
import ContentHeader from "../components/Headers/ContentHeader.vue";
import Sidebar from "../components/Sidebars/Side.vue";
import Navbar from "../components/Navbars/Navbar.vue";
import Footer from "../components/Footers/Footer.vue";
import Loader from "@/components/Loader";

export default {
  name: "layout-admin",
  data() {
    return {};
  },
  components: {
    ContentHeader,
    Navbar,
    Sidebar,
    Footer,
    Loader,
  },
  computed: {
    ...mapState({
      isLoading: (state) => state.isLoading,
      sidebarHidden: (state) => state.sidebarHidden,
    }),
  },
};
</script>