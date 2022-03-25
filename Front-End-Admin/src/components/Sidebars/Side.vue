<template>
  <div class="sidebar">
    <nav class="sidebar-nav">
      <ul class="nav">
        <li class="nav-item">
          <router-link :to="'/'" class="nav-link"
            ><i class="icon-speedometer text-info"></i> Dashboard</router-link
          >
        </li>
        <li
          class="nav-item nav-dropdown"
          @click="navDropdownClick(2)"
          :class="{ open: navDropdownOpen == 2 }"
        >
          <a class="nav-link nav-dropdown-toggle" href="#"
            ><i class="icon-calendar text-info"></i> Event</a
          >
          <ul class="nav-dropdown-items">
            <li class="nav-item">
              <router-link :to="'/create-event'" class="nav-link"
                ><i class="fa fa-circle text-info"></i> Add New</router-link
              >
            </li>
            <li class="nav-item">
              <router-link :to="'/event'" class="nav-link"
                ><i class="fa fa-circle text-info"></i> All</router-link
              >
            </li>
          </ul>
        </li>
        <li
          class="nav-item nav-dropdown"
          @click="navDropdownClick(4)"
          :class="{ open: navDropdownOpen == 4 }"
        >
          <a class="nav-link nav-dropdown-toggle" href="#"
            ><i class="icon-notebook text-info"></i> News</a
          >
          <ul class="nav-dropdown-items">
            <li class="nav-item">
              <router-link :to="'/create-news'" class="nav-link"
                ><i class="fa fa-circle text-info"></i> Add New</router-link
              >
            </li>
            <li class="nav-item">
              <router-link :to="'/news'" class="nav-link"
                ><i class="fa fa-circle text-info"></i> All</router-link
              >
            </li>
          </ul>
        </li>
        <li
          class="nav-item nav-dropdown"
          @click="navDropdownClick(3)"
          :class="{ open: navDropdownOpen == 3 }"
        >
          <a class="nav-link nav-dropdown-toggle" href="#"
            ><i class="icon-layers text-info"></i> Category</a
          >
          <ul class="nav-dropdown-items">
            <li class="nav-item">
              <router-link :to="'/create-category'" class="nav-link"
                ><i class="fa fa-circle text-info"></i> Add New</router-link
              >
            </li>
            <li class="nav-item">
              <router-link :to="'/category'" class="nav-link"
                ><i class="fa fa-circle text-info"></i> All</router-link
              >
            </li>
          </ul>
        </li>

        <li
          class="nav-item nav-dropdown"
          @click="navDropdownClick(5)"
          :class="{ open: navDropdownOpen == 5 }"
        >
          <a class="nav-link nav-dropdown-toggle" href="#"
            ><i class="icon-people text-info"></i> User</a
          >
          <ul class="nav-dropdown-items">
            <li class="nav-item">
              <router-link :to="'/create-user'" class="nav-link"
                ><i class="fa fa-circle text-info"></i> Add New</router-link
              >
            </li>
            <li class="nav-item">
              <router-link :to="'/user'" class="nav-link"
                ><i class="fa fa-circle text-info"></i> All</router-link
              >
            </li>
          </ul>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
import route from '../../router'
import serviceUser from '../../services/UserDataService'
export default {
  data() {
    return {
      navDropdownOpen: null,
      route_change: ""
    };
  },
  computed: {
    url_path: function(){
      console.log(route.currentRoute.value.name);
       return  route.currentRoute.value.name
    }
  },
  methods: {
    navDropdownClick(index) {
      if (this.navDropdownOpen == index) {
        this.navDropdownOpen = null;
      } else {
        this.navDropdownOpen = index;
      }
    },
  },
  created() {
      serviceUser.profile().then(res => {
        console.log(res.data);
      })
  }
};
</script>

<style>
.sidebar-dark-primary .nav-sidebar > .nav-item > .nav-link.active,
.sidebar-light-primary .nav-sidebar > .nav-item > .nav-link.active {
  background-color: #4d5359;
}
[class*="sidebar-dark-"] .nav-treeview > .nav-item > .nav-link.active,
[class*="sidebar-dark-"] .nav-treeview > .nav-item > .nav-link.active:focus,
[class*="sidebar-dark-"] .nav-treeview > .nav-item > .nav-link.active:hover {
  background-color: #4d5359;
  color: #ffffff;
  box-shadow: 0 1px 3px rgb(0 0 0 / 12%), 0 1px 2px rgb(0 0 0 / 24%);
}
[class*="sidebar-dark-"] .nav-sidebar > .nav-item.menu-open > .nav-link,
[class*="sidebar-dark-"] .nav-sidebar > .nav-item:hover > .nav-link,
[class*="sidebar-dark-"] .nav-sidebar > .nav-item > .nav-link:focus {
  background-color: rgb(52 58 64);
  color: #fff;
}
.brand-link {
  background: dimgray;
  border-bottom: 0;
}
</style>