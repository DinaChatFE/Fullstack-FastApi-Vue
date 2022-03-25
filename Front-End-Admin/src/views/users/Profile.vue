<template>
  <div class="container">
    <div class="row gutters">
      <div class="col-xl-3 col-lg-3 col-md-12 col-sm-12 col-12">
        <div class="card h-100">
          <div class="card-body">
            <div class="account-settings">
              <div class="user-profile">
                <div class="user-avatar">
                  <img
                    v-bind:src="
                      profile && profile.profile
                        ? 'http://127.0.0.1:8000/static/images/' +
                          profile.profile
                        : 'https://iupac.org/wp-content/uploads/2018/05/default-avatar.png'
                    "
                    alt=""
                  />
                </div>
                <h5 class="user-name" v-if="profile">
                  {{ this.capitalizeFirstLetter(profile.first_name) }}
                  {{ this.capitalizeFirstLetter(profile.last_name) }}
                </h5>
                <h6 class="user-email" v-if="profile">{{ profile.email }}</h6>
              </div>
              <!-- <div class="about">
                <h5>About</h5>
                <p>
                  I'm Yuki. Full Stack Designer I enjoy creating user-centric,
                  delightful and human experiences.
                </p>
              </div> -->
            </div>
          </div>
        </div>
      </div>
      <div class="col-xl-9 col-lg-9 col-md-12 col-sm-12 col-12">
        <div class="card h-100 mb-0">
          <form @submit.prevent="handleSubmit()">
            <div class="card-body">
              <div class="row gutters">
                <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                  <h6 class="mb-2 text-primary">Personal Details</h6>
                </div>
                <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                  <div class="row">
                    <div class="col-md-6">
                      <div class="form-group">
                        <label>First Name</label>
                        <input
                          type="text"
                          v-model="form.first_name"
                          class="form-control"
                          :class="{
                            'is-invalid':
                              submitted && v$.form.first_name.$error,
                          }"
                          placeholder="Enter first name"
                        />
                        <div v-if="submitted">
                          <span
                            class="error invalid-feedback"
                            v-for="error of v$.form.first_name.$errors"
                            :key="error.$uid"
                            >First name
                            {{ error.$message.toLowerCase() }}.</span
                          >
                        </div>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group">
                        <label>Last Name</label>
                        <input
                          type="text"
                          v-model="form.last_name"
                          class="form-control"
                          :class="{
                            'is-invalid': submitted && v$.form.last_name.$error,
                          }"
                          placeholder="Enter last name"
                        />
                        <div v-if="submitted">
                          <span
                            class="error invalid-feedback"
                            v-for="error of v$.form.last_name.$errors"
                            :key="error.$uid"
                            >Last name {{ error.$message.toLowerCase() }}.</span
                          >
                        </div>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group">
                        <label>Phone</label>
                        <input
                          type="text"
                          v-model="form.phone_number"
                          class="form-control"
                          :class="{
                            'is-invalid':
                              submitted && v$.form.phone_number.$error,
                          }"
                          placeholder="Enter phone"
                        />
                        <div v-if="submitted">
                          <span
                            class="error invalid-feedback"
                            v-for="error of v$.form.phone_number.$errors"
                            :key="error.$uid"
                            >Phone {{ error.$message.toLowerCase() }}.</span
                          >
                        </div>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group">
                        <label>Email</label>
                        <input
                          type="text"
                          v-model="form.email"
                          class="form-control"
                          :class="{
                            'is-invalid': submitted && v$.form.email.$error,
                          }"
                          placeholder="Enter email"
                        />
                        <div v-if="submitted">
                          <span
                            class="error invalid-feedback"
                            v-for="error of v$.form.email.$errors"
                            :key="error.$uid"
                            >Email {{ error.$message.toLowerCase() }}.</span
                          >
                        </div>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group">
                        <label>Date of Birth</label>
                        <input
                          type="date"
                          class="form-control"
                          v-model="form.date_of_birth"
                        />
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div>
                        <div class="form-group">
                          <label>Profile</label>
                          <input
                            accept="image/jpeg"
                            type="file"
                            @change="handleImage"
                            class="form-control"
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="card-footer">
              <button type="submit" class="btn btn-sm btn-primary mr-1">
                <i class="fa fa-dot-circle-o"></i> Submit
              </button>
              <button type="reset" class="btn btn-sm btn-danger">
                <i class="fa fa-ban"></i> Reset
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapMutations } from "vuex";
import { email, required } from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import UserDataService from "@/services/UserDataService";
import {
  AUTHPROFILE,
  BREADCRUMB,
  LOADING_SPINNER_MUTATION,
} from "@/store/storeconstants";
import { createToast } from "mosha-vue-toastify";
import "mosha-vue-toastify/dist/style.css";

export default {
  setup() {
    const v$ = useVuelidate();
    return { v$ };
  },
  created() {
    document.title = "User Profile";
    this.breadcrumb("User Profile");
    this.retrieveProfile();
  },
  data() {
    return {
      lists: [],
      profile: null,
      form: {
        profile: "",
        email: "",
        last_name: "",
        first_name: "",
        phone_number: "",
        date_of_birth: "",
        role: "admin",
      },
      submitted: false,
    };
  },
  validations() {
    return {
      form: {
        first_name: { required },
        last_name: { required },
        phone_number: { required },
        email: { required, email },
      },
    };
  },
  methods: {
    ...mapMutations({
      isLoading: LOADING_SPINNER_MUTATION,
      breadcrumb: BREADCRUMB,
      authProfile: AUTHPROFILE,
    }),
    async handleImage(e) {
      const fileBase64 = await this.getBase64(e.target.files[0]);
      this.form.profile = this.removeBase64Prefix(fileBase64);
    },
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    getBase64(file) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader();

        reader.onload = function () {
          const result = reader.result;
          return resolve(result);
        };

        reader.onerror = function (error) {
          return reject(error);
        };

        reader.readAsDataURL(file);
      });
    },
    removeBase64Prefix(base64) {
      return base64.replace("data:image/jpeg;base64,", "");
    },
    async handleSubmit(e) {
      this.submitted = true;
      const isFormCorrect = await this.v$.$validate();

      if (!isFormCorrect) return;
      this.isLoading(true);
      let id = this.profile.id;
      await UserDataService.update(id, this.form)
        .then((response) => {
          console.log(response.data);
          this.isLoading(true);
          this.authProfile(response.data.profile);
          this.submitted = false;
          this.form = {};
          this.form.role = "admin";
          this.successToast();
          this.$router.push({ path: "/user" });
        })
        .catch((e) => {
          this.isLoading(false);
          this.submitted = false;
          console.log(e);
        });
    },
    retrieveProfile() {
      let vm = this;
      this.isLoading(true);
      UserDataService.profile()
        .then((response) => {
          setTimeout(function () {
            vm.isLoading(false);
          }, 500);
          this.profile = response.data.data;
          console.log(response.data.data);

          this.form.profile = this.profile.profile;
          this.form.email = this.profile.email;
          this.form.last_name = this.profile.last_name;
          this.form.first_name = this.profile.first_name;
          this.form.phone_number = this.profile.phone_number;
          this.form.date_of_birth = this.profile.date_of_birth;
        })
        .catch((e) => {
          this.isLoading(false);
          console.log(e);
        });
    },
    successToast() {
      createToast("record created successfully.", {
        position: "top-right",
        type: "success",
        showIcon: "true",
        transition: "slide",
      });
    },
  },
};
</script>

<style>
.account-settings .user-profile {
  margin: 0 0 1rem 0;
  padding-bottom: 1rem;
  text-align: center;
}
.account-settings .user-profile .user-avatar {
  margin: 0 0 1rem 0;
}
.account-settings .user-profile .user-avatar img {
  width: 90px;
  height: 90px;
  -webkit-border-radius: 100px;
  -moz-border-radius: 100px;
  border-radius: 100px;
}
.account-settings .user-profile h5.user-name {
  margin: 0 0 0.5rem 0;
}
.account-settings .user-profile h6.user-email {
  margin: 0;
  font-size: 0.8rem;
  font-weight: 400;
  color: #9fa8b9;
}
.account-settings .about {
  margin: 2rem 0 0 0;
  text-align: center;
}
.account-settings .about h5 {
  margin: 0 0 15px 0;
  color: #007ae1;
}
.account-settings .about p {
  font-size: 0.825rem;
}

.card {
  background: #ffffff;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  border-radius: 5px;
  border: 0;
  margin-bottom: 1rem;
}
</style>