<template>
  <div class="card card-default">
    <form @submit.prevent="handleSubmit()">
      <div class="card-header">
        <h3 class="card-title">{{ this.$route.name }}</h3>
      </div>
      <div class="card-body">
        <div class="row">
          <div class="col-md-6">
            <div class="form-group">
              <label>First Name</label>
              <input
                type="text"
                v-model="form.first_name"
                class="form-control"
                :class="{
                  'is-invalid': submitted && v$.form.first_name.$error,
                }"
                placeholder="Enter first name"
              />
              <div v-if="submitted">
                <span
                  class="error invalid-feedback"
                  v-for="error of v$.form.first_name.$errors"
                  :key="error.$uid"
                  >First name {{ error.$message.toLowerCase() }}.</span
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
                  'is-invalid': submitted && v$.form.phone_number.$error,
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
            <div class="form-group">
              <label>Password</label>
              <input
                type="password"
                v-model="form.password"
                class="form-control"
                :class="{
                  'is-invalid': submitted && v$.form.password.$error,
                }"
                placeholder="Enter password"
              />
              <div v-if="submitted">
                <span
                  class="error invalid-feedback"
                  v-for="error of v$.form.password.$errors"
                  :key="error.$uid"
                  >Password {{ error.$message.toLowerCase() }}.</span
                >
              </div>
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
</template>

<script>
import { mapMutations } from "vuex";
import { email, required } from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import UserDataService from "@/services/UserDataService";
import { BREADCRUMB, LOADING_SPINNER_MUTATION } from "@/store/storeconstants";
import { createToast } from "mosha-vue-toastify";
import "mosha-vue-toastify/dist/style.css";

export default {
  setup() {
    const v$ = useVuelidate();
    return { v$ };
  },
  // setup: () => ({ v$: useVuelidate() }),
  created() {
    document.title = "Edit User";
    this.breadcrumb("Edit User");
    this.form.categories = [this.$route.query.cate_id];
  },
  mounted() {
    this.getList(this.$route.params.id);
  },
  data() {
    return {
      form: {
        profile: "",
        email: "",
        last_name: "",
        first_name: "",
        phone_number: "",
        role: "admin",
      },
      currentList: null,
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
        password: { required },
      },
    };
  },

  methods: {
    ...mapMutations({
      isLoading: LOADING_SPINNER_MUTATION,
      breadcrumb: BREADCRUMB,
    }),
    async handleImage(e) {
      const fileBase64 = await this.getBase64(e.target.files[0]);
      this.form.profile = this.removeBase64Prefix(fileBase64);
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
    getList: function (id) {
      var vm = this;
      UserDataService.get(id)
        .then(async (response) => {
          vm.currentList = response.data;
          vm.form.profile = response.data.profile;
          vm.form.email = response.data.email;
          vm.form.last_name = response.data.last_name;
          vm.form.first_name = response.data.first_name;
          vm.form.phone_number = response.data.phone_number;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    async handleSubmit(e) {
      this.submitted = true;
      const isFormCorrect = await this.v$.$validate();

      if (!isFormCorrect) return;
      this.isLoading(true);

      await UserDataService.update(this.currentList.id, this.form)
        .then((response) => {
          this.submitted = false;
          this.isLoading(false);
          this.form = {};
          this.successToast();
          this.$router.push({ path: "/user" });
        })
        .catch((e) => {
          this.isLoading(false);
          this.submitted = false;
          console.log(e);
        });
    },
    successToast() {
      createToast("record updated successfully.", {
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
</style>