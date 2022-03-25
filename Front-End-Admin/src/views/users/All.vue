<template>
  <div class="row">
    <div class="col-lg-12">
      <div class="card">
        <div class="card-header">
          <h5 class="card-title mb-0">{{ this.$route.name }}</h5>
        </div>
        <div class="card-body">
          <table class="table table-responsive-sm table-striped">
            <thead class="thead-light">
              <tr>
                <th>#</th>
                <th>Profile</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Phone</th>
                <th>Email</th>
                <th>Date of Birth</th>
                <th>Role</th>
                <!-- <th>Action</th> -->
              </tr>
            </thead>
            <tbody>
              <tr v-for="(list, index) in lists" :key="index">
                <td>{{ index + 1 }}</td>
                <td>
                  <img
                    class="rounded-circle"
                    width="40"
                    height="40"
                    style="object-fit: cover"
                    v-bind:src="
                      list.profile
                        ? 'http://127.0.0.1:8000/static/images/' + list.profile
                        : 'https://iupac.org/wp-content/uploads/2018/05/default-avatar.png'
                    "
                  />
                </td>
                <td>{{ list.first_name }}</td>
                <td>{{ list.last_name }}</td>
                <td>{{ list.phone_number }}</td>
                <td>{{ list.email }}</td>
                <td>{{ list.date_of_birth }}</td>
                <td>{{ list.role }}</td>
                <!-- <td>
                  <router-link
                    :to="{
                      name: 'Edit User',
                      params: { id: list.id },
                    }"
                    class="text-info mr-2"
                  >
                    <i class="fa fa-edit"></i>
                  </router-link>
                </td> -->
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapMutations } from "vuex";
import UserDataService from "@/services/UserDataService";
import { BREADCRUMB, LOADING_SPINNER_MUTATION } from "@/store/storeconstants";

export default {
  created() {
    document.title = "User All";
    this.breadcrumb("User");
  },
  data() {
    return {
      lists: [],
    };
  },
  methods: {
    ...mapMutations({
      isLoading: LOADING_SPINNER_MUTATION,
      breadcrumb: BREADCRUMB,
    }),
    retrieveLists() {
      let vm = this;
      this.isLoading(true);
      UserDataService.getAll()
        .then((response) => {
          setTimeout(function () {
            vm.isLoading(false);
          }, 500);
          this.lists = response.data;
          console.log(response.data);
        })
        .catch((e) => {
          this.isLoading(false);
          console.log(e);
        });
    },
    deleteList(id) {
      if (confirm("Are you sure to delete the record?"))
        UserDataService.delete(id)
          .then((response) => {
            console.log(response);
            this.retrieveLists();
          })
          .catch((e) => {
            console.log(e);
          });
    },
  },
  mounted() {
    this.retrieveLists();
  },
};
</script>

<style>
</style>