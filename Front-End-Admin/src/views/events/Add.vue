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
              <label>Title</label>
              <input
                type="text"
                v-model="form.title"
                class="form-control"
                :class="{
                  'is-invalid': submitted && v$.form.title.$error,
                }"
                placeholder="Enter title"
              />

              <div v-if="submitted">
                <span
                  class="error invalid-feedback"
                  v-for="error of v$.form.title.$errors"
                  :key="error.$uid"
                  >Title {{ error.$message.toLowerCase() }}.</span
                >
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
              <label>Mode</label>
              <Select2
                @onChangeMode="emitChangeMode($event)"
                :options="this.modeOptions"
                :emitTitle="this.modeEmitTitle"
              />
              <div v-if="submitted">
                <span
                  class="error invalid-feedback"
                  v-for="error of v$.form.mode.$errors"
                  :key="error.$uid"
                  >Mode {{ error.$message.toLowerCase() }}.</span
                >
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
              <label>Start Date</label>
              <input
                type="datetime-local"
                class="form-control"
                v-model="form.start_date"
                :class="{
                  'is-invalid': submitted && v$.form.start_date.$error,
                }"
              />
              <div v-if="submitted">
                <span
                  class="error invalid-feedback"
                  v-for="error of v$.form.start_date.$errors"
                  :key="error.$uid"
                  >Start date {{ error.$message.toLowerCase() }}.</span
                >
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
              <label>End Date</label>
              <input
                type="datetime-local"
                class="form-control"
                v-model="form.end_date"
                @keyup="form.end_date = $event.target.value"
                :class="{
                  'is-invalid': submitted && v$.form.end_date.$error,
                }"
              />
              <div v-if="submitted">
                <span
                  class="error invalid-feedback"
                  v-for="error of v$.form.end_date.$errors"
                  :key="error.$uid"
                  >End date {{ error.$message.toLowerCase() }}.</span
                >
              </div>
            </div>
          </div>
          <div class="col-md-12">
            <div class="form-group">
              <label>Location</label>
              <input
                type="text"
                v-model="form.location"
                class="form-control"
                :class="{
                  'is-invalid': submitted && v$.form.location.$error,
                }"
                placeholder="Enter location"
              />
              <div v-if="submitted">
                <span
                  class="error invalid-feedback"
                  v-for="error of v$.form.location.$errors"
                  :key="error.$uid"
                  >Location {{ error.$message.toLowerCase() }}.</span
                >
              </div>
            </div>
          </div>
          <div class="col-md-12">
            <div class="form-group">
              <label>Description</label>
              <TextEditor
                @onChangeDescription="emitChangeDescription($event)"
                :emitTitle="this.descriptionEmitTitle"
                :value="this.form.description"
              ></TextEditor>
            </div>
          </div>
        </div>
        <div class="col-md-12">
          <div>
            <div class="form-group">
              <label>Thumbnail</label>
              <input
                accept="image/jpeg"
                type="file"
                @change="handleImage"
                class="form-control"
                :class="{
                  'is-invalid': submitted && v$.form.thumbnail.$error,
                }"
                placeholder="Enter location"
              />
              <div v-if="submitted">
                <span
                  class="error invalid-feedback"
                  v-for="error of v$.form.thumbnail.$errors"
                  :key="error.$uid"
                  >Thumbnail {{ error.$message.toLowerCase() }}.</span
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
import EventDataService from "@/services/EventDataService";
import { BREADCRUMB, LOADING_SPINNER_MUTATION } from "@/store/storeconstants";
import { createToast } from "mosha-vue-toastify";
import "mosha-vue-toastify/dist/style.css";
import Select2 from "@/components/Fields/Select2";
import TextEditor from "@/components/Fields/TextEditor";

export default {
  setup() {
    const v$ = useVuelidate();
    return { v$ };
  },
  components: { Select2, TextEditor },
  // setup: () => ({ v$: useVuelidate() }),
  created() {
    document.title = "Create Event";
    this.breadcrumb("Create Event");
  },
  data() {
    return {
      form: {
        title: "",
        mode: "",
        start_date: "",
        end_date: "",
        location: "",
        description: "<p>test</p>",
        status: "Open",
        categories: [],
        thumbnail: "",
      },
      modeOptions: ["Offline", "Online"], //or [{id: key, text: value}, {id: key, text: value}]
      modeEmitTitle: "onChangeMode",
      descriptionEmitTitle: "onChangeDescription",
      submitted: false,
    };
  },
  validations() {
    return {
      form: {
        title: { required },
        mode: { required },
        start_date: { required },
        end_date: { required },
        location: { required },
        thumbnail: { required },
      },
    };
  },
  methods: {
    ...mapMutations({
      isLoading: LOADING_SPINNER_MUTATION,
      breadcrumb: BREADCRUMB,
    }),
    emitChangeMode(value) {
      this.form.mode = value;
    },
    emitChangeDescription(value) {
      this.form.description = value;
    },
    async handleImage(e) {
      const fileBase64 = await this.getBase64(e.target.files[0]);
      this.form.thumbnail = this.removeBase64Prefix(fileBase64);
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
      console.log(this.form.start_date);
      this.submitted = true;
      const isFormCorrect = await this.v$.$validate();

      if (!isFormCorrect) return;
      this.isLoading(true);
      await EventDataService.create(this.form)
        .then((response) => {
          this.submitted = false;
          this.isLoading(false);
          this.form = {};
          this.successToast();
          this.$router.push({ name: "Event All" });
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