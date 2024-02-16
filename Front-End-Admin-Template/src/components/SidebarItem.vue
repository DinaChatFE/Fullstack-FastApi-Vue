<template>
    <router-link class="flex items-center px-6 py-2 mt-4 duration-200 border-l-4"
        :class="[$route.name === routeName ? activeClass : inactiveClass]" :to="{ name: routeName }">
        <svg class="w-5 h-5" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M2 10C2 5.58172 5.58172 2 10 2V10H18C18 14.4183 14.4183 18 10 18C5.58172 18 2 14.4183 2 10Z"
                fill="currentColor" />
            <path d="M12 2.25195C14.8113 2.97552 17.0245 5.18877 17.748 8.00004H12V2.25195Z" fill="currentColor" />
        </svg>

        <span class="mx-4">{{ title }}</span>
    </router-link>
</template>
<script lang="ts" setup>
defineProps<{
    title: string,  
    routeName: string,
    activeClass: string,
    inactiveClass: string, 
}>()
</script>