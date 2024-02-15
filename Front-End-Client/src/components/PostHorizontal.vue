<template>
  <div class="mt-6">
    <div class="px-10 py-6 mx-auto bg-white rounded-lg shadow-md">
      <div class="flex items-center justify-between" v-for="category in data.categories_props" v-bind:key="category.id">
        <span class="font-light text-gray-600">{{data.created_at_format}}</span
        ><router-link
          :to="'/news?q='+ category.name"
          href="#"
          class="
            px-2
            py-1
            font-bold
            text-gray-100
            bg-gray-600
            rounded
            hover:bg-gray-500
          "
          >{{category.name}}</router-link
        >
      </div>
      <div class="mt-2 text-left" >
        <router-link :to="'/detail/news/' + data.id" href="#" class="text-2xl font-bold text-gray-700 hover:underline line-clamp-1"
          >{{data.title}}</router-link
        >
        <p class="mt-2 text-gray-600 line-clamp-3" v-html="data.description">
        </p>
      </div>
      <div class="flex items-center justify-between mt-4">
        <router-link :to="'/detail/news/'+ data.id" href="#" class="text-blue-500 hover:underline">Read more</router-link>
        <div>
          <a href="#" class="flex items-center"
            ><img
              v-if="data.created_by?.profile"
              :src="envStorage + this.data.created_by.profile"
              alt="avatar"
              class="hidden object-cover w-10 h-10 mx-4 rounded-full sm:block"
            />
            <h1 class="font-bold text-gray-700 hover:underline"> {{ data.created_by?.first_name }} </h1>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return  {
      envStorage: process.env.VUE_APP_STORAGE
    }
  },
  props: ['data']
};
</script>

<style>
</style>