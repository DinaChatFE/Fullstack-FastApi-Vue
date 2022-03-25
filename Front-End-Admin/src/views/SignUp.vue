<template>
  <div class="login-box container justify-content-center" style="width: 400px">
    <div class="login-logo">
      <div class="login-logo" style="text-align: center; font-size: 24px">
        <a href="#" style="color: #000"><strong>EVENT-NEWS</strong></a>
      </div>
    </div>
    <div class="card">
      <div class="card-body login-card-body">
        <p style="text-align: center">Signup your account.</p>
        <form @submit.prevent="handleSubmit()">
          <label class="mt-1">First Name</label>
          <div class="input-group">
            <input
              type="text"
              class="form-control"
              :class="{
                'is-invalid': submitted && v$.form.first_name.$error,
              }"
              aria-invalid="true"
              placeholder="Enter your first name"
              v-model="form.first_name"
            />
            <div class="input-group-append">
              <span class="input-group-text">
                <i class="icons icon-user"></i>
              </span>
            </div>
          </div>
          <div v-if="submitted">
            <span
              class="error invalid-feedback"
              v-for="error of v$.form.first_name.$errors"
              :key="error.$uid"
              >First name {{ error.$message.toLowerCase() }}.</span
            >
          </div>
          <label class="mt-1">Last Name</label>
          <div class="input-group">
            <input
              type="text"
              class="form-control"
              aria-invalid="true"
              placeholder="Enter your last name"
              v-model="form.last_name"
              :class="{
                'is-invalid': submitted && v$.form.last_name.$error,
              }"
            />
            <div class="input-group-append">
              <span class="input-group-text">
                <i class="icons icon-user"></i>
              </span>
            </div>
          </div>
          <div v-if="submitted">
            <span
              class="error invalid-feedback"
              v-for="error of v$.form.last_name.$errors"
              :key="error.$uid"
              >Last name {{ error.$message.toLowerCase() }}.</span
            >
          </div>
          <label class="mt-1">Phone</label>
          <div class="input-group">
            <input
              type="text"
              class="form-control"
              aria-invalid="true"
              placeholder="Enter your phone"
              v-model="form.phone_number"
              :class="{
                'is-invalid': submitted && v$.form.phone_number.$error,
              }"
            />
            <div class="input-group-append">
              <span class="input-group-text">
                <i class="icons icon-call-end"></i>
              </span>
            </div>
          </div>
          <div v-if="submitted">
            <span
              class="error invalid-feedback"
              v-for="error of v$.form.phone_number.$errors"
              :key="error.$uid"
              >Phone {{ error.$message.toLowerCase() }}.</span
            >
          </div>
          <label class="mt-1">Email</label>
          <div class="input-group">
            <input
              type="text"
              class="form-control"
              aria-invalid="true"
              placeholder="Enter your email"
              v-model="form.email"
              :class="{
                'is-invalid': submitted && v$.form.email.$error,
              }"
            />
            <div class="input-group-append">
              <span class="input-group-text">
                <i class="icon-envelope icons"></i>
              </span>
            </div>
          </div>
          <div v-if="submitted">
            <span
              class="error invalid-feedback"
              v-for="error of v$.form.email.$errors"
              :key="error.$uid"
              >Email {{ error.$message.toLowerCase() }}.</span
            >
          </div>
          <label class="mt-1">Password</label>
          <div class="input-group">
            <input
              type="password"
              class="form-control"
              aria-invalid="true"
              placeholder="Enter your password"
              v-model="form.password"
              :class="{
                'is-invalid': submitted && v$.form.password.$error,
              }"
            />
            <div class="input-group-append">
              <span class="input-group-text">
                <i class="icons icon-lock"></i>
              </span>
            </div>
          </div>
          <div v-if="submitted">
            <span
              class="error invalid-feedback"
              v-for="error of v$.form.password.$errors"
              :key="error.$uid"
              >Password {{ error.$message.toLowerCase() }}.</span
            >
          </div>
          <label class="mt-1">Confirm password</label>
           <div class="input-group">
            <input
              type="password"
              class="form-control"
              aria-invalid="true"
              placeholder="Enter your Confirm password"
              v-model="form.confirm_password"
            />
            <div class="input-group-append">
              <span class="input-group-text">
                <i class="icons icon-lock"></i>
              </span>
            </div>
          </div>
          <div class="row mt-3">
            <div class="col-12">
              <button
                type="submit"
                class="btn btn-primary btn-block"
                id="btn-login"
              >
                <span>Sign up</span>
              </button>
            </div>
            <div class="col-12" style="text-align: center; padding-top: 10px">
              <router-link :to="'/sign-in'">
                <p style="font-size: 14px; color: black">Login</p>
              </router-link>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
import { mapMutations } from "vuex";
import { email, required } from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import UserDataService from "@/services/UserDataService";
import { LOADING_SPINNER_MUTATION } from "@/store/storeconstants";
import { createToast } from "mosha-vue-toastify";
import "mosha-vue-toastify/dist/style.css";

export default {
  setup() {
    const v$ = useVuelidate();
    return { v$ };
  },
  // setup: () => ({ v$: useVuelidate() }),
  created() {
    document.title = "Signup";
  },
  data() {
    return {
      form: {
        profile: "",
        email: "",
        password: "",
        last_name: "",
        first_name: "",
        phone_number: "",
        role: "admin",
        date_of_birth: "1994-10-12",
        confirm_password: "",
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
        password: { required },
      },
    };
  },
  methods: {
    ...mapMutations({
      isLoading: LOADING_SPINNER_MUTATION,
    }),
    async handleSubmit(e) {
      this.submitted = true;
      const isFormCorrect = await this.v$.$validate();

      if (!isFormCorrect) return;
      this.isLoading(true);
      await UserDataService.create(this.form)
        .then((response) => {
          console.log(response.data);
          this.submitted = false;
          this.isLoading(false);
          this.form = {};
          this.form.role = "admin";
          this.form.date_of_birth = "1994-10-12";
          this.form.confirm_password = "12345678";
          this.successToast();
          this.$router.push({ path: "/sign-in" });
        })
        .catch((e) => {
          this.isLoading(false);
          this.submitted = false;
          console.log(e);
        });
    },
    successToast() {
      createToast("signup successfully.", {
        position: "top-right",
        type: "success",
        showIcon: "true",
        transition: "zoom",
      });
    },
  },
};

$(function () {
  $(".select2").select2();
});
</script>

<style>
.invalid-feedback {
  display: block;
}
input,
input::-webkit-input-placeholder {
  font-size: 12px;
  /* line-height: 3; */
}
.input-group-text {
  border: 1px solid #000;
  border-radius: 0px 2px 2px 0px !important;
}
label {
  font-weight: normal !important;
  color: #000;
}
.content-wrapper {
  background-color: #fff !important;
}
.login-box,
.register-box {
  margin-top: 5% !important;
}
#btn-login {
  border-radius: 0;
  text-transform: uppercase;
  font-weight: bold;
  background: black;
  border: 0px;
}
.form-control {
  border-radius: 2px;
  border: 1px solid #000;
}
</style>
