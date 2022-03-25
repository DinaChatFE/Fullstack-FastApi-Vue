<template>
  <transition-group
    tag="div"
    name="list-complete"
    class="flex flex-wrap mx-auto"
  >
    <li
      v-for="item in data"
      :key="item.id"
      @click="deleteProduct(item.id)"
      class="
        list-complete-item
        shadow-md
        duration-75
        list-none
        text-left
        p-4
        my-1
        hover:bg-gray-50
        mt-4
        sm:w-full
        lg:w-1/4
        md:w-1/2
        rounded-md
      "
    >
      <img :src="item.img" class="hover:bg-gray-100 mx-auto h-60" alt="image" />
      <div class="flex justify-between">
        <a class="text-left py-2 truncate uppercase text-md">{{ item.name }}</a>
        <p class="py-2 font-bold whitespace-nowrap">x {{ item.quantity }}</p>
      </div>
      <p class="text-blue-500 font-bold py-2 float-left">$ {{ item.price }}</p>
      <p class="text-gray-400 text-sm py-2 float-right">
        {{ moment(item.created_at).fromNow() }}
      </p>
    </li>
  </transition-group>
</template>

<script>
import moment from "moment";
export default {
  setup() {
    return {
      moment,
    };
  },
  props: {
    data: Array,
    deleteProduct: Function,
  },
};
</script>

<style scoped>
.list-complete-item {
  transition: transform 0.8s ease;
  display: inline-block;
}

.list-complete-enter-from,
.list-complete-leave-to {
  opacity: 0;
  transform: translateY(30px);
}

.list-complete-leave-active {
  position: absolute;
}
</style>