<template>
  <div class="card card-default">
    <form @submit.prevent="handleSubmit()">
      <div class="card-header">
        <h3 class="card-title">{{ this.$route.name }}</h3>
      </div>
      <div class="card-body">
        <div class="row">
          <div class="col-md-12">
            <div class="form-group">
              <label>Name</label>
              <input
                type="text"
                v-model="form.name"
                class="form-control"
                :class="{
                  'is-invalid': submitted && v$.form.name.$error,
                }"
                placeholder="Enter name"
              />

              <div v-if="submitted">
                <span
                  class="error invalid-feedback"
                  v-for="error of v$.form.name.$errors"
                  :key="error.$uid"
                  >Name {{ error.$message.toLowerCase() }}.</span
                >
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
import { required } from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import CategoryDataService from "@/services/CategoryDataService";
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
    document.title = "Create Category";
    this.breadcrumb("Create Category");
  },
  data() {
    return {
      form: {
        name: "",
      },
      submitted: false,
    };
  },
  validations() {
    return {
      form: {
        name: { required },
      },
    };
  },
  methods: {
    ...mapMutations({
      isLoading: LOADING_SPINNER_MUTATION,
      breadcrumb: BREADCRUMB,
    }),
    async handleSubmit(e) {
      console.log(this.form.start_date);
      this.submitted = true;
      const isFormCorrect = await this.v$.$validate();

      if (!isFormCorrect) return;
      this.isLoading(true);
      await CategoryDataService.create(this.form)
        .then((response) => {
          console.log(response.data);
          this.submitted = false;
          this.isLoading(false);
          this.form = {};
          this.successToast();
          this.$router.push({ path: "/category" });
        })
        .catch((e) => {
          this.isLoading(false);
          this.submitted = false;
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
</style>