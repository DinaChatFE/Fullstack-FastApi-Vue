<template>
  <!-- Breadcrumb -->
  <ol class="breadcrumb">
    <li class="breadcrumb-item">Home</li>
    <li class="breadcrumb-item active">{{ this.breadcrumb }}</li>
    <!-- Breadcrumb Menu-->
    <li class="breadcrumb-menu d-md-down-none">
      <div
        class="btn-group"
        role="group"
        aria-label="Button group with nested dropdown"
      >
        <a class="btn"><i class="icon-speedometer"></i> &nbsp;Dashboard</a>
      </div>
    </li>
  </ol>
</template>

<script>
import { mapState } from "vuex";
export default {
  computed: {
    ...mapState({
      breadcrumb: (state) => state.breadcrumb,
    }),
  },
};
</script>

<style>
</style>