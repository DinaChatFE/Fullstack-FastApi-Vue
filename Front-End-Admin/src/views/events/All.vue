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
                <th>Stat Date</th>
                <th>End Date</th>
                <th>Location</th>
                <th>Mode</th>
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
                <td>{{ list.start_date_format }}</td>
                <td>{{ list.end_date_format }}</td>
                <td>{{ list.location }}</td>
                <td>{{ list.mode }}</td>
                <td style="min-width: 80px">
                  <router-link
                    :to="{
                      name: 'Event Show',
                      params: { id: list.id },
                    }"
                    class="text-info mr-2"
                  >
                    <i class="fa fa-eye"></i>
                  </router-link>
                  <router-link
                    v-if="profile.id == list.created_by?.id"
                    :to="{
                      name: 'Edit Event',
                      params: { event_id: list.id },
                      query: {
                        mode: list.mode,
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
import EventDataService from "@/services/EventDataService";
import { LOADING_SPINNER_MUTATION, BREADCRUMB } from "@/store/storeconstants";
import { createToast } from "mosha-vue-toastify";
import "mosha-vue-toastify/dist/style.css";
import UserDataService from '../../services/UserDataService';

export default {
  created() {
    document.title = "Event All";
    this.breadcrumb("Event");
  },
  data() {
    return {
      lists: [],
      profile: {}
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
      EventDataService.getAll()
        .then((response) => {
          setTimeout(function () {
            vm.isLoading(false);
          }, 1000);
          this.lists = response.data.data;
        })
        .catch((e) => {
          this.isLoading(false);
          console.log(e);
        });
    },
    imageUrlAlt(event) {
      event.target.src = "";
    },
    deleteList(id) {
      if (confirm("Are you sure to delete the record?"))
        EventDataService.delete(id)
          .then((response) => {
            this.retrieveLists();
            setTimeout(() => {
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
    UserDataService.profile().then((res) => {
      this.profile = res.data.data;
    });
  },
};
</script>

<style>
</style>