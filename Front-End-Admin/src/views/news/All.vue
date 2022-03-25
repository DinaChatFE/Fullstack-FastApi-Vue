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
                <th>Thumbnail</th>
                <th>Title</th>
                <th>Category</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(list, index) in lists" :key="index">
                <td>{{ index + 1 }}</td>
                <td>
                  <img
                    width="80"
                    v-bind:src="
                      'http://127.0.0.1:8000/static/images/' + list.thumbnail
                    "
                    @error="imageUrlAlt"
                  />
                </td>
                <td>{{ list.title }}</td>
                <td>{{ this.category(list.categories_props) }}</td>
                <td style="min-width: 80px">
                  <router-link
                    :to="{
                      name: 'News Show',
                      params: { id: list.id },
                    }"
                    class="text-info mr-2"
                  >
                    <i class="fa fa-eye"></i>
                  </router-link>
                  <router-link
                   v-if="profile.id == list.created_by?.id"
                    :to="{
                      name: 'News Edit',
                      params: { id: list.id },
                      query: {
                        cate_id: this.category(list.categories_props, 'id'),
                      },
                    }"
                    class="text-info mr-2"
                  >
                    <i class="fa fa-edit"></i>
                  </router-link
                  >
                  <a
                    v-if="profile.id == list.created_by?.id"
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
import NewsDataService from "@/services/NewsDataService";
import { BREADCRUMB, LOADING_SPINNER_MUTATION } from "@/store/storeconstants";
import UserDataService from "../../services/UserDataService";

export default {
  created() {
    document.title = "News All";
    this.breadcrumb("News");
  },
  data() {
    return {
      lists: [],
      profile: {},
    };
  },

  methods: {
    ...mapMutations({
      isLoading: LOADING_SPINNER_MUTATION,
      breadcrumb: BREADCRUMB,
    }),
    category(data, column = "name") {
      var categ = "";
      data.forEach((value, index) => {
        categ = column == "name" ? value.name : value.id;
      });
      return categ;
    },
    imageUrlAlt(event) {
      event.target.src = "";
    },
    retrieveLists() {
      let vm = this;
      this.isLoading(true);
      NewsDataService.getAll()
        .then((response) => {
          setTimeout(function () {
            vm.isLoading(false);
          }, 500);
          this.lists = response.data.data;
        })
        .catch((e) => {
          this.isLoading(false);
          console.log(e);
        });
    },
    deleteList(id) {
      if (confirm("Are you sure to delete the record?"))
        NewsDataService.delete(id)
          .then((response) => {
            this.retrieveLists();
            createToast("record deleted successfully.", {
              position: "top-right",
              type: "success",
              showIcon: "true",
              transition: "slide",
            });
          })
          .catch((e) => {
            this.retrieveLists();
          });
    },
  },
  mounted() {
    this.retrieveLists();
    UserDataService.profile().then((res) => {
      this.profile = res.data.data;
    });
  },
};
</script>

<style>
</style>