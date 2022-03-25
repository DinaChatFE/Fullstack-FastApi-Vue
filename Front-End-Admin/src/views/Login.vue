<template>
  <div class="login-box container justify-content-center" style="width: 400px">
    <div class="login-logo">
      <div class="login-logo" style="text-align: center; font-size: 24px">
        <a href="#" style="color: #000"><strong>EVENT-NEWS</strong></a>
      </div>
    </div>
    <div class="card">
      <div class="card-body login-card-body">
        <p style="text-align: center">Sign in to start your session</p>
        <p
          v-if="this.unauthentication"
          style="color: red; text-align: center; font-size: 14px"
        >
          {{ this.unauthentication }}
        </p>
        <form @submit.prevent="onLogin()">
          <label>Email</label>
          <div class="input-group">
            <input
              type="text"
              v-model="phone"
              class="form-control"
              aria-invalid="true"
              v-bind:class="{ 'is-invalid': errors.phone }"
              placeholder="Enter your phone"
            />
            <div class="input-group-append">
              <span class="input-group-text">
                <i class="icon-envelope icons"></i>
              </span>
            </div>
          </div>
          <span class="error invalid-feedback" v-if="errors.phone">{{
            errors.phone
          }}</span>
          <label class="mt-3">Password</label>
          <div class="input-group">
            <input
              type="password"
              v-model="password"
              class="form-control"
              aria-invalid="true"
              v-bind:class="{ 'is-invalid': errors.password }"
              placeholder="Enter your password"
            />
            <div class="input-group-append">
              <span class="input-group-text">
                <i class="icon-lock icons"></i>
              </span>
            </div>
          </div>
          <span class="error invalid-feedback" v-if="errors.password">{{
            errors.password
          }}</span>
          <div class="row mt-3">
            <div class="col-12">
              <button
                type="submit"
                class="btn btn-primary btn-block"
                id="btn-login"
                :disabled="isDisable"
              >
                <span>Sign In</span>
              </button>
            </div>
            <div class="col-12" style="text-align: center; padding-top: 10px">
              <!-- <router-link :to="'/sign-up'">
                <p style="font-size: 14px; color: black">
                  Don't have an account register here.
                </p>
              </router-link> -->
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
import { mapActions, mapMutations } from "vuex";
import LoginValidations from "@/services/LoginValidations";
import { LOGIN_ACTION, LOADING_SPINNER_MUTATION } from "@/store/storeconstants";
export default {
  data() {
    return {
      phone: "",
      password: "",
      errors: [],
      isDisable: false,
      unauthentication: "",
    };
  },
  created() {
    document.title = "Sign In";
  },
  methods: {
    ...mapActions("auth", {
      processLogin: LOGIN_ACTION,
    }),
    ...mapMutations({
      isLoading: LOADING_SPINNER_MUTATION,
    }),
    async onLogin() {
      // check validation
      let validations = new LoginValidations(this.phone, this.password);
      this.errors = validations.checkValidaiotns();
      if ("phone" in this.errors || "password" in this.errors) {
        return false;
      }
      this.isLoading(true);
      this.isDisable = true;
      await this.processLogin({
        phone: this.phone,
        password: this.password,
        role: 'admin'
      }).catch((error) => {
        this.isLoading(false);
        this.isDisable = false;
        this.unauthentication = error.data.detail;
        console.log(error.data.detail);
      });
      this.isLoading(false);
      this.isDisable = false;
      this.$router.push({ path: "/" });
    },
  },
};
</script>
<style>
.form-control {
  border: 1px solid #000;
}
</style>
