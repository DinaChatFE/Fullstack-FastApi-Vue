<template>
  <div class="row">
    <div class="col-lg-12">
      <div class="card">
        <div class="card-header">
          {{ this.$route.name }}
        </div>
        <div class="card-body">
          <table class="table table-responsive-sm table-striped">
            <thead class="thead-light">
              <tr>
                <th>#</th>
                <th>Name</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(list, index) in lists" :key="index">
                <td>{{ list.id }}</td>
                <td>{{ list.name }}</td>
                <td>
                  <router-link
                    :to="{ name: 'Edit Category', params: { id: list.id } }"
                    class="text-info mr-2"
                  >
                    <i class="fa fa-edit"></i>
                  </router-link>
                  <a
                    class="text-danger"
                    v-on:click="deleteList(list.id)"
                    style="cursor: pointer"
                  >
                    <i class="fa fa-trash-o"></i>
                  </a>
                </td>
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
import CaregoryDataService from "@/services/CaregoryDataService";
import { BREADCRUMB, LOADING_SPINNER_MUTATION } from "@/store/storeconstants";
import { createToast } from 'mosha-vue-toastify';
import "mosha-vue-toastify/dist/style.css";

export default {
  created() {
    document.title = "Category All";
    this.breadcrumb("Category");
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
      CaregoryDataService.getAll()
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
        CaregoryDataService.delete(id)
          .then((response) => {
            console.log(response);
            setTimeout(() => {
              this.retrieveLists();
              createToast("record deleted successfully.", {
                position: "top-right",
                type: "success",
                showIcon: "true",
                transition: "slide",
              });
              
            }, 1000);

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