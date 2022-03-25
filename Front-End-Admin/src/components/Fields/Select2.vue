<template>
  <select value="2" style="width: 100%"></select>
</template>

<script>
export default {
  name: "MySelect2",
  props: ["options", "value", "ajax", "tags", "emitTitle"],
  mounted: function () {
    var vm = this;
    let options = [];
    options.push({
      id: "",
      text: "Choose...", // Supports vue-i18n, just put 'this.$t('select2.choose')' here
      disabled: true,
      // selected: true,
    });

    options = options.concat(this.options);
    console.log(options);

    $(this.$el)
      // init select2
      .select2({ ajax: this.ajax, tags: this.tags, data: options })
      .val(this.value)
      .trigger("change")
      // emit event on change.
      .on("change", function () {
        vm.$emit(vm.emitTitle, this.value);
      });
  },
  watch: {
    value: function (value) {
      // update value
      $(this.$el).val(value).trigger("change");
    },
    options: function (newoptions) {
      let options = [];
      options.push({
        id: "",
        text: "Choose...", // Supports vue-i18n, just put 'this.$t('select2.choose')' here
        disabled: true,
        selected: true,
      });
      options = options.concat(newoptions);
      $(this.$el).empty().select2({ data: options });
    },
  },
  destroyed: function () {
    $(this.$el).off().select2("destroy");
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