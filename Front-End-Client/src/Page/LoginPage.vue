<template>
  <section class="flex flex-col md:flex-row h-screen items-center">
    <div
      class="bg-indigo-600 hidden lg:block w-full md:w-1/2 xl:w-2/3 h-screen"
    >
      <img
        src="https://images.unsplash.com/photo-1492684223066-81342ee5ff30?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZXZlbnR8ZW58MHx8MHx8&w=1000&q=80"
        alt=""
        class="w-full h-full object-cover"
      />
    </div>
    <div
      class="
        bg-white
        w-full
        md:max-w-md
        lg:max-w-full
        md:mx-auto md:mx-0 md:w-1/2
        xl:w-1/3
        h-screen
        px-6
        lg:px-16
        xl:px-12
        flex
        items-center
        justify-center
        relative
      "
    >
      <div class="w-full h-100 ">
        <h1 class="text-xl md:text-2xl font-bold leading-tight mt-12">
          Log in to your account
        </h1>
        <div class="flex absolute top-10 left-10 hover:underline cursor-pointer">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M15 19l-7-7 7-7"
            /></svg
          >
           <router-link to="/"><a>Home</a></router-link>
        </div>
        <form @submit="login" class="mt-6" action="#" method="POST">
          <div>
            <label class="block text-gray-700 text-left text-sm"
              >Email Address</label
            >
            <input
              v-model="body.email"
              @blur="v$.body.email.$touch"
              type="email"
              placeholder="Enter Email Address"
              class="
                w-full
                px-4
                py-3
                rounded-lg
                bg-gray-200
                mt-2
                border
                focus:border-blue-500 focus:bg-white focus:outline-none
              "
              :class="v$.body.email.$error ? 'border-red-500 focus:border-red-500' : ''"
            />
          </div>
          <span
            v-if="error_raise"
            class="
              flex
              items-center
              font-medium
              tracking-wide
              text-red-500 text-xs
              mt-1
              ml-1
            "
          >
            Please check your email and password again before login
          </span>
          <span
            v-if="v$.body.email.$error"
            class="
              flex
              items-center
              font-medium
              tracking-wide
              text-red-500 text-xs
              mt-1
              ml-1
            "
          >
            {{ v$.body.email.email.$message }},
            {{ v$.body.email.required.$message }}
          </span>
          <p v-for="error of v$.$errors" :key="error.$uid"></p>
          <div class="mt-4">
            <label class="block text-gray-700 text-left">Password</label>
            <input
              v-model="body.password"
              @blur="v$.body.password.$touch"
              type="password"
              placeholder="Enter Password"
              minlength="6"
              class="
                w-full
                px-4
                py-3
                rounded-lg
                bg-gray-200
                mt-2
                border
                focus:border-blue-500 focus:bg-white focus:outline-none
              "
               :class="v$.body.password.$error ? 'border-red-500 focus:border-red-500' : ''"
            />
          </div>
          <span
            v-if="v$.body.password.$error"
            class="
              flex
              items-center
              font-medium
              tracking-wide
              text-red-500 text-xs
              mt-1
              ml-1
            "
          >
              {{v$.body.password.required.$message}}
          </span>

          <div class="text-right mt-2">
            <a
              href="#"
              class="
                text-sm
                font-semibold
                text-gray-700
                hover:text-blue-700
                focus:text-blue-700
              "
              >Forgot Password?</a
            >
          </div>

          <button
            type="submit"
            class="
              w-full
              block
              bg-indigo-500
              hover:bg-indigo-400
              focus:bg-indigo-400
              text-white
              font-semibold
              rounded-lg
              px-4
              py-3
              mt-6
            "
          >
            Log In
          </button>
        </form>

        <hr class="my-6 border-gray-300 w-full" />

        <button
          type="button"
          class="
            w-full
            block
            bg-white
            hover:bg-gray-100
            focus:bg-gray-100
            text-gray-900
            font-semibold
            rounded-lg
            px-4
            py-3
            border border-gray-300
          "
        >
          <div class="flex items-center justify-center">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              xmlns:xlink="http://www.w3.org/1999/xlink"
              class="w-6 h-6"
              viewBox="0 0 48 48"
            >
              <defs>
                <path
                  id="a"
                  d="M44.5 20H24v8.5h11.8C34.7 33.9 30.1 37 24 37c-7.2 0-13-5.8-13-13s5.8-13 13-13c3.1 0 5.9 1.1 8.1 2.9l6.4-6.4C34.6 4.1 29.6 2 24 2 11.8 2 2 11.8 2 24s9.8 22 22 22c11 0 21-8 21-22 0-1.3-.2-2.7-.5-4z"
                />
              </defs>
              <clipPath id="b">
                <use xlink:href="#a" overflow="visible" />
              </clipPath>
              <path clip-path="url(#b)" fill="#FBBC05" d="M0 37V11l17 13z" />
              <path
                clip-path="url(#b)"
                fill="#EA4335"
                d="M0 11l17 13 7-6.1L48 14V0H0z"
              />
              <path
                clip-path="url(#b)"
                fill="#34A853"
                d="M0 37l30-23 7.9 1L48 0v48H0z"
              />
              <path
                clip-path="url(#b)"
                fill="#4285F4"
                d="M48 48L17 24l-4-3 35-10z"
              />
            </svg>
            <span class="ml-4"> Log in with Google</span>
          </div>
        </button>

        <p class="mt-8">
          Need an account?
          <router-link to="/register">
            <a href="#" class="text-blue-500 hover:text-blue-700 font-semibold"
              >Create an account</a
            >
          </router-link>
        </p>
      </div>
    </div>
  </section>
</template>

<script>
import { computed } from "vue";
import { useStore } from "vuex";
import { LOGIN, PROFILE } from "../store/type";
import useVuelidate from "@vuelidate/core";
import { required, email } from "@vuelidate/validators";

export default {
  name: "LoginPage",
  data() {
    const store = useStore();

    return {
      body: {
        email: "",
        password: "",
      },
      v$: useVuelidate(),
      is_auth: computed(() => store.state.auth.is_auth),
      profile: computed(() => store.state.auth.profile),
      error_raise: computed(()=> store.state.auth.error_raise),
      login(e) {
        e.preventDefault();
        store.dispatch({
          type: LOGIN,
          credential: this.body,
        });
        store.dispatch(PROFILE);
      },
    };
  },
  validations() {
    return {
      body: { email: { required, email }, password: { required } },
    };
  },
  created() {
    const store = useStore();
    store.dispatch(PROFILE);
  },
};
</script>

<style>
</style>