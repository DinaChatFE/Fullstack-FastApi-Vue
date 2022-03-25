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
              <label>Category</label>
              <Select2
                @onChangeCategory="emitChangeCategory($event)"
                :options="this.categoryOptions"
                :emitTitle="this.categoryEmitTitle"
              />
              <div v-if="submitted">
                <span
                  class="error invalid-feedback"
                  v-for="error of v$.form.categories.$errors"
                  :key="error.$uid"
                  >Category {{ error.$message.toLowerCase() }}.</span
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
              <div v-if="submitted">
                <span
                  class="error invalid-feedback"
                  v-for="error of v$.form.description.$errors"
                  :key="error.$uid"
                  >Description {{ error.$message.toLowerCase() }}.</span
                >
              </div>
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
import NewsDataService from "@/services/NewsDataService";
import CaregoryDataService from "@/services/CaregoryDataService";
import { BREADCRUMB, LOADING_SPINNER_MUTATION } from "@/store/storeconstants";
import { createToast } from "mosha-vue-toastify";
import Select2 from "@/components/Fields/Select2";
import TextEditor from "@/components/Fields/TextEditor";
import "mosha-vue-toastify/dist/style.css";

export default {
  setup() {
    const v$ = useVuelidate();
    return { v$ };
  },
  components: { Select2, TextEditor },
  // setup: () => ({ v$: useVuelidate() }),
  created() {
    document.title = "Create News";
    this.breadcrumb("Create News");
    this.retrieveCategories();
  },
  data() {
    return {
      form: {
        title: "",
        description: "<p>test</p>",
        categories: [],
        thumbnail: "",
        content: "test",
      },
      descriptionEmitTitle: "onChangeDescription",
      categoryOptions: [], //or [{id: key, text: value}, {id: key, text: value}]
      categoryEmitTitle: "onChangeCategory",
      submitted: false,
    };
  },
  validations() {
    return {
      form: {
        title: { required },
        thumbnail: { required },
        categories: { required },
        description: { required },
      },
    };
  },
  methods: {
    ...mapMutations({
      isLoading: LOADING_SPINNER_MUTATION,
      breadcrumb: BREADCRUMB,
    }),
    emitChangeCategory(value) {
      this.form.categories = [value];
    },
    emitChangeDescription(value) {
      this.form.description = value;
    },
    retrieveCategories() {
      let vm = this;
      CaregoryDataService.getAll()
        .then((response) => {
          var cats = [];
          response.data.forEach((value, index) => {
            cats.push({
              id: value.id,
              text: value.name,
            });
          });
          vm.categoryOptions = cats;
        })
        .catch((e) => {
          console.log(e);
        });
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
      this.submitted = true;
      const isFormCorrect = await this.v$.$validate();

      if (!isFormCorrect) return;
      this.isLoading(true);
      await NewsDataService.create(this.form)
        .then((response) => {
          console.log(response.data);
          this.submitted = false;
          this.isLoading(false);
          this.form = {};
          this.successToast();
          this.$router.push({ path: "/news" });
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