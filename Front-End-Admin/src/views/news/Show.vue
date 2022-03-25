<template>
  <div class="card card-default">
    <div class="card-header">News</div>
    <div class="card-body">
      <div class="row">
        
        <div class="col-md-12 my-2">Title: {{ data?.title }}</div>
        <div class="col-md-12 my-2">
          Created at: {{ data?.created_at_format }}
        </div>
        <div class="col-md-12 my-2">
          Category:
          <b class="mr-2" v-for="d in data?.categories_props" v-bind:key="d.id"
            >{{ d.name }} </b
          >
        </div>

        <div class="col-md-12 my-2"><span>Description: </span> <div v-html="data?.description"></div></div>
        
        
        <div class="col-md-12 my-4">
          Thumbnail:
          <img
           class="ml-4"
            width="200"
            style="border-radius: 10px;"
            v-bind:src="'http://127.0.0.1:8000/static/images/' + data?.thumbnail"
            :alt="data?.thumbnail"
          />
        </div>
      </div>
    </div>
    <div class="card-footer">
      <a href="#"> Back</a>
    </div>
  </div>
</template>

<script>
import NewsDataService from "@/services/NewsDataService";

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
    getList(id) {
      let vm = this;
      NewsDataService.get(id)
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