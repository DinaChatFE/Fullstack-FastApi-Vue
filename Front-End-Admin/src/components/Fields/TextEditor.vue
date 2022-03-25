<template>
  <textarea v-model="value" class="form-control"></textarea>
</template>

<script>
export default {
  name: "TextEditor",
  props: ["value", "emitTitle"],
  mounted: function () {
    var vm = this;
    $(this.$el).summernote({
      height: 150,
      callbacks: {
        onChange: function (contents, $editable) {
          vm.$emit(vm.emitTitle, contents);
        },
      },
    });
  },
  watch: {
    value: function (value) {
      // update value
      $(this.$el).text(value);
    },
  },
};
</script>
<style>
.select2-container--default .select2-selection--single {
  border-radius: 2px !important;
  border: 1px solid #c2cfd6;
}
.select2-container .select2-selection--single {
  height: 35px !important;
}
.select2-container--default
  .select2-selection--single
  .select2-selection__rendered {
  color: #6f848f !important;
  line-height: 34px !important;
}
.select2-container--default
  .select2-selection--single
  .select2-selection__arrow
  b {
  margin-left: -5px !important;
  margin-top: 2px !important;
}
</style>