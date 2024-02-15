<template>
    <router-link to="/profile" v-if="auth.is_auth" class="px-2 font-semibold bg-transparent rounded-lg flex justify-center align-middle
            " href="#">
        <div class="border-2 border-grey-400 overflow-hidden rounded-full">
            <img alt="" :src="imageUrl" class="align-middle w-10 h-10 object-cover
              " />
        </div>
    </router-link>
</template>
<script>
export default {
    props: {
        auth: Object
    },
    computed: {
        imageUrl: function () {
            if (this.auth.profile.profile) {
                return process.env.VUE_APP_STORAGE + this.auth.profile.profile
            }
            return 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png'
        }
    },
}
</script>