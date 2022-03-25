<template>
  <div class="card card-default">
    <div class="card-header">News</div>
    <div class="card-body">
      <table class="container-fluid">
        <tbody>
          <tr class="my-2">
            <td scope="row" class="border-0 font-weight-bold">Title</td>
            <td class="border-0">:</td>
            <td class="border-0">{{ data?.title }}</td>
            <td scope="row" class="border-0 font-weight-bold">Location</td>
            <td class="border-0">:</td>
            <td class="border-0">{{ data?.location }}</td>
          </tr>

          <tr class="my-2">
            <td scope="row" class="border-0 font-weight-bold">Mode</td>
            <td class="border-0">:</td>
            <td class="border-0">{{ data?.mode }}</td>
            <td scope="row" class="border-0 font-weight-bold">Create by</td>
            <td class="border-0">:</td>
            <td class="border-0">
              <router-link to="/user">{{ data?.created_by?.full_name }}</router-link> 
            </td>
          </tr>
          <tr class="my-2">
            <td scope="row" class="border-0 font-weight-bold">Start date</td>
            <td class="border-0">:</td>
            <td class="border-0">
              {{ data.start_date_format }}
            </td>
            <td scope="row" class="border-0 font-weight-bold">End date</td>

            <td class="border-0">:</td>
            <td class="border-0">
              {{ data.end_date_format }}
            </td>
          </tr>
          <tr class="my-2">
            <td scope="row" class="border-0 font-weight-bold">Status</td>
            <td class="border-0">:</td>
            <td class="border-0">{{ data?.status }}</td>
          </tr>
          <tr class="my-2">
            <td scope="row" class="border-0 font-weight-bold">Description</td>
            <td class="border-0">:</td>
            <td
              class="border-0"
              style="width: 600px"
              v-html="data?.description"
            ></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="card-footer">
      <a href="#"> Back</a>
    </div>
  </div>
  <div class="card card-default my-4">
    <div class="card-header">Register List</div>
    <div class="card-body">
      <table class="table">
        <thead class="thead-light">
          <tr>
            <th scope="col">#</th>
            <th scope="col">First name</th>
            <th scope="col">Last name</th>
            <th scope="col">Date of birth</th>
            <th scope="col">Email</th>
            <th scope="col">Address</th>
            <th scope="col">Phone number</th>
            <th scope="col">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="member in data.register_member" v-bind:key="member.id">
            <th scope="row">1</th>
            <td>{{ member.first_name }}</td>
            <td>{{ member.last_name }}</td>
            <td>{{ member.date_of_birth }}</td>
            <td>{{ member.email }}</td>
            <td>{{ member.address }}</td>
            <td>{{ member.phone_number }}</td>
            <td>
              <a
                class="btn btn-light"
                :class="member.check_in ? 'disabled' : ''"
                @click="checkInMember(data.id, member.id)"
                >{{ member.check_in ? "Checked" : "Check" }}</a
              >
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="card-footer">
      <a href="#"> Back</a>
    </div>
  </div>
</template>

<script>
import EventDataService from "@/services/EventDataService";
import { createToast } from "mosha-vue-toastify";

export default {
  data() {
    return {
      data: {},
    };
  },
  created() {
    this.getList(this.$route.params.id);
  },
  methods: {
    checkInMember(event_id, user_id) {
      this.$swal
        .fire({
          title: "Are you sure to check in this member?",
          showCancelButton: true,
          confirmButtonText: "Yes",
        })
        .then((result) => {
          /* Read more about isConfirmed, isDenied below */
          if (result.isConfirmed) {
            EventDataService.checkIn(event_id, user_id)
              .then((response) => {
                this.getList(this.$route.params.id);
                setTimeout(() => {
                  this.$swal.fire("Check in success", "", "success");
                }, 400);
              })
              .catch((error) => {
                if (error.response.status == 403) {
                  createToast("You cannot check in while event not event started yet", {
                    position: "top-right",
                    type: "danger",
                    showIcon: "true",
                    transition: "slide",
                  });
                }
              });
          }
        });
    },
    getList(id) {
      let vm = this;
      EventDataService.getEventForAdmin(id)
        .then((response) => {
          this.data = response.data;
          vm.form.title = response.data.title;
          vm.form.content = response.data.content;
          vm.form.description = response.data.description;
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>

<style>
</style>